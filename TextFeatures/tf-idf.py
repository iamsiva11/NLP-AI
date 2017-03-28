from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(dataset['allTextFeaures']) 
# The Cosine Similarity between the first document/row with other documents of the set
cosine_arr = cosine_similarity(tfidf_matrix[i], tfidf_matrix)
