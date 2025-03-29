import json
import random
from time import sleep

PENALTY = 30
NUM_ROUNDS = 5
# Predefined outcomes: False = loss, True = win.
# (This forces 2 wins and 3 losses.)
outcomes = [False, True, False, True, False]

def load_words(filename):
    """
    Loads the JSON file (with keys as strings) and returns a list of word dictionaries.
    Each dictionary has 'text' and 'cost' keys.
    """
    with open(filename, "r") as f:
        data = json.load(f)
    # Convert dictionary values into a list.
    words = [value for key, value in data.items()]
    return words

def select_system_word(words):
    """Randomly select a system word from the list."""
    return random.choice(words)

def select_candidate_word(system_word, words):
    """
    From the list, choose a word that can beat the system word—that is, with a cost greater than the system word.
    If no such candidate exists, return the system word (forcing a loss).
    """
    candidates = [w for w in words if w["cost"] > system_word["cost"]]
    if candidates:
        return random.choice(candidates)
    else:
        return system_word

def risky_strategy(filename):
    words = load_words(filename)
    total_cost = 0

    # Print table header
    header = f"{'Round':<6}{'System Word':<25}{'Word Used':<20}{'Cost':<10}{'Result':<10}{'Total This Round':<25}"
    print(header)
    print("-" * len(header))

    for i in range(NUM_ROUNDS):
        round_num = i + 1

        # Select a random system word
        system_word = select_system_word(words)
        # Find a candidate word that is supposed to beat the system word
        candidate = select_candidate_word(system_word, words)

        # Force outcome according to our predetermined pattern
        win = outcomes[i]
        if win:
            round_total = candidate["cost"]
            result_symbol = "✅"
            cost_detail = f"${candidate['cost']}"
        else:
            round_total = candidate["cost"] + PENALTY
            result_symbol = "❌"
            cost_detail = f"${candidate['cost']} + ${PENALTY} = ${round_total}"

        total_cost += round_total

        # (Optional) Sleep to simulate delay
        sleep(1)

        # Prepare system word display (showing text and its cost)
        system_word_display = f"{system_word['text']} ($ {system_word['cost']})"
        # Print round details: we show the system word and the candidate word used to beat it.
        print(f"{round_num:<6}{system_word_display:<25}{candidate['text']:<20}{'$'+str(candidate['cost']):<10}"
              f"{result_symbol:<10}{cost_detail:<25}")

    print("\n🧮 Total: $" + str(total_cost))

if __name__ == "__main__":
    # Ensure that test.json is in the same directory as this script.
    risky_strategy("test.json")
