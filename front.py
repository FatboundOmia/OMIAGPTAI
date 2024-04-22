import streamlit as st



with st.sidebar:
    "El chat de mantenimiento de OMIA es una herramienta automatizada diseñada para optimizar y simplificar los procesos de mantenimiento en OMIA. Esta herramienta está diseñada para integrarse con los estándares ISO 14224 y OREDA, proporcionando a los operadores, técnicos y profesionales de mantenimiento una solución integral para gestionar de manera eficiente y segura sus procesos."

st.title("👨‍💻OMIA GPT COPILOT")
st.caption('💬OMIA GPT COPILOT POWERED BY MAINTANCE🛠')

if "message" not in st.session_state:
    st.session_state["message"] = [{'role':'assistant', "content":"¿Como te puedo ayudar hoy?"}]

if prompt := st.chat_input():
    
    st.session_state.message.append({"role":'user', "content":prompt})
    st.chat_message("user").write(prompt)
