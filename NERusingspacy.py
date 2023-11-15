import spacy

def perform_ner(text):
    # Load the English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the text
    doc = nlp(text)

    # Extract named entities
    named_entities = [(ent.text, ent.label_) for ent in doc.ents]

    return named_entities

# Example usage
text = "Apple Inc. was founded by Steve Jobs in Cupertino. Google is headquartered in Mountain View, California."
ner_results = perform_ner(text)

# Print the results
for entity, label in ner_results:
    print(f"Entity: {entity}, Label: {label}")
