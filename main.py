from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
import document
import os 
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')



text = document.document()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=200)
context = "\n\n".join(str(p.page_content) for p in text)
texts = text_splitter.split_text(context)

embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001',google_api_key=GOOGLE_API_KEY, task_type='SEMANTIC_SIMILARITY')

vector_index = Chroma.from_texts(texts, embeddings).as_retriever()


def pregunta(question):
    from langchain_google_genai import ChatGoogleGenerativeAI
    docs = vector_index.get_relevant_documents(query=question)

    promp_template = """
    Quiero que respondas lo mas claro y conciso posible. Puedes utilizar tu imaginación para responder las preguntas.
    {context}
    question :
    {question}
    
    siempre a tus repuestas agrega la fuente de información
    """

    prompt = PromptTemplate(template=promp_template, input_variables=["context","question"])

    model = ChatGoogleGenerativeAI(model='gemini-1.5-pro-latest', temperature=0.2, google_api_key=GOOGLE_API_KEY )
    chain = load_qa_chain(model, chain_type='stuff', prompt=prompt)

    response = chain.invoke(
        {"input_documents":docs, "question":question})

    return response["output_text"]
