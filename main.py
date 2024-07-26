from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
import document
import os 
from dotenv import load_dotenv


load_dotenv()# Cargo archivo que contine mis variables de entorno


#####################################
#Sección de codigo en el que cargo el modelo de LLM

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')
############################################
#Sección de codigo que carga los PDF y lo pone en chunks y hace un embedding con ellos
text = document.document()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=200)
context = "\n\n".join(str(p.page_content) for p in text)
texts = text_splitter.split_text(context)

embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001',google_api_key=GOOGLE_API_KEY, task_type='SEMANTIC_SIMILARITY')

vector_index = Chroma.from_texts(texts, embeddings).as_retriever()

############################################

def pregunta(question):
    """
    Función que ingresa la pregunta en mi llm y en mi prompt para ser mandada al agente
    Retorna la respuesta del LLM
    
    """
    from langchain_google_genai import ChatGoogleGenerativeAI
    docs = vector_index.get_relevant_documents(query=question)

    promp_template = """
        Answer the question, if the answer is not in
        provided context calculate de answer with public data\n\n if the answer is different about reliability and maintenance respond 'Yo soy agente de confiabilidad y mantenimiento de OMIA, OMIA GPT AI'
        \n\n if the user make the question "what is your name or similar" respond "Yo soy OMIA GPT AI"
        Context:\n {context}?\n
        Question: \n{question}\n
        Please always add the source the information with autor and response in spanish always.
        Answer:
    """

    prompt = PromptTemplate(template=promp_template, input_variables=["context","question"])

    model = ChatGoogleGenerativeAI(model='gemini-1.5-pro-latest', temperature=0.6, google_api_key=GOOGLE_API_KEY)
    chain = load_qa_chain(model, chain_type='stuff', prompt=prompt)

    response = chain.invoke(
        {"input_documents":docs, "question":question})

    return response["output_text"]
