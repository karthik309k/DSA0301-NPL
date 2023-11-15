from nltk.corpus import wordnet

def explore_word_meanings(word):
    # Get synsets for the given word
    synsets = wordnet.synsets(word)

    if not synsets:
        print(f"No synsets found for the word '{word}'.")
        return

    print(f"Synsets for the word '{word}':")
    for synset in synsets:
        print(f" - {synset.name()}: {synset.definition()}")

    # Explore hypernyms (more abstract terms)
    hypernyms = synsets[0].hypernyms()
    if hypernyms:
        print(f"\nHypernyms for the first synset:")
        for hypernym in hypernyms:
            print(f" - {hypernym.name()}: {hypernym.definition()}")

# Example usage
word_to_explore = "dog"
explore_word_meanings(word_to_explore)
