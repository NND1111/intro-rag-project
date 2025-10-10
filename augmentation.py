def augment_prompt(query, retrieved_chunks):
    context = "\n\n".join([chunk[0] for chunk in retrieved_chunks])  # Concat chunks
    prompt = f"""Use the following context to answer the question factually. If the context doesn't cover it, say "I don't have info on that."
    I know that: {context}
    With all the context above, I can answer that {query}"""
    return prompt

