import spacy

nlp = spacy.load("en_core_web_sm")

sent = "Swimming in the pool is my favorite activity."
doc = nlp(sent)

for token in doc:
    print(f"Token: {token.text}\nLemma: {token.lemma_}\nPOS: {token.pos_}\n")

prepos_phrases = []
for token in doc:
    if token.pos_ == "ADP":  # Check if it's a preposition
        prep_phrase = token.text
        for child in token.children:
            prep_phrase += " " + child.text
        prepos_phrases.append(prep_phrase)
print(f"Preposition Phrases: {prepos_phrases}")

ger_phrases = []
for token in doc:
    if token.pos_ == "VERB" and token.text.endswith("ing"):  # Check for gerund
        gerundive_phrase = token.text
        for child in token.children:
            gerundive_phrase += " " + child.text
        ger_phrases.append(gerundive_phrase)
print(f"Gerundive Phrases: {ger_phrases}")

inf_clause = []
for token in doc:
    if token.pos_ == "PART" and token.text == "to":
        infinitive_clause = token.text
        for child in token.rights:  # Use token.rights to find child tokens
            infinitive_clause += " " + child.text
        inf_clause.append(infinitive_clause)
print(f"Infinite Clauses: {inf_clause}")

rel_clause = []
for token in doc:
    if "nsubj" in token.dep_:
        for child in token.subtree:
            rel_clause.append(child.text)
print(f"Relative Clauses: {rel_clause}")
