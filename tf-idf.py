from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample documents
documents = [
    "The quick brown fox jumps over the lazy dog",
    "A brown dog barks loudly",
    "The lazy cat sleeps on the windowsill",
    "A fox and a dog are friends",
]

# Query
query = "brown dog"

def retrieve_documents(documents, query):
    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Compute TF-IDF scores for documents and the query
    tfidf_matrix = vectorizer.fit_transform([query] + documents)

    # Compute cosine similarities between the query and documents
    cosine_similarities = linear_kernel(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    # Rank documents based on cosine similarities
    ranked_documents = [(doc, score) for doc, score in zip(documents, cosine_similarities)]

    # Sort documents by score in descending order
    ranked_documents.sort(key=lambda x: x[1], reverse=True)

    return ranked_documents

# Retrieve and print ranked documents
ranked_documents = retrieve_documents(documents, query)

print(f"Query: {query}\n")
print("Ranked Documents:")
for i, (document, score) in enumerate(ranked_documents, 1):
    print(f"{i}. Document: {document}\n   Score: {score}\n")
