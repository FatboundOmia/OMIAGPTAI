
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def document():
    """Función que carga todos los archivos PDF, con su directorio

    Returns:
        List: Se retorna una lista con todos los archivos de de PDF que van a ser cargados
        en el chat
    """
    data_final = []
    loader = PyPDFDirectoryLoader(path="files")
    data_final.extend(loader.load_and_split())
    return data_final


if __name__ == '__main__':
    document()