# Full RAG test
from retrieval import *
from augmentation import *


def generate_response(generate_func, question, context, max_length):
    if not context:
        return generate_func(question=question, context="", temperature = 0.5, do_sample = True, num_return_sequences = 1, top_k=1 ,doc_stride=256,  handle_impossible_answer=True)
    return generate_func(question=question, context=context, temperature = 0.5, do_sample = True, num_return_sequences = 1, top_k=1, doc_stride=256,handle_impossible_answer=True )

def rag_pipeline(generate_func, query, embed_model, index, all_chunks, max_length=100):
    retrieved = retrieve_chunks(query, embed_model, index, all_chunks)
    context = "\n".join([chunk[0] for chunk in retrieved])
    return generate_response(generate_func, question=query, context=context, max_length=150)



# sample_query = "Biden was born in" # depends on your data
# retrieved = retrieve_chunks(sample_query, embed_model, index, all_chunks)  
# aug_prompt = augment_prompt(sample_query, retrieved)
# print(aug_prompt) 

# # aug_prompt = augment_prompt(sample_query, retrieved)


# # Plain baseline (no context)
# plain_prompt = f"Question: {sample_query}\nAnswer:"
# plain_answer = generate_response(plain_prompt, max_length=150)
# plain_answer[0]["generated_text"]  # Likely more hallucinated