import numpy as np
from numpy.linalg import norm

def load_embeddings(filepath):
    """
    Load pretrained word embeddings (e.g., GloVe) from a local file.
    Each line should contain a word followed by its vector components.
    """
    embeddings = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            values = line.split()
            word = values[0]
            vector = np.asarray(values[1:], dtype='float32')
            embeddings[word] = vector
    return embeddings

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (norm(vec1) * norm(vec2))

# You might start with these seed words, but ideally you'd expand this list
# based on your application or train a regression model on labeled data.
strong_seeds = ['excavator', 'titanium', 'fortress', 'steel']
weak_seeds   = ['paper', 'feather', 'cotton', 'fluff']

def evaluate_word_strength(word, embeddings):
    """
    Evaluates the 'strength' of a word based on its cosine similarity with a set of seed words.
    The strength score is computed as the difference between the average similarity
    to strong seeds and the average similarity to weak seeds.
    """
    if word not in embeddings:
        print(f"Word '{word}' not found in embeddings. Cannot evaluate.")
        return None

    word_vec = embeddings[word]
    
    # Calculate average cosine similarity with strong seeds.
    strong_sims = [cosine_similarity(word_vec, embeddings[s]) 
                   for s in strong_seeds if s in embeddings]
    avg_strong = np.mean(strong_sims) if strong_sims else 0

    # Calculate average cosine similarity with weak seeds.
    weak_sims = [cosine_similarity(word_vec, embeddings[w]) 
                 for w in weak_seeds if w in embeddings]
    avg_weak = np.mean(weak_sims) if weak_sims else 0

    # A higher result indicates the word is closer to "strong" concepts.
    strength_score = avg_strong - avg_weak
    return strength_score

if __name__ == "__main__":
    # Load embeddings from a local file (download and store locally first)
    embeddings = load_embeddings("glove.6B.50d.txt")  # for example, use GloVe 50-dimensional embeddings
    
    new_word = input("Enter a word to evaluate its 'strength': ").strip().lower()
    score = evaluate_word_strength(new_word, embeddings)
    if score is not None:
        print(f"The evaluated strength score for '{new_word}' is: {score:.3f}")
        if score > 0:
            print(f"'{new_word}' is considered relatively strong.")
        else:
            print(f"'{new_word}' is considered relatively weak.")
