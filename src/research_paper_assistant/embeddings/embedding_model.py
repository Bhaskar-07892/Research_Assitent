from langchain_huggingface import HuggingFaceEmbeddings

# convert langchain document into string 

def docs_converted_into_str (docs) : 
    text = [doc.page_content for doc in docs]
    return text 

def get_embedding_model():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )