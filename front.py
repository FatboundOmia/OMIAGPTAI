import streamlit as st
import subprocess
from main import pregunta
from langchain_google_genai import GoogleGenerativeAIEmbeddings, GoogleGenerativeAI
import base64
from PIL import Image

subprocess.run(["python", "main.py"])

st.set_page_config(
    page_title='OMIA GPT AI', 
    layout='wide',
    page_icon='images\OMIA-LOGO.ico'
    
)

# st.markdown(
#     """
# <style>
# .css-nzvw1x {
#     background-color: #061E42 !important;
#     background-image: none !important;
# }
# .css-1aw8i8e {
#     background-image: none !important;
#     color: #FFFFFF !important
# }
# .css-ecnl2d {
#     background-color: #496C9F !important;
#     color: #496C9F !important
# }
# .css-15zws4i {
#     background-color: #496C9F !important;
#     color: #FFFFFF !important
# }
# </style>
# """,
#     unsafe_allow_html=True
# )


st.markdown(
    """
<style>
.sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: white;
}
</style>
""",
    unsafe_allow_html=True,
)



# def color_sidebar(color):
#     st.markdown(f'<style>.stSidebar .css-n3p1cb {{background-color: {color};}}</style>', unsafe_allow_html=True)

# codigo_color = "#337ab7"
# color_sidebar(codigo_color)


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


def clear_chat():
    st.session_state["message"] = [{'role':'assistant', "content":"🖐 Hola, yo soy agente de inteligencia artificial especialista en mantenimiento y confiabilidad. ¿En que te puedo ayudar?"}]

#tex_1 =     """OMIA, impulsando el desarrollo y la innovación, haciendo uso de nuevas tecnologías de inteligencia artificial presenta su 1er agente diseñado para servir como chatbot entrenado en mantenimiento y confiabilidad. El entrenamiento se fundamentó en el aprovechamiento de modelos generativos contextualizados de manera especifica y en la vectorización de referencias bibliográficas respetando el derecho de los autores, mejores prácticas (SMRP), métricas clase mundial, estándares como la ISO 14224, ISO 55000 (gestión de activos). Adicionalmente, orientará sus respuestas con base en el modelo de gestión de servicio de OMIA.\t
#    """ 
text_2 =     """
    El OMIA AI agent es capaz de soportar a nuestros profesionales de mantenimiento y confiabilidad en el dominio de terminologías técnicas específicas, conceptos, asistir de manera interpersonal en interpretaciones y análisis cualitativos con base en el procesamiento de datos e indicadores, generación de informes y datos estructurados insumos para la visualización de información. 
    Este gran impulso tecnológico contribuirá con el fortalecimiento de las competencias técnicas de nuestros profesionales, permitirá unificar criterios, gestionar el conocimiento, soportar para mejorar en términos de eficiencia la interpretación y análisis para la toma de decisiones.
    """


with st.sidebar:
#   st.markdown('<div style="text-align: justify;">{}</div>'.format(tex_1), unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify;">{}</div>'.format(text_2), unsafe_allow_html=True)
    st.markdown('---')
    st.button('Clear Chat History', on_click=clear_chat, )
    


#st.title("👨‍💻OMIA GPT AI") #todo Omia GPT: mantenimiento y confiabilidad

col1, mid, col2 = st.columns([11,3,50])

with col1:
    st.image('images\Logo OMIA.png', width=200)

with col2:
    st.title('GPT AI: mantenimiento y confiabilidad', )

if "message" not in st.session_state.keys():
    st.session_state["message"] = [{'role':'assistant', "content":"🖐 Hola, yo soy agente de inteligencia artificial especialista en mantenimiento y confiabilidad. ¿En que te puedo ayudar?"}]

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



    

