# Asistente-Virtual


Este repositorio contiene un agente de *Retrieval-Augmented Generation* (RAG) basado en un modelo de lenguaje de gran escala (*Large Language Model*, LLM), diseñado para interactuar con un documento específico de manera experta. Utilizando una combinación de tecnologías como Python, LangChain, Ollama LLaMA 3, y una interfaz gráfica en Streamlit, este sistema permite al usuario interactuar de manera eficiente con el contenido de un documento PDF y obtener respuestas precisas sobre el mismo.

## Descripción del Proyecto

Este proyecto implementa un sistema RAG que combina un modelo de lenguaje *LLM* con la capacidad de recuperar información del documento suministrado. Se realizan operaciones de embeddings y fragmentación de texto (chunks) para analizar y generar respuestas coherentes basadas en el contenido del documento. El agente está diseñado para proporcionar respuestas expertas y relevantes en función del contexto del documento.

La aplicación incluye una interfaz gráfica interactiva para facilitar la interacción con el agente virtual, utilizando *Streamlit* para hacerla accesible y fácil de usar.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal.
- **LangChain**: Biblioteca para integrar diversos componentes como el manejo de embeddings, cargadores de documentos y generación de respuestas.
- **Ollama LLaMA 3**: Modelo de lenguaje de código abierto de Meta, utilizado como base del agente para la generación de respuestas.
- **PyMuPDF**: Herramienta utilizada para leer y extraer texto de documentos PDF.
- **Sentence-Transformers**: Usado para crear embeddings de los fragmentos de texto.
- **Streamlit**: Herramienta para crear la interfaz gráfica de usuario.

## Funcionalidad

1. **Carga y Procesamiento del Documento**:
   - El sistema Esta entrenado con un documento en especifico pero puede ser modificado segun la necesidad
   - El documento se fragmenta en partes más pequeñas (*chunks*) de 1000 caracteres, con una superposición de 200 caracteres entre párrafos.

2. **Embeddings**:
   - Se generan embeddings para los fragmentos utilizando el modelo *sentence-transformers/all-MiniLM-L6-v2*, que convierte los fragmentos en vectores numéricos para ser comparados posteriormente.

3. **Generación de Respuestas**:
   - Utilizando el modelo *Ollama LLaMA 3*, el sistema responde consultas del usuario basándose en los fragmentos más relevantes extraídos del documento.
   - La comparación de embeddings permite seleccionar los fragmentos más similares a la consulta del usuario, garantizando respuestas precisas.

4. **Interfaz Gráfica**:
   - Se crea una interfaz de usuario con *Streamlit*, donde los usuarios pueden cargar documentos PDF, hacer preguntas sobre el contenido y recibir respuestas generadas por el agente experto.

## Instalación

### Requisitos Previos

Asegúrate de tener instalado Python 3.8 o superior. Además, necesitarás tener acceso a Internet para descargar los modelos y dependencias necesarias.

### Pasos para la Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio

