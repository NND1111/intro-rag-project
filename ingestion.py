import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
import pickle  # For saving chunks if needed

# Path to your data folder
data_dir = "data"  # Assumes /data in your repo root

# List to hold all chunks
all_chunks = []

# Loop over files 1.txt to 15.txt (skips missing ones)
for i in range(1, 11):  # 1 to 15
    file_path = os.path.join(data_dir, f"{i}.txt")
    if os.path.exists(file_path):
        print(f"Loading {file_path}...")
        loader = TextLoader(file_path, encoding="utf-8")  # Handles standard text
        docs = loader.load()
        text = " ".join([doc.page_content for doc in docs])  # Just the text

        # Clean: Remove extra whitespace, newlines (basic)
        text = ' '.join(text.split())  # Collapses multiples
        text = text.replace('\n', ' ')  # Flatten newlines if any

        # Chunk this file's text
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,  # ~500 chars/tokens
            chunk_overlap=50,  # Overlap for context continuity
            metadata={"source": f"{i}.txt"}
        )
        file_chunks = splitter.split_text(text)
        all_chunks.extend(file_chunks)  # Add to total pool
        print(f"Added {len(file_chunks)} chunks from {i}.txt")
    else:
        print(f"Skipping {file_path} (not found)")

# Final count
print(f"Total chunks created: {len(all_chunks)}")

# Optional: Save for later (e.g., Day 2 embedding)
with open("chunks.pkl", "wb") as f:
    pickle.dump(all_chunks, f)
print("Chunks saved to chunks.pkl")