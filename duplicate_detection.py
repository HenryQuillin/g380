import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def compute_similarity(texts):
    #filter out none values
    texts = [text if text is not None else '' for text in texts]
    vectorizer = TfidfVectorizer().fit_transform(texts)
    return cosine_similarity(vectorizer)


def detect_duplicates(articles):
    similarity_threshold = 0.5
    if not articles:
        return []

    titles = [article.get('title', '') for article in articles]
    descriptions = [article.get('description', '') for article in articles]

    # Combine
    combined_texts = [f"{title} {desc}" for title, desc in zip(titles, descriptions)]

    sim_matrix = compute_similarity(combined_texts)

    duplicates = {}
    for i in range(len(articles)):
        if i not in duplicates:
            similar_indices = np.where(sim_matrix[i] > similarity_threshold)[0]
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