import streamlit as st
import subprocess
from main import pregunta
from langchain_google_genai import GoogleGenerativeAIEmbeddings, GoogleGenerativeAI

subprocess.run(["python", "main.py"])



st.set_page_config(
    page_title='OMIA GPT AI', 
    layout='wide',
    page_icon='images\OMIA-LOGO.ico'
    
)



def clear_chat():
    st.session_state["message"] = [{'role':'assistant', "content":"¿Como te puedo ayudar hoy?"}]



with st.sidebar:
    "El chat de mantenimiento de OMIA es una herramienta automatizada diseñada para optimizar y simplificar los procesos de mantenimiento en OMIA. Esta herramienta está diseñada para integrarse con los estándares ISO 14224 y OREDA, proporcionando a los operadores, técnicos y profesionales de mantenimiento una solución integral para gestionar de manera eficiente y segura sus procesos."

st.sidebar.button('Clear Chat History', on_click=clear_chat)
st.title("👨‍💻OMIA GPT COPILOT")
st.caption('💬OMIA GPT COPILOT POWERED BY MAINTANCE🛠')

if "message" not in st.session_state.keys():
    st.session_state["message"] = [{'role':'assistant', "content":"¿Como te puedo ayudar hoy?"}]

for msg in st.session_state.message:
    if msg['role'] == "assistant":
        with st.chat_message(msg['role'], avatar='images\OMIA-LOGO.ico'):
            st.write(msg["content"])
    else:
        with st.chat_message(msg['role']):
            st.write(msg["content"])
    
        

if prompt := st.chat_input():
    
    st.session_state.message.append({"role":'user', "content":prompt})
    st.chat_message("user").write(prompt)
    response = pregunta(prompt)
    
    st.session_state.message.append({'role':'assistant', 'content':response})
    st.chat_message("assistant", avatar='images\OMIA-LOGO.ico').write(response)
    
