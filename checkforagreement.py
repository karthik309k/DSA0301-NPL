import nltk

def check_subject_verb_agreement(sentence, grammar):
    parser = nltk.ChartParser(grammar)
    tokens = nltk.word_tokenize(sentence)

    try:
        for tree in parser.parse(tokens):
            return check_agreement(tree)
    except ValueError:
        print("No parse tree found for the given sentence.")
        return False

def check_agreement(tree):
    for subtree in tree.subtrees():
        if subtree.label() == 'NP':
            # Check agreement between subject and verb
            subject = get_subject(subtree)
            verb = get_verb(subtree)

            if subject and verb and subject[1] != verb[1]:  # Check for number agreement
                print(f"Subject '{subject[0]}' and verb '{verb[0]}' do not agree in number.")
                return False

    print("Subject-verb agreement is correct.")
    return True

def get_subject(tree):
    for subtree in tree.subtrees():
        if subtree.label() == 'NP':
            for child in subtree:
                if child.label() == 'N':
                    return (child[0], child[1])  # Return (word, number)

def get_verb(tree):
    for subtree in tree.subtrees():
        if subtree.label() == 'VP':
            for child in subtree:
                if child.label() == 'V':
                    return (child[0], child[1])  # Return (word, number)

# Example usage
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N | NP PP
    VP -> V NP | VP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'cat' | 'cats' | 'dog' | 'dogs'
    V -> 'chases' | 'chase'
    P -> 'with' | 'in'
""")

sentence = "the cat chases the dogs with a dog"
check_subject_verb_agreement(sentence, grammar)
