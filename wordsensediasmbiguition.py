from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def lesk_algorithm(sentence, target_word):
    # Tokenize the sentence and remove stopwords
    tokens = word_tokenize(sentence)
    stop_words = set(stopwords.words('english'))
    tokens = [token.lower() for token in tokens if token.isalnum() and token.lower() not in stop_words]

    # Get all possible synsets for the target word
    target_synsets = wordnet.synsets(target_word)

    # Choose the sense with the maximum overlap
    max_overlap = 0
    best_sense = None

    for sense in target_synsets:
        # Get the definition and example of the sense
        signature = set(word_tokenize(sense.definition()))
        signature.update(set(word_tokenize(' '.join(sense.examples()))))

        # Calculate the overlap with the context
        overlap = len(set(tokens).intersection(signature))

        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense

    return best_sense

# Example usage
sentence = "He went to the bank to deposit some money."
target_word = "bank"
sense = lesk_algorithm(sentence, target_word)

if sense:
    print(f"Target Word: {target_word}")
    print(f"Best Sense: {sense.name()}")
    print(f"Definition: {sense.definition()}")
else:
    print(f"No sense found for the target word: {target_word}")
