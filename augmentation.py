def augment_prompt(query, retrieved_chunks):
    context = "\n\n".join([chunk[0] for chunk in retrieved_chunks])  # Concat chunks
    prompt = f"""I know that: {context}
    With all the context above, I can answer that {query}"""
    return prompt

def augment_prompt_no_query(retrieved_chunks):
    context_parts = []
    for chunk_tuple in retrieved_chunks:
        chunk_dict = chunk_tuple[0]  # {'text':, 'source':}
        source = chunk_dict['source']
        text = chunk_dict['text']
        context_parts.append(f"[Source: {source}]\n{text}")
    
    context = "\n\n".join(context_parts)
    prompt = f"""Use the following context to answer the question factually. If the context doesn't cover it, just say "I don't have info on that."
Else, when referencing information from the context, include the [Source: x.txt] inline in your answer where it's used.
    
Context: {context}"""
    return prompt