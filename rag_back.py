import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import BedrockEmbeddings
from langchain.vectorstores import FAISS
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms.bedrock import Bedrock

def hr_index():
    # Define the data source and load data with PDFLoader
    data_load = PyPDFLoader(r'C:\Users\sahil\OneDrive\Documents\AgriArogya\__CROP_INFORMATION_Cleaned__ (1).pdf')
    
    # Split the Text based on Character, Tokens etc.
    data_split = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", " ", ""],
        chunk_size=100,
        chunk_overlap=10
    )
    
    # Create Embeddings -- Client connection
    data_embeddings = BedrockEmbeddings(
        credentials_profile_name='default',
        model_id='amazon.titan-embed-text-v1'
    )
    
    # Create Vector DB, Store Embeddings and Index for Search
    data_index = VectorstoreIndexCreator(
        text_splitter=data_split,
        embedding=data_embeddings,
        vectorstore_cls=FAISS
    )
    
    # Create index for HR Policy Document
    db_index = data_index.from_loaders([data_load])
    
    return db_index

def hr_llm():
    # Write a function to connect to Bedrock Foundation Model
    llm = Bedrock(
        credentials_profile_name='default',
        model_id='anthropic.claude-v2',
        model_kwargs={
            "max_tokens_to_sample": 3000,
            "temperature": 0.1,
            "top_p": 0.9
        }
    )
    return llm

def hr_rag_response(index, question):
    # Write a function which searches the user prompt, searches the best match from Vector DB and sends both to LLM.
    rag_llm = hr_llm()
    hr_rag_query = index.query(question=question, llm=rag_llm)
    return hr_rag_query
