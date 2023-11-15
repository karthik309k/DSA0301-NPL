import nltk

def pcfg_parse(sentence, pcfg):
    parser = nltk.ChartParser(pcfg)

    try:
        for tree in parser.parse(sentence.split()):
            return tree
    except ValueError:
        print("No parse tree found for the given sentence.")
        return None

# Example usage
pcfg = nltk.PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.5] | NP PP [0.5]
    VP -> V NP [0.7] | VP PP [0.3]
    PP -> P NP [1.0]
    Det -> 'the' [0.7] | 'a' [0.3]
    N -> 'cat' [0.4] | 'dog' [0.4] | 'bird' [0.2]
    V -> 'chases' [0.6] | 'catches' [0.4]
    P -> 'with' [0.5] | 'in' [0.5]
""")

sentence = "the cat chases the bird with a dog"
result_tree = pcfg_parse(sentence, pcfg)

if result_tree:
    result_tree.pretty_print()
