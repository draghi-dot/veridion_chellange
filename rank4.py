import json
import math
import numpy as np
import random
import requests
import time

# Configurări pentru host și URL-uri
host = "http://172.18.4.158:8000"
post_url = f"{host}/submit-word"
get_url = f"{host}/get-word"
status_url = f"{host}/status"

# Setează PLAYER_ID-ul (modifică manual între "player1" sau "player2")
PLAYER_ID = "NNPScDuaYV"

def load_words(filename):
    """
    Încarcă cuvintele din fișierul JSON și returnează o listă de dicționare.
    Fiecare dicționar trebuie să aibă cheile 'Nume', 'cost' și 'power'.
    """
    with open(filename, "r") as f:
        data = json.load(f)
    words = [value for key, value in data.items()]
    return words

def find_word(word, words):
    """
    Caută un cuvânt (case-insensitive) și returnează dicționarul corespunzător dacă este găsit.
    """
    for w in words:
        if w["Nume"].lower() == word.lower():
            return w
    return None

def find_closest_bigger(test_words, target_power):
    """
    Găsește un singur cuvânt în test_words cu putere strict mai mare decât target_power
    și cel mai apropiat de target_power. Returnează None dacă nu există.
    """
    candidates = [w for w in test_words if w["power"] > target_power]
    if not candidates:
        return None
    best = min(candidates, key=lambda w: w["power"] - target_power)
    return best

def compute_result(input_word, database_words, test_words):
    """
    Folosește logica existentă:
      - Dacă cuvântul nu se găsește în database, rezultatul este "Supermassive Black Hole".
      - Dacă se găsește și puterea este 100, rezultatul este "Entropy".
      - Altfel, se caută în test.json cuvântul cu putere strict mai mare și cel mai apropiat.
    """
    found_word = find_word(input_word, database_words)
    if found_word is None:
        return "Supermassive Black Hole"
    target_power = found_word["power"]
    if target_power == 100:
        return "Entropy"
    match = find_closest_bigger(test_words, target_power)
    if match:
        return match["Nume"]
    else:
        return "Supermassive Black Hole"

def main():
    # Încarcă datele locale
    database_words = load_words("database.json")
    test_words = load_words("test.json")
    
    total_rounds = 5
    current_round = 0

    print(f"Turneu început. Jucător: {PLAYER_ID}. Se așteaptă startul rundelor...")

    # Loop-ul turneului: 5 runde
    while current_round < total_rounds:
        # Poll GET până când se primește {"round": 1, "word": "<cuvânt>"}.
        game_state = {}
        while True:
            try:
                resp = requests.get(get_url, params={"player_id": PLAYER_ID})
                game_state = resp.json()
            except Exception as e:
                print("Eroare GET:", e)
                time.sleep(0.5)
                continue

            # Dacă round e 1 și cuvântul nu este gol, înseamnă că runda a început.
            if game_state.get("round") == 1 and game_state.get("word", ""):
                break
            time.sleep(0.2)

        input_word = game_state["word"]
        print(f"Runda {current_round + 1} a început. Cuvânt primit: '{input_word}'")
        
        # Calculează rezultatul folosind logica existentă.
        result_word = compute_result(input_word, database_words, test_words)
        print(f"Rezultat calculat: '{result_word}'")
        
        # Timer de 5 secunde în care se așteaptă trimiterea POST.
        time.sleep(5)

        # Trimite rezultatul la /submit-word împreună cu PLAYER_ID.
        payload = {"player_id": PLAYER_ID, "result": result_word}
        try:
            post_resp = requests.post(post_url, json=payload)
            if post_resp.ok:
                print(f"Runda {current_round + 1}: Rezultat trimis cu succes.")
            else:
                print(f"Runda {current_round + 1}: Eroare la trimitere: {post_resp.status_code} {post_resp.text}")
        except Exception as e:
            print(f"Runda {current_round + 1}: Eroare la trimitere: {e}")

        # Așteaptă sfârșitul rundei: GET va returna {"round": 2}.
        while True:
            try:
                resp = requests.get(get_url, params={"player_id": PLAYER_ID})
                game_state = resp.json()
            except Exception as e:
                print("Eroare GET (final rundă):", e)
                time.sleep(0.5)
                continue

            if game_state.get("round") == 2:
                break
            time.sleep(0.2)
        
        print(f"Runda {current_round + 1} s-a încheiat.\n")
        current_round += 1

    print("Turneul s-a încheiat.")

if __name__ == "__main__":
    main()
