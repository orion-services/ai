"""
This script provides functionality to split a text file into chunks and store
them in a ChromaDB collection.

Author: Rodrigo Prestes Machado
"""
import os
import chromadb
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer


def splits_chunks(chunk_text, chunk_size=120):
    """
    Splits a text in chunks of chunk_size text.

    text: text to be split
    chunk_size: size of each chunk
    """
    words = chunk_text.split()
    chunks = [' '.join(words[i:i + chunk_size])
              for i in range(0, len(words), chunk_size)]
    return chunks


# Directory containing text files
TEXT_FILES = "text_files"

# Array to store the text files
texts = []

# Lists the files in the directory
files = os.listdir(TEXT_FILES)

# Reads the content of each file and adds it to the list of texts
for file in files:
    file_path = os.path.join(TEXT_FILES, file)
    with open(file_path, "r", encoding="utf-8") as f:
        texts.append(f.read())

# join all texts in a single string
ALL_TEXTS = " ".join(texts)

# Save the text in a file
with open("all_texts.txt", "w", encoding="utf-8") as f:
    f.write(ALL_TEXTS)

# Splitting ALL_TEXTS string into chunks
all_chunks = []
for text in texts:
    chunks = splits_chunks(text)
    all_chunks.extend(chunks)

# Chroma Sentence Transformers
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Initialize ChromaDB client
client = chromadb.PersistentClient(path="./database")

# Check if the collection already exists
existing_collections = client.list_collections()
collection_names = [col.name for col in existing_collections]
if "ai_collection" in collection_names:
    collection = client.get_collection("ai_collection")
    print("Collection 'ai_collection' already exists.")
else:
    collection = client.create_collection("ai_collection")
    print("Collection 'ai_collection' created.")

# Generate embeddings using the model
embeddings = model.encode(all_chunks)

# Adicionando os chunks ao ChromaDB
# Add chunks to the collection
for i, chunk in enumerate(all_chunks):
    collection.add(
        ids=[f"chunk_{i}"],
        # Add specific embedding
        #embeddings=[embeddings[i].tolist()],
        # Add metadata
        # metadatas=None,
        documents=[chunk]
    )
