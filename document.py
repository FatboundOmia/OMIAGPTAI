
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def document():
    loader = PyPDFDirectoryLoader(path="files")
    data = loader.load_and_split()
    return data


if __name__ == '__main__':
    document()