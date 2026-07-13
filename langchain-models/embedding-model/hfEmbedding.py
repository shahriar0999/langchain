from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# text = "Dhaka is the capital of Bangladesh"

# vector = embedding.embed_query(text)

texts = [
    "Dhaka is the capital of Bangladesh",
    "Dhaka is the worst city in the world"
]

vector = embedding.embed_documents(texts)

print(vector)