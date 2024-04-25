import streamlit as st
import subprocess
from main import pregunta
from langchain_google_genai import GoogleGenerativeAIEmbeddings, GoogleGenerativeAI
import base64
from PIL import Image

subprocess.run(["python", "main.py"])

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()



def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: contain;
    background-position: center;
    background-repeat: no-repeat;
    
    
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)




st.set_page_config(
    page_title='OMIA GPT AI', 
    layout='wide',
    page_icon='images\OMIA-LOGO.ico'
    
)


def clear_chat():
    st.session_state["message"] = [{'role':'assistant', "content":"¿Como te puedo ayudar hoy?"}]


with st.sidebar:
    """El Chat de Mantenimiento de OMIA representa una innovadora herramienta automatizada diseñada para optimizar y simplificar los procesos de mantenimiento en OMIA. Esta solución está meticulosamente diseñada para integrarse con los estándares de calidad más exigentes, 
    incluyendo las Buenas Prácticas de Ramesh Gulati, el análisis de datos de OMIA (ODA), ISO 14224, Buenas practicas de las SMRP, proporcionando así a los operadores, técnicos y profesionales de mantenimiento una solución integral para gestionar de manera eficiente y segura 
    sus actividades de mantenimiento. Con esta herramienta, 
    se garantiza una gestión proactiva y eficaz de los procesos, asegurando un funcionamiento óptimo y una mayor confiabilidad de los activos de OMIA
    """

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




    

