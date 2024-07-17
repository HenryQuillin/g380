import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def detect_duplicates(texts, similarity_threshold=0.7):
    # Create TF-IDF vectors
    vectorizer = TfidfVectorizer().fit_transform(texts)

    # Compute cosine similarity
    cosine_sim = cosine_similarity(vectorizer)

    # Find duplicates
    duplicates = {}
    for i in range(len(texts)):
        if i not in duplicates:
            similar_indices = np.where(cosine_sim[i] > similarity_threshold)[0]
            if len(similar_indices) > 1:  # More than just itself
                duplicates[i] = similar_indices.tolist()

    return duplicates


# Sample texts
sample_texts = [
    "The quick brown fox jumps over the lazy dog",
    "A fast auburn fox leaps above the sleepy canine",
    "Python is a popular programming language",
    "Java is a popular programming language",
    "Java is another widely used programming language",
    "The lazy dog is jumped over by the quick brown fox",
    "Programming in Python is fun and productive",
]

# Detect duplicates
result = detect_duplicates(sample_texts)

# Print results
print("Duplicate groups:")
for primary_index, duplicate_indices in result.items():
    print(f"\nGroup {primary_index + 1}:")
    print(f"Primary: {sample_texts[primary_index]}")
    print("Duplicates:")
    for idx in duplicate_indices:
        if idx != primary_index:
            print(f"- {sample_texts[idx]}")

print("\nAll texts with grouping:")
for i, text in enumerate(sample_texts):
    group = next((key for key, value in result.items() if i in value), None)
    print(f"{i + 1}. {'[Group ' + str(group + 1) + ']' if group is not None else '[Unique]'} {text}")