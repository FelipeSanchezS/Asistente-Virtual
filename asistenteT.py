import streamlit as st
from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_ollama import ChatOllama
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA


# Título de la aplicación
st.title("Prueba técnica / RAG")

# Cargar el archivo PDF solo una vez y configurar el chatbot
def iniciar_chat():
    # Cargar el documento ya predefinido
    ruta_archivo = "010-25.pdf"  # Este es el archivo predefinido

    loader = PyMuPDFLoader(ruta_archivo)
    data_pdf = loader.load()
    #print(data_pdf[0])

    # Dividir el documento en partes
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(data_pdf)

    # Realizar los embeddings
    embed_model = FastEmbedEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Usar Chroma para almacenamiento y recuperación de vectores
    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=embed_model,
        persist_directory="chroma_db_dir",
        collection_name="prueba"
    )
    retriever = vectorstore.as_retriever(search_kwargs={'k': 2})

    # Crear el prompt para la recuperación
    custom_prompt_template = """Se un especialista sobre el tema y usa la siguiente información para responder las preguntas que te hago
    Si no sabes, di que no lo sabes y no inventes respuesta
    
    Contexto: {context}
    Pregunta: {question}

    Solo devuelve la respuesta útil a continuación y nada más
    Respuesta útil:"""
    prompt = PromptTemplate(template=custom_prompt_template, input_variables=['context', 'question'])

    # Crear la cadena de recuperación de preguntas y respuestas
    #llm = ChatOllama(model="gemma:2b")
    llm = ChatOllama(model="llama3")  # Asegúrate de que este modelo esté disponible
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )
    
    return qa
    #response = qa.invoke({"query": "who is the author?"})
    #print(response['result'])

# Iniciar el chatbot con el PDF cargado por defecto
qa = iniciar_chat()

# Inicializar un contenedor para el chat
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "¡Hola!. Puedes preguntarme sobre el contenido del documento."}]

# Mostrar los mensajes anteriores
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

# Interacción con el usuario
user_input = st.chat_input("Haz una pregunta sobre el documento")
if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Obtener la respuesta del asistente basada en el documento
    respuesta = qa.invoke({"query": user_input})
    respuesta_texto = respuesta['result']
    
    # Mostrar la respuesta generada
    st.session_state["messages"].append({"role": "assistant", "content": respuesta_texto})
    st.chat_message("assistant").write(respuesta_texto)
