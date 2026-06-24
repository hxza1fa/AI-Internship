import numpy as np

def most_similar_doc(documents: np.array, query: np.array) -> int:
    directions = []

    for doc in documents:
        v = (np.dot(doc, query)) / (np.linalg.norm(doc) * np.linalg.norm(query))
        theta = np.arccos(v)
        directions.append(theta)

    return np.argmin(directions)

def main():
    documents = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [1, 0, 0]
])

    query = np.array([2, 4, 6])
    print(f"Most similar document: {most_similar_doc(documents, query)}")

main()