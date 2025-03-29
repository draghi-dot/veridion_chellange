import spacy
import numpy as np

# Load the medium-sized English model (ensure you have installed it via: python -m spacy download en_core_web_md)
nlp = spacy.load("en_core_web_md")

"""
Acestea sunt câteva exemple de evaluare a puterii (în JSON). Folosește aceste exemple ca referință pentru a evalua puterea unui cuvânt nou:

{
  "1": {"Nume": "Feather", "cost": 1, "power": 1},
  "3": {"Nume": "Pebble", "cost": 1, "power": 2},
  "4": {"Nume": "Leaf", "cost": 2, "power": 2},
  "5": {"Nume": "Paper", "cost": 2, "power": 3},
  "8": {"Nume": "Twig", "cost": 3, "power": 3},
  "2": {"Nume": "Coal", "cost": 1, "power": 4},
  "6": {"Nume": "Rock", "cost": 2, "power": 5},
  "13": {"Nume": "Rope", "cost": 5, "power": 6},
  "16": {"Nume": "Bacteria", "cost": 6, "power": 22},
  "29": {"Nume": "Stone", "cost": 11, "power": 7},
  "30": {"Nume": "Echo", "cost": 11, "power": 4},
  "7": {"Nume": "Water", "cost": 3, "power": 10},
  "9": {"Nume": "Sword", "cost": 4, "power": 35},
  "10": {"Nume": "Shield", "cost": 4, "power": 30},
  "11": {"Nume": "Gun", "cost": 5, "power": 40},
  "12": {"Nume": "Flame", "cost": 5, "power": 12},
  "15": {"Nume": "Cure", "cost": 6, "power": 15},
  "17": {"Nume": "Shadow", "cost": 7, "power": 20},
  "18": {"Nume": "Light", "cost": 7, "power": 20},
  "20": {"Nume": "Sound", "cost": 8, "power": 10},
  "25": {"Nume": "Vaccine", "cost": 9, "power": 15},
  "28": {"Nume": "Robots", "cost": 10, "power": 25},
  "33": {"Nume": "Wind", "cost": 13, "power": 12},
  "34": {"Nume": "Ice", "cost": 13, "power": 12},
  "44": {"Nume": "Whale", "cost": 17, "power": 15},
  "14": {"Nume": "Disease", "cost": 6, "power": 30},
  "19": {"Nume": "Virus", "cost": 7, "power": 30},
  "23": {"Nume": "Earthquake", "cost": 9, "power": 40},
  "24": {"Nume": "Storm", "cost": 9, "power": 40},
  "26": {"Nume": "Logic", "cost": 10, "power": 35},
  "31": {"Nume": "Thunder", "cost": 12, "power": 45},
  "32": {"Nume": "Karma", "cost": 12, "power": 45},
  "35": {"Nume": "Sandstorm", "cost": 13, "power": 40},
  "36": {"Nume": "Laser", "cost": 14, "power": 50},
  "37": {"Nume": "Magma", "cost": 14, "power": 50},
  "38": {"Nume": "Peace", "cost": 14, "power": 55},
  "39": {"Nume": "Explosion", "cost": 15, "power": 55},
  "40": {"Nume": "War", "cost": 15, "power": 60},
  "41": {"Nume": "Enlightenment", "cost": 15, "power": 65},
  "43": {"Nume": "Volcano", "cost": 16, "power": 60},
  "46": {"Nume": "Moon", "cost": 17, "power": 60},
  "48": {"Nume": "Tsunami", "cost": 18, "power": 65},
  "51": {"Nume": "Plague", "cost": 20, "power": 70},
  "52": {"Nume": "Rebirth", "cost": 20, "power": 70},
  "55": {"Nume": "Human Spirit", "cost": 23, "power": 75},
  "21": {"Nume": "Time", "cost": 8, "power": 80},
  "22": {"Nume": "Fate", "cost": 8, "power": 80},
  "27": {"Nume": "Gravity", "cost": 10, "power": 85},
  "42": {"Nume": "Nuclear Bomb", "cost": 16, "power": 90},
  "45": {"Nume": "Earth", "cost": 17, "power": 85},
  "47": {"Nume": "Star", "cost": 18, "power": 90},
  "49": {"Nume": "Supernova", "cost": 19, "power": 95},
  "50": {"Nume": "Antimatter", "cost": 19, "power": 95},
  "53": {"Nume": "Tectonic Shift", "cost": 21, "power": 90},
  "54": {"Nume": "Gamma-Ray Burst", "cost": 22, "power": 98},
  "56": {"Nume": "Apocalyptic Meteor", "cost": 24, "power": 97},
  "57": {"Nume": "Earth’s Core", "cost": 25, "power": 92},
  "58": {"Nume": "Neutron Star", "cost": 26, "power": 98},
  "59": {"Nume": "Supermassive Black Hole", "cost": 35, "power": 99},
  "60": {"Nume": "Entropy", "cost": 45, "power": 100}
}

Atunci când ți se oferă un cuvânt nou, evaluează-i scorul de "power" (pe o scală de la 1 la 100) ținând cont de exemplele de mai sus.
"""

# Seturi de cuvinte seed
concrete_seed_words = ["power", "strength", "force", "mighty", "dominant"]
abstract_seed_words = ["abstract", "concept", "idea", "theory", "philosophy"]

# Pre-calculează tokenii pentru fiecare set pentru eficiență
concrete_seed_tokens = [nlp(seed)[0] for seed in concrete_seed_words]
abstract_seed_tokens = [nlp(seed)[0] for seed in abstract_seed_words]

def compute_similarity(token, seed_tokens):
    """
    Calculează similaritatea combinată (30% medie, 70% maximă)
    între token și fiecare token din setul de seed-uri.
    """
    similarities = [token.similarity(seed) for seed in seed_tokens]
    avg_sim = np.mean(similarities)
    max_sim = max(similarities)
    combined_sim = 0.3 * avg_sim + 0.7 * max_sim
    return combined_sim

def compute_power_score(word):
    """
    Calculează scorul de putere pentru un cuvânt dat,
    evaluând similaritatea atât cu setul de seed-uri concrete, cât și
    cu cel de seed-uri abstracte și alegând scorul mai mare.
    """
    token = nlp(word)[0]
    
    # Calculează similaritatea pentru fiecare set de seed-uri
    sim_concrete = compute_similarity(token, concrete_seed_tokens)
    sim_abstract = compute_similarity(token, abstract_seed_tokens)
    
    # Se alege similaritatea maximă
    combined_sim = max(sim_concrete, sim_abstract)
    
    # Mapare pe scara 1-100:
    lower_bound = 0.2
    upper_bound = 0.8
    normalized = (combined_sim - lower_bound) / (upper_bound - lower_bound)
    normalized = max(0, min(normalized, 1))
    score = int(normalized * 99 + 1)
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
