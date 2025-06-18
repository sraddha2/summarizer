import langchain_groq
import getpass
import os
from langchain_core.prompts import PromptTemplate
import streamlit
from resorse import api_key

os.environ["GROQ_API_KEY"] = api_key
from langchain.chat_models import init_chat_model

model = init_chat_model("llama3-8b-8192", model_provider="groq")

# Define a function to get a response from the model
def get_response(prompt):
    response = model.invoke(prompt)
    return response.content

# Test the model
prompt = "Hello, who are you? few words"
response = get_response(prompt)
print(response)