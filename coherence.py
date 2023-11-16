import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def evaluate_coherence(text):
    nlp = spacy.load("en_core_web_sm")
    
    # Tokenize and process the text using spaCy
    doc = nlp(text)
    
    # Extract sentences from the processed text
    sentences = [sent.text for sent in doc.sents]
    
    # Compute sentence vectors using TF-IDF
    vectorizer = TfidfVectorizer()
    sentence_vectors = vectorizer.fit_transform(sentences)
    
    # Compute pairwise cosine similarity between sentence vectors
    similarity_matrix = cosine_similarity(sentence_vectors, sentence_vectors)
    
    # Calculate coherence score
    coherence_score = sum(similarity_matrix.sum(axis=1) - 1) / (len(sentences) * (len(sentences) - 1))
    
    return coherence_score

# Example usage
input_text = """
Natural language processing (NLP) is a field of artificial intelligence 
that focuses on the interaction between computers and humans using natural language. 
It involves the development of algorithms and models to enable computers to understand, 
interpret, and generate human-like text. NLP has applications in various domains, 
including machine translation, sentiment analysis, and information retrieval. 
Coherence in text is essential for effective communication and understanding. 
A coherent text flows smoothly, with logically connected ideas and clear transitions between sentences. 
Evaluating coherence can help improve the quality of natural language processing applications.
"""

coherence_score = evaluate_coherence(input_text)

print(f"Coherence Score: {coherence_score:.4f}")
