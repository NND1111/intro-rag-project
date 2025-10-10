def retrieve_chunks(query, embed_model, index, all_chunks, top_k=3):
    query_embedding = embed_model.encode([query])
    distances, indices = index.search(query_embedding, top_k)
    retrieved = [(all_chunks[i], distances[0][j]) for j, i in enumerate(indices[0])]
    return retrieved  # List of (chunk_text, similarity_score) tuples