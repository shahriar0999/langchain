import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature = 1.2
)
query = input("Enter your query here: ")
response = llm.invoke(query)

print(response.content)