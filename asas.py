import spacy
import numpy as np
import math

# Load the medium-sized English model
nlp = spacy.load("en_core_web_md")

# Define a set of seed words representing "power"
seed_words = ["power", "strength", "force", "mighty", "dominant"]

def compute_power_score(word, seeds=seed_words):
    # Get the token for the input word (assuming it's a single token)
    token = nlp(word)[0]
    
    # Compute similarity scores with each seed word
    scores = []
    for seed in seeds:
        seed_token = nlp(seed)[0]
        similarity = token.similarity(seed_token)
        scores.append(similarity)
    
    # Average the similarities
    avg_similarity = np.mean(scores)
    
    # Use a sigmoid function to better distribute the score across 1-100.
    # Adjusting parameters:
    # a controls the steepness of the sigmoid curve,
    # b is the midpoint (similarity value that maps to roughly half the score).
    a = 20    # Steepness; increase for a sharper transition.
    b = 0.2   # Midpoint; adjust based on typical average similarities.
    
    # Compute the sigmoid output in the range [0, 1]
    sigmoid = 1 / (1 + math.exp(-a * (avg_similarity - b)))
    
    # Scale the sigmoid output to [1, 100]
    score = int(1 + sigmoid * 99)
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
