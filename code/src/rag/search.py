import chromadb

# Open a ChromaDB client
client = chromadb.PersistentClient(path="./database")

# Verify if the collection already exists
COLLECTION_NAME = "ai_collection"
existing_collections = client.list_collections()
collection_names = [col.name for col in existing_collections]

if COLLECTION_NAME in collection_names:
    collection = client.get_collection(COLLECTION_NAME)
    print(f"Collection '{COLLECTION_NAME}' loaded.")
else:
    raise ValueError(f"Collection '{COLLECTION_NAME}' not found.")


def search_chunks(prompt, chunks_collection, top_n=2):
    """
          Searches for chunks in ChromaDB

          prompt: query to be searched
          chuncks_collection: collection of chunks
          top_n: number of results to be returned
    """
    results = chunks_collection.query(
        query_texts=[prompt],
        n_results=top_n,
    )
    return results


# Example of searching for chunks
PROMPT = "configurar o vscode para usar com o python"
resulted_chunks = search_chunks(PROMPT, collection, top_n=2)

print("Prompt ", PROMPT)
print(resulted_chunks)
for idx, doc in enumerate(resulted_chunks['documents'][0]):
    print(f"Result {idx + 1}:\n{doc}\n")
