from chromadb import PersistentClient

# Connect to the ChromaDB folder
client = PersistentClient(path="chroma_db")

# Get the existing collection
collection = client.get_collection("langchain")

# # Peek at a few docs
# print(collection.peek())

# This will return ids automatically along with requested metadatas
all_docs = collection.get(include=["metadatas"])

print(all_docs.keys())  # you'll see: dict_keys(['ids', 'metadatas', ...])

ids_to_delete = [
    doc_id for doc_id, meta in zip(all_docs["ids"], all_docs["metadatas"])
    if meta.get("source") == "data/movies_updated"
]

print(f"Found {len(ids_to_delete)} docs to delete")

# Delete them
if ids_to_delete:
    collection.delete(ids=ids_to_delete)
    print(f"Deleted {len(ids_to_delete)} docs")
else:
    print("No matching docs found.")