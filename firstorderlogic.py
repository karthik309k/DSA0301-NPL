import nltk

# Sample FOPL statements
statement1 = "All humans are mortal."
statement2 = "Socrates is a human."

# Tokenize and parse FOPL statements
tokens1 = nltk.word_tokenize(statement1)
tokens2 = nltk.word_tokenize(statement2)

# Create an nltk Tree to represent FOPL expressions
tree1 = nltk.Tree("FOPL", [tokens1])
tree2 = nltk.Tree("FOPL", [tokens2])

# Define a simple FOPL inference
def is_mortal(entity):
    if entity == "Socrates":
        return True
    return False

# Check if Socrates is mortal based on FOPL statements
if "human" in tokens2:
    entity = tokens2[tokens2.index("is") + 1]
    if is_mortal(entity):
        print(f"{entity} is mortal.")
    else:
        print(f"{entity} is not mortal.")
else:
    print("No information about mortality.")

# You can extend this example to handle more complex FOPL statements and inferences.
