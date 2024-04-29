from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
import document


GOOGLE_API_KEY = 'AIzaSyB0hf-O1dIEyx09hmxvDYo0dwWH6O_WrLc'
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
        Answer the question, if the answer is not in
        provided context just say, "I'm OMIA GPT AI, I only response reliability and maintenance question"\n\n
        \n\n if the user make the question "what is your name or similar" respond "I'm OMIA GPT AI"
        Context:\n {context}?\n
        Question: \n{question}\n
        Please always add the source the information with autor and response in spanish always.
        respond without markdowmn. 
        Answer:
    """

    prompt = PromptTemplate(template=promp_template, input_variables=["context","question"])

    model = ChatGoogleGenerativeAI(model='gemini-1.5-pro-latest', temperature=0.6, google_api_key=GOOGLE_API_KEY )
    chain = load_qa_chain(model, chain_type='stuff', prompt=prompt)

    response = chain.invoke(
        {"input_documents":docs, "question":question})

    return response["output_text"]
