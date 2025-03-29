import re
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

def get_local_llm_pipeline(model_name="gpt2-large"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    model.to("cpu")
    # Configure tokenizer for single-number responses
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    return pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        device=-1,  # CPU
        pad_token_id=tokenizer.eos_token_id
    )

def query_llm(pipeline_obj, word):
    prompt = (
        "Evaluate the power score (1-100) for the word: {word}\n"
        "Examples (DO NOT USE THESE):\n"
        "Feather → 1 | Sword → 35 | Nuclear → 95 | Entropy → 100\n"
        "Score for '{word}':"
    ).format(word=word)
    
    response = pipeline_obj(
        prompt,
        max_new_tokens=5,
        do_sample=True,
        temperature=0.8,
        top_p=0.9,
        num_return_sequences=1,
        return_full_text=False,
        clean_up_tokenization_spaces=True
    )[0]["generated_text"]
    return response.strip()

def extract_score(response):
    # Extract first valid integer from response
    match = re.search(r"\b(100|\d{1,2})\b", response.split("\n")[0])
    return int(match.group()) if match else None

def main():
    print("Loading GPT-2 Large (this may take 2-5 minutes and ~5GB RAM)...")
    llm_pipeline = get_local_llm_pipeline()
    
    while True:
        word = input("\nEnter a word (or 'q' to quit): ").strip().lower()
        if word == 'q':
            break
        if not word:
            print("Please enter a valid word")
            continue
            
        print(f"\nEvaluating '{word}'...")
        try:
            response = query_llm(llm_pipeline, word)
            print("Raw Model Output:", repr(response))
            
            score = extract_score(response) or "N/A"
            print(f"Power Score: {score if score != 'N/A' else 'Could not determine'}")

        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()