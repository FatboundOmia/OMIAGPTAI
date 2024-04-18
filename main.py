from langchain_google_genai import GoogleGenerativeAI, ChatGoogleGenerativeAI
from IPython.display import Markdown
from IPython.display import display
import textwrap
import google.generativeai as genai
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
import document
from langchain_google_genai import GoogleGenerativeAIEmbeddings


GOOGLE_API_KEY = 'AIzaSyB0hf-O1dIEyx09hmxvDYo0dwWH6O_WrLc'
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')



text = document.document()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=200)
context = "\n\n".join(str(p.page_content) for p in text)
texts = text_splitter.split_text(context)

embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001',google_api_key=GOOGLE_API_KEY)

vector_index = Chroma.from_texts(texts, embeddings).as_retriever()


def pregunta(question):
    
    docs = vector_index.get_relevant_documents(query=question)

    promp_template = """
    Responde lo mas claro posible y utilizando tus base de conocimientos para responder
    {context}
    question :
    {question}
    """

    prompt = PromptTemplate(template=promp_template, input_variables=["context","question"])

    model = ChatGoogleGenerativeAI(model='gemini-pro', temperature=0.9, google_api_key=GOOGLE_API_KEY)
    chain = load_qa_chain(model, chain_type='stuff', prompt=prompt)

    response = chain.invoke(
        {"input_documents":docs, "question":question}, return_only_outputs=True 
    )

    return response["output_text"]


while True:
    question = str(input("Que deseas preguntar sobre el manual: "))
    print('=='*50)
    print(pregunta(question))
    print('=='*50)

