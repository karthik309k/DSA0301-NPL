import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
sentence = "The quick brown foxes are jumping over the lazy dogs"
words = word_tokenize(sentence)
pos_tags = pos_tag(words)
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word, pos=get_wordnet_pos(tag)) for word, tag in pos_tags]
for word, pos_tag, lemma in zip(words, pos_tags, lemmatized_words):
    print(f"Word: {word}, POS Tag: {pos_tag[1]}, Lemma: {lemma}")
