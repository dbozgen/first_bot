import os
import openai
import streamlit as st 
from openai import OpenAIError
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="AI Learning Chatbot", page_icon="🤖")

st.title("AI Learning Chatbot 🤖")
st.write ("Ask your questions about learning new skills!")

if "convo_history" not in st.session_state:
    st.session_state.convo_history =[{"role":"system","content":"You are a helpful and knowledgable assistant." }]

user_input = st.text_input("You:", placeholder="Type your question here...")

def get_response(convo_history):
    try:
        response = openai.chat.completions.create (
            model="gpt-3.5-turbo",
            messages= convo_history
        )
        return response.choices[0].message.content
    except OpenAIError as e:
        st.error(f"Error, {e}. Stay tight, we are working on it")
        return None 

if user_input:
    st.session_state.convo_history.append({"role":"user", "content": user_input})
    
    bot_response = get_response(st.session_state.convo_history)
    
    if bot_response:
        st.write (f"**Bot:** {bot_response}")
    st.session_state.convo_history.append({"role":"assistant", "content":bot_response})
# st.text_input("You:", placeholder="Type your question here...", value="", key="input" )

st.write("### Chat History")

for chat in st.session_state.convo_history:
    if chat["role"] =="user":
        st.write(f"**You:** {chat['content']}")
    elif chat ["role"] == "assistant":
        st.write(f"**Bot:** {chat['content']}")