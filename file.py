    import spacy
    import numpy as np

    # Load the medium-sized English model
    nlp = spacy.load("en_core_web_md")

    # Define a set of seed words representing "power"
    seed_words = ["power", "strength", "force", "mighty", "dominant"]

    def compute_power_score(word, seeds=seed_words):
        # Process the target word (assuming it is a single token)
        token = nlp(word)[0]
        
        # Compute similarity scores with each seed word
        similarities = []
        for seed in seeds:
            seed_token = nlp(seed)[0]
            sim = token.similarity(seed_token)
            similarities.append(sim)
        
        # Calculate both average and maximum similarity scores.
        avg_sim = np.mean(similarities)
        max_sim = max(similarities)
        
        # Combine the scores: weight maximum similarity more heavily.
        # You can adjust the weights (here 30% average and 70% maximum) if needed.
        combined_sim = 0.3 * avg_sim + 0.7 * max_sim

        # Map the combined similarity to a score between 1 and 100.
        # Assume typical combined similarities range between 0.2 and 0.8; adjust as needed.
        lower_bound = 0.2
        upper_bound = 0.8
        normalized = (combined_sim - lower_bound) / (upper_bound - lower_bound)
        normalized = max(0, min(normalized, 1))  # Clamp between 0 and 1
        score = int(normalized * 99 + 1)  # Scale to 1-100
        
        return score

    def main():
        word = input("Enter a word: ").strip()
        if not word:
            print("No word provided!")
            return
        
        score = compute_power_score(word)
        print(f"\nPower Score for '{word}': {score}")

    if __name__ == "__main__":
        main()
