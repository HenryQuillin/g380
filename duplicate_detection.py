import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def compute_similarity(texts):
    texts = [text if text is not None else '' for text in texts]# Filter out None values

    # find importance of words in each text
    vectorizer = TfidfVectorizer().fit_transform(texts)
    # this computes the cosine similarity between all pairs of texts
    # by finding the cosine of the angles between the vectors
    return cosine_similarity(vectorizer)


def detect_duplicates(articles):
    title_threshold = 0.3
    description_threshold = 0.6
    if not articles:
        return []

    titles = [str(article.get('title', '')) for article in articles]
    descriptions = [str(article.get('description', '')) for article in articles]

    title_sim_matrix = compute_similarity(titles)
 #    print(title_sim_matrix)
 #    [[1.         0.07953175 0.04423622 ... 0.         0.02389394 0.        ]
 # [0.07953175 1.         0.04964045 ... 0.         0.026813   0.        ]
 # [0.04423622 0.04964045 1.         ... 0.         0.         0.        ]
 # ...
 # [0.         0.         0.         ... 1.         0.23589887 0.03771018]
 # [0.02389394 0.026813   0.         ... 0.23589887 1.         0.03311483]
 # [0.         0.         0.         ... 0.03771018 0.03311483 1.        ]]

    desc_sim_matrix = compute_similarity(descriptions)

    duplicates = {}
    for i in range(len(articles)):
        if i not in duplicates:
            # Check for similar titles or similar descriptions
            title_similar_indices = set(np.where(title_sim_matrix[i] > title_threshold)[0])
            desc_similar_indices = set(np.where(desc_sim_matrix[i] > description_threshold)[0])
            similar_indices = title_similar_indices.union(desc_similar_indices)

            if len(similar_indices) > 1:  # More than just itself
                duplicates[i] = list(similar_indices)

    grouped_articles = []
    processed_indices = set() # keeps track of which articles have been processed

    for i, article in enumerate(articles):
        if i not in processed_indices:
            if i in duplicates:
                primary_article = article.copy()
                primary_article['duplicates'] = []
                for j in duplicates[i]:
                    if j != i:
                        duplicate_info = {
                            'title': articles[j].get('title', ''),
                            'description': articles[j].get('description', ''),
                            'url': articles[j].get('url', ''),
                            'publishedAt': articles[j].get('publishedAt', ''),
                            'source': articles[j].get('source', {}),
                        }
                        primary_article['duplicates'].append(duplicate_info)
                grouped_articles.append(primary_article)
                processed_indices.update(duplicates[i]) #ensure we dont process this articel again
            else:
                grouped_articles.append(article)
            processed_indices.add(i)

    return grouped_articles