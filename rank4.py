import json
import math
import numpy as np
import random

# Configurații pentru host și URL-uri
host = "http://172.18.4.158:8000"
post_url = f"{host}/submit-word"
get_url = f"{host}/get-word"
status_url = f"{host}/status"



def load_words(filename):
    """
    Loads words from the JSON file and returns a list of dictionaries.
    Each dictionary should have keys like 'Nume', 'cost', and 'power'.
    """
    with open(filename, "r") as f:
        data = json.load(f)
    # Convert dictionary values into a list.
    words = [value for key, value in data.items()]
    return words

def find_word(word, words):
    """
    Searches for a word in the given list (case-insensitive) and returns
    the corresponding dictionary if found, otherwise returns None.
    """
    for w in words:
        if w["Nume"].lower() == word.lower():
            return w
    return None

def find_closest_bigger(test_words, target_power):
    """
    Finds the single word in test_words with power strictly greater than target_power 
    that is closest to target_power. Returns None if no such word exists.
    """
    # Filter only words with power > target_power.
    candidates = [w for w in test_words if w["power"] > target_power]
    if not candidates:
        return None
    # Find the candidate with the smallest difference.
    best = min(candidates, key=lambda w: w["power"] - target_power)
    return best

def main():
    # Load words from the database and test files.
    database_words = load_words("database.json")
    test_words = load_words("test.json")
    
    input_word = input("Enter a word: ").strip()
    if not input_word:
        print("No word provided!")
        return

    found_word = find_word(input_word, database_words)
    if found_word is None:
        print("Supermassive Black Hole")
        return

    target_power = found_word["power"]
    print(f"Found '{input_word}' in the database with power: {target_power}")

    # If the target power is 100, reply with "Entropy" directly.
    if target_power == 100:
        print("\nEntropy")
        return

    # Find in test.json the word with power strictly greater than target_power
    # and which is the closest to target_power.
    match = find_closest_bigger(test_words, target_power)
    if match:
        print(f"\nClosest word in test.json with power greater than {target_power}:")
        print(f"- {match['Nume']} (power: {match['power']})")
    else:
        print("\nNo matching word found in test.json with a power greater than the target.")

if __name__ == "__main__":
    main()
