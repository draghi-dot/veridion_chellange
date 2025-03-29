import json
import random
import numpy as np
from scipy.stats import spearmanr, kendalltau
import math

host = "GET http://172.18.4.158:8000/get-word"
post_url = f"{host}/submit-word"
get_url = f"{host}/get-word"
status_url = f"{host}/status"


def load_words(filename):
    """
    Loads words from the JSON file and returns a list of dictionaries.
    Each dictionary has 'Nume' and 'cost' keys.
    """
    with open(filename, "r") as f:
        data = json.load(f)
    # Convert dictionary values into a list.
    words = [value for key, value in data.items()]
    return words

def get_ground_truth_ranking(words):
    """
    Ground truth ranking is obtained by sorting words by cost (ascending).
    Lower cost is assumed better.
    """
    return sorted(words, key=lambda w: w["cost"])

def get_predicted_ranking(words, noise_level=0.5):
    """
    Simulates a predicted ranking by adding noise to each word's cost.
    """
    predicted = []
    for w in words:
        noisy_cost = w["cost"] + random.uniform(-noise_level, noise_level)
        predicted.append({"Nume": w["Nume"], "cost": w["cost"], "score": noisy_cost})
    predicted_sorted = sorted(predicted, key=lambda w: w["score"])
    return predicted_sorted

def extract_ranks(ranking):
    """
    Returns a dictionary mapping each word's name to its rank (starting at 1).
    """
    rank_dict = {}
    for i, w in enumerate(ranking, start=1):
        rank_dict[w["Nume"]] = i
    return rank_dict

def compute_spearman(ground_truth, predicted):
    gt_ranks = extract_ranks(ground_truth)
    pred_ranks = extract_ranks(predicted)
    common_words = list(gt_ranks.keys())
    gt_list = [gt_ranks[w] for w in common_words]
    pred_list = [pred_ranks[w] for w in common_words]
    corr, p_val = spearmanr(gt_list, pred_list)
    return corr, p_val

def compute_kendall(ground_truth, predicted):
    gt_ranks = extract_ranks(ground_truth)
    pred_ranks = extract_ranks(predicted)
    common_words = list(gt_ranks.keys())
    gt_list = [gt_ranks[w] for w in common_words]
    pred_list = [pred_ranks[w] for w in common_words]
    tau, p_val = kendalltau(gt_list, pred_list)
    return tau, p_val

def dcg(scores):
    """
    Computes Discounted Cumulative Gain for a list of relevance scores.
    """
    dcg_val = 0.0
    for i, score in enumerate(scores, start=1):
        dcg_val += score / np.log2(i + 1)
    return dcg_val

def compute_ndcg(ground_truth, predicted, k=None):
    """
    Computes normalized DCG (nDCG) at cutoff k.
    For relevance, we use: relevance = (max_cost - cost + 1), so lower cost implies higher relevance.
    """
    if k is None:
        k = len(predicted)
    max_cost = max(w["cost"] for w in ground_truth)
    def relevance(word):
        return max_cost - word["cost"] + 1

    pred_scores = [relevance(w) for w in predicted[:k]]
    dcg_val = dcg(pred_scores)
    
    ideal = sorted(ground_truth, key=lambda w: relevance(w), reverse=True)
    ideal_scores = [relevance(w) for w in ideal[:k]]
    idcg_val = dcg(ideal_scores)
    
    return dcg_val / idcg_val if idcg_val > 0 else 0

def compute_mrr(predicted, relevant_word):
    """
    Computes Mean Reciprocal Rank (MRR) for a single query,
    assuming that relevant_word is the only correct answer.
    """
    for rank, w in enumerate(predicted, start=1):
        if w["Nume"] == relevant_word:
            return 1.0 / rank
    return 0.0

def compute_precision_at_k(ground_truth, predicted, k):
    """
    Computes Precision at K.
    Here, we define relevant words as those in the top half of the ground truth ranking.
    """
    gt_ranks = extract_ranks(ground_truth)
    threshold_rank = len(ground_truth) // 2  # top half are "relevant"
    relevant_words = {w for w, r in gt_ranks.items() if r <= threshold_rank}
    top_k = [w["Nume"] for w in predicted[:k]]
    relevant_in_top_k = [w for w in top_k if w in relevant_words]
    return len(relevant_in_top_k) / k

def compute_mae_rmse(ground_truth, predicted):
    """
    Computes the Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE)
    between the ranking positions of ground truth and predicted ranking.
    """
    gt_ranks = extract_ranks(ground_truth)
    pred_ranks = extract_ranks(predicted)
    errors = [abs(gt_ranks[w] - pred_ranks[w]) for w in gt_ranks]
    mae = sum(errors) / len(errors)
    rmse = math.sqrt(sum(e ** 2 for e in errors) / len(errors))
    return mae, rmse

def rbo_score(list1, list2, p=0.9):
    """
    Computes the Rank-Biased Overlap (RBO) between two ranked lists.
    list1 and list2 should be lists of items (e.g., word names).
    The parameter p (0<p<1) controls the top-weightedness.
    """
    S, T = set(), set()
    rbo, weight = 0.0, 1 - p
    depth = max(len(list1), len(list2))
    for d in range(1, depth + 1):
        if d <= len(list1):
            S.add(list1[d - 1])
        if d <= len(list2):
            T.add(list2[d - 1])
        overlap = len(S.intersection(T))
        rbo += (overlap / d) * (p ** (d - 1))
    return (1 - p) * rbo

def main():
    words = load_words("test.json")
    ground_truth = get_ground_truth_ranking(words)
    predicted = get_predicted_ranking(words, noise_level=0.5)

    print("=== Ground Truth Ranking (by cost ascending) ===")
    for i, w in enumerate(ground_truth, start=1):
        print(f"{i}. {w['Nume']} (cost: {w['cost']})")
    
    print("\n=== Predicted Ranking (with noise) ===")
    for i, w in enumerate(predicted, start=1):
        print(f"{i}. {w['Nume']} (cost: {w['cost']}, score: {w['score']:.2f})")

    # Compute various ranking metrics.
    spearman_corr, spearman_p = compute_spearman(ground_truth, predicted)
    kendall_tau, kendall_p = compute_kendall(ground_truth, predicted)
    ndcg_val = compute_ndcg(ground_truth, predicted, k=10)
    best_word = ground_truth[0]["Nume"]
    mrr_val = compute_mrr(predicted, best_word)
    precision5 = compute_precision_at_k(ground_truth, predicted, k=5)
    mae, rmse = compute_mae_rmse(ground_truth, predicted)
    
    # For RBO, compare the ranked lists (by word names).
    gt_list = [w["Nume"] for w in ground_truth]
    pred_list = [w["Nume"] for w in predicted]
    rbo_val = rbo_score(gt_list, pred_list, p=0.9)
    
    print("\n=== Ranking Metrics ===")
    print(f"Spearman's Rank Correlation: {spearman_corr:.3f} (p-value: {spearman_p:.3f})")
    print(f"Kendall's Tau: {kendall_tau:.3f} (p-value: {kendall_p:.3f})")
    print(f"nDCG@10: {ndcg_val:.3f}")
    print(f"MRR: {mrr_val:.3f}")
    print(f"Precision@5: {precision5:.3f}")
    print(f"MAE of ranking positions: {mae:.3f}")
    print(f"RMSE of ranking positions: {rmse:.3f}")
    print(f"Rank-Biased Overlap (RBO): {rbo_val:.3f}")

if __name__ == "__main__":
    main()
