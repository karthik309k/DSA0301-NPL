import nltk
from nltk import pos_tag
from nltk import RegexpParser
from nltk import word_tokenize

def recognize_dialog_acts(sentence):
    # Tokenize and part-of-speech tagging
    tokens = word_tokenize(sentence)
    pos_tags = pos_tag(tokens)

    # Define a simple grammar for dialog act recognition
    grammar = r"""
        DA: {<VB.*><DT|PRP.*>?<JJ.*>*<NN.*>+}  # Dialog Act: Verb + (Determiner/Personal Pronoun) + Adjectives + Nouns
    """
    parser = RegexpParser(grammar)

    # Apply the parser to the part-of-speech tagged sentence
    tree = parser.parse(pos_tags)

    # Extract dialog acts based on the grammar
    dialog_acts = [subtree.leaves() for subtree in tree.subtrees() if subtree.label() == 'DA']
    return dialog_acts

# Example usage
dialog = "Can you please pass the salt?"
dialog_acts = recognize_dialog_acts(dialog)

print(f"Dialog: {dialog}")
print("Dialog Acts:")
for dialog_act in dialog_acts:
    print(dialog_act)
