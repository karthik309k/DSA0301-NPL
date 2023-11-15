import nltk

def generate_parse_tree(sentence, grammar):
    parser = nltk.ChartParser(grammar)
    tokens = nltk.word_tokenize(sentence)

    try:
        for tree in parser.parse(tokens):
            tree.pretty_print()
            return tree
    except ValueError:
        print("No parse tree found for the given sentence.")

# Example usage
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N | NP PP
    VP -> V NP | VP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog' | 'bird'
    V -> 'chased' | 'caught'
    P -> 'with' | 'in'
""")

sentence = "the cat chased the bird with the dog"
generate_parse_tree(sentence, grammar)
