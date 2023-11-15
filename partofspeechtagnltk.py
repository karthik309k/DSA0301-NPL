import nltk
from nltk import word_tokenize
nltk.download('punkt')  # Download the Punkt tokenizer models if not already downloaded
nltk.download('averaged_perceptron_tagger')  # Download the POS tagger model if not already downloaded

def pos_tagging(text):
    tokens = word_tokenize(text)
    pos_tags = nltk.pos_tag(tokens)
    return pos_tags

# Example usage
text = "This is an example sentence for part-of-speech tagging using the NLTK library."
result = pos_tagging(text)

print(result)
