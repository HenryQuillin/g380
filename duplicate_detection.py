import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def detect_duplicates(articles, similarity_threshold=0.5):
    # Extract titles and descriptions
    texts = [f"{article['title']} {article['description']}" for article in articles]

    # Create TF-IDF vectors
    vectorizer = TfidfVectorizer().fit_transform(texts)

    # Compute cosine similarity
    cosine_sim = cosine_similarity(vectorizer)

    # Find duplicates
    duplicates = {}
    for i in range(len(articles)):
        if i not in duplicates:
            similar_indices = np.where(cosine_sim[i] > similarity_threshold)[0]
            if len(similar_indices) > 1:  # More than just itself
                duplicates[i] = similar_indices.tolist()

    # Group duplicates
    grouped_articles = []
    processed_indices = set()

    for i, article in enumerate(articles):
        if i not in processed_indices:
            if i in duplicates:
                primary_article = article.copy()
                primary_article['duplicates'] = [articles[j] for j in duplicates[i] if j != i]
                grouped_articles.append(primary_article)
                processed_indices.update(duplicates[i])
            else:
                grouped_articles.append(article)
            processed_indices.add(i)

    return grouped_articles