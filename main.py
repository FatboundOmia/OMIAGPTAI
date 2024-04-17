from langchain_google_genai import GoogleGenerativeAI, ChatGoogleGenerativeAI


GOOGLE_API_KEY = 'AIzaSyB0hf-O1dIEyx09hmxvDYo0dwWH6O_WrLc'


llm = ChatGoogleGenerativeAI(model='gemini-pro', google_api_key=GOOGLE_API_KEY, temperature=0.3, verbose=True)

while True:
    
    pregunta = input("Pregunta:")
    result = llm.invoke('{}'.format(pregunta))
    print('=='*25)
    print(result.content)
    print('=='*25)