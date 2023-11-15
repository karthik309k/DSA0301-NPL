import nltk
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.tag import untag
from nltk.corpus import treebank

# Download the Treebank dataset for training
nltk.download('treebank')

# Train the model on the Treebank dataset
train_data = treebank.tagged_sents()[:3000]  # Use a portion of the Treebank dataset for training
fd = FreqDist(untag(train_data))  # Frequency distribution of POS tags for each word

def stochastic_pos_tagging(sentence):
    tokens = word_tokenize(sentence)
    tagged_sentence = []

    for token in tokens:
        # If the word is in the training data, assign the most frequent POS tag
        if token in fd:
            most_common_tag = fd[token].max()
            tagged_sentence.append((token, most_common_tag))
        else:
            # If the word is not in the training data, assign a default tag (e.g., 'NN' for a noun)
            tagged_sentence.append((token, 'NN'))

    return tagged_sentence

# Example usage
sentence = "This is a simple stochastic part-of-speech tagging algorithm using a basic probabilistic model."
result = stochastic_pos_tagging(sentence)

print(result)
