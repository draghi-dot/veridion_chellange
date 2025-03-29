import json
import random
import numpy as np
from sklearn.neighbors import NearestNeighbors

def load_words(filename):
    """
    Loads words from the JSON file and returns a list of dictionaries.
    Each dictionary has 'text' and 'cost' keys.
    """
    with open(filename, "r") as f:
        data = json.load(f)
    # Convert dictionary values into a list.
    words = [value for key, value in data.items()]
    return words

def build_nn_model(words):
    """
    Builds a nearest neighbor model (using cost as the one-dimensional feature)
    for efficiently finding candidate words.
    """
    # Build a numpy array of costs (each cost is a feature vector of shape (1,))
    costs = np.array([[w["cost"]] for w in words])
    # Use NearestNeighbors; n_neighbors is set high so we can iterate over all neighbors
    nn = NearestNeighbors(n_neighbors=len(costs), algorithm='ball_tree', metric='euclidean')
    nn.fit(costs)
    return nn, costs

def find_candidate(system_word, words, nn, costs):
    """
    Given a system word, finds the candidate word with the smallest cost
    that is strictly greater than the system word's cost.
    Uses the NearestNeighbors model built on cost.
    Returns the candidate word dictionary or None if not found.
    """
    target = np.array([[system_word["cost"]]])
    distances, indices = nn.kneighbors(target)
    
    # Iterate through the neighbors in order of increasing distance.
    for idx in indices[0]:
        candidate = words[idx]
        if candidate["cost"] > system_word["cost"]:
            return candidate
    return None

def smart_fight(filename):
    # Load all words and build the nearest neighbor model.
    words = load_words(filename)
    nn, costs = build_nn_model(words)
    
    # Select a random system word from the list.
    system_word = random.choice(words)
    candidate = find_candidate(system_word, words, nn, costs)
    
    print("=== Word Fight ===")
    print(f"System word: {system_word['Nume']} (cost: {system_word['cost']})")
    if candidate is not None:
        print(f"Candidate word: {candidate['Nume']} (cost: {candidate['cost']})")
        print("=> Candidate beats the system word!")
    else:
        print("No candidate found to beat the system word (it may be the strongest word).")

if __name__ == "__main__":
    # Ensure that test.json is in the same directory as this script.
    smart_fight("test.json")
