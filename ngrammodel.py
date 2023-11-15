import random
from collections import defaultdict

def generate_bigram_model(text):
    words = text.split()
    bigram_model = defaultdict(list)

    for current_word, next_word in zip(words, words[1:]):
        bigram_model[current_word].append(next_word)

    return bigram_model

def generate_text(bigram_model, seed_word, length=10):
    current_word = seed_word
    generated_text = [current_word]

    for _ in range(length - 1):
        next_words = bigram_model.get(current_word, [])
        if next_words:
            next_word = random.choice(next_words)
            generated_text.append(next_word)
            current_word = next_word
        else:
            break

    return ' '.join(generated_text)

# Example usage
input_text = "This is a sample text for the bigram model. It will generate text based on the bigrams."
bigram_model = generate_bigram_model(input_text)

seed_word = "sample"
generated_text = generate_text(bigram_model, seed_word, length=15)

print(generated_text)
