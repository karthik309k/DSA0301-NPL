import spacy

def extract_noun_phrases(sentence):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)

    noun_phrases = []
    for chunk in doc.noun_chunks:
        noun_phrases.append((chunk.text, get_noun_phrase_meaning(chunk)))

    return noun_phrases

def get_noun_phrase_meaning(noun_chunk):
    # In a real application, you might use a knowledge base or external API to get meanings.
    # For simplicity, we'll use a basic example here.
    meanings = {
        "cat": "a small domesticated carnivorous mammal",
        "dog": "a domesticated carnivorous mammal",
        "bird": "a warm-blooded egg-laying vertebrate",
        # Add more meanings as needed
    }

    # Look up the meaning based on the noun chunk's text
    return meanings.get(noun_chunk.text.lower(), "Meaning not found")

# Example usage
sentence = "The cat and the dog are playing in the garden."
noun_phrases = extract_noun_phrases(sentence)

print("Noun Phrases and Meanings:")
for noun_phrase, meaning in noun_phrases:
    print(f"{noun_phrase}: {meaning}")
