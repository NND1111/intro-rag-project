# Full RAG test
from retrieval import *
from augmentation import *


def generate_response(generate_func, prompt, max_length):
    return generate_func(prompt, max_length=max_length, temperature = 0.2, do_sample = False, num_return_sequences = 1 )

def rag_pipeline(generate_func, query, embed_model, index, all_chunks, max_length=100):
    retrieved = retrieve_chunks(query, embed_model, index, all_chunks)
    aug_prompt = augment_prompt(query, retrieved)
    return generate_response(generate_func, aug_prompt, max_length=150)



# sample_query = "Biden was born in" # depends on your data
# retrieved = retrieve_chunks(sample_query, embed_model, index, all_chunks)  
# aug_prompt = augment_prompt(sample_query, retrieved)
# print(aug_prompt) 

# # aug_prompt = augment_prompt(sample_query, retrieved)


# # Plain baseline (no context)
# plain_prompt = f"Question: {sample_query}\nAnswer:"
# plain_answer = generate_response(plain_prompt, max_length=150)
# plain_answer[0]["generated_text"]  # Likely more hallucinated