import json
import math
import numpy as np
import random
import requests

# Configurations for host and URLs
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
    words = [value for key, value in data.items()]
    return words

def find_word(word, words):
    """
    Searches for a word (case-insensitive) and returns the corresponding dictionary if found.
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
    candidates = [w for w in test_words if w["power"] > target_power]
    if not candidates:
        return None
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
        result_word = "Supermassive Black Hole"
    else:
        target_power = found_word["power"]
        if target_power == 100:
            result_word = "Entropy"
        else:
            match = find_closest_bigger(test_words, target_power)
            if match:
                result_word = match["Nume"]
            else:
                result_word = "Supermassive Black Hole"
    
    # Print the result locally (just the word).
    print(result_word)
    
    # Send the result to /submit-word as a JSON payload.
    payload = {"result": result_word}
    try:
        response = requests.post(post_url, json=payload)
        if response.ok:
            print("Result submitted successfully:", response.text)
        else:
            print("Failed to submit result:", response.status_code, response.text)
    except Exception as e:
        print("Error submitting result:", e)

if __name__ == "__main__":
    main()