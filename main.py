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
texts = text_splitter.split_text(text)

embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001')

vector_index = Chroma.from_texts(texts, embeddings).as_retriever()




