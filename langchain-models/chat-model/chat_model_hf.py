from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of Bangladesh? and how many divisions are there?")


print(result.content)