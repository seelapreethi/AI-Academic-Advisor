from vector_store import store_embedding, search_similar

store_embedding("I want to study machine learning", 1)

results = search_similar("AI learning")

print(results)