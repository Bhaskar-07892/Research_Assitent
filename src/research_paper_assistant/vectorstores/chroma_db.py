from langchain_chroma import Chroma

def vector (chunk_document , embedding_model , persist_dir) :
    vector_store = Chroma.from_documents(
        documents = chunk_document , 
        embedding= embedding_model , 
        persist_directory= persist_dir
    )
    return vector_store