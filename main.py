import langchain_groq
import getpass
import os
from langchain_core.prompts import PromptTemplate
import streamlit as st
from resorse import api_key

os.environ["USER_AGENT"] = "summarizer/1.0"
os.environ["GROQ_API_KEY"] = api_key

from langchain_community.document_loaders import WebBaseLoader
from langchain.chat_models import init_chat_model

model = init_chat_model("llama3-8b-8192", model_provider="groq")

prompt = PromptTemplate.from_template(
    '''   
   #  scrap data from website: {page_data}
   #  summarize the website in max 50 to 100 words
    '''
)

extract = prompt | model

# Streamlit UI
st.title("Website Summarizer")
url = st.text_input("Enter website URL", "https://www.example.com/")

if st.button("Summarize"):
    try:
        loader = WebBaseLoader(url)
        page_data = loader.load().pop().page_content
        res = extract.invoke(input={'page_data': page_data})
        st.subheader("Summary:")
        st.write(res.content)
    except Exception as e:
        st.error(f"Error: {e}")




    