def transform_based_pos_tagging(sentence):
    tagged_sentence = []

    for word in sentence.split():
        tagged_word = apply_rules(word)
        tagged_sentence.append((word, tagged_word))

    return tagged_sentence

def apply_rules(word):
    # Define transformation rules
    if word.lower() in ['is', 'am', 'are', 'was', 'were']:
        return 'VB'  # Verb (to be)
    elif word.lower() in ['the', 'a', 'an']:
        return 'DT'  # Determiner
    elif word.lower() in ['this', 'that', 'these', 'those']:
        return 'DT'  # Demonstrative determiner
    elif word.lower() in ['I', 'you', 'he', 'she', 'it', 'we', 'they']:
        return 'PRP'  # Personal pronoun
    elif word.endswith('ed'):
        return 'VBD'  # Past tense verb
    elif word.endswith('ing'):
        return 'VBG'  # Gerund/present participle
    elif word.endswith('s'):
        return 'NNS'  # Plural noun
    elif word.endswith('\'s'):
        return 'POS'  # Possessive ending
    else:
        return 'NN'  # Default to noun

# Example usage
sentence = "This is a simple example sentence for transformation-based POS tagging."
result = transform_based_pos_tagging(sentence)

print(result)
