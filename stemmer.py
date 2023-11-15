import nltk
from nltk.stem import PorterStemmer

# Initialize the Porter Stemmer
stemmer = PorterStemmer()

# List of words to be stemmed
words = ["jumping", "jumps", "jumped", "running", "runner", "ran", "better", "best", "flies", "flies"]

# Perform stemming
stemmed_words = [stemmer.stem(word) for word in words]

# Print the original and stemmed words
for original, stemmed in zip(words, stemmed_words):
    print(f"{original} => {stemmed}")
