from langchain_groq.chat_models import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model='openai/gpt-oss-20b')

result = llm.invoke("What is the capital of Bangladesh?")

print(result.content)