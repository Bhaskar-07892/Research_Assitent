from pathlib import Path
from research_paper_assistant.loaders.pdf_loader import loadpath_pdf
from research_paper_assistant.splitters.parent_splitter import parent_docs_splitter
from research_paper_assistant.splitters.child_splitter import child_docs_spliter
from research_paper_assistant.docstore.parent_store import store_parent_docs
from research_paper_assistant.embeddings.embedding_model import get_embedding_model , docs_converted_into_str
from research_paper_assistant.vectorstores.chroma_db import vector

# call all component in right order 
def indexing_services_ (filename) : 


    ROOT_DIR = Path(__file__).resolve().parent

    #uploaded pdf path
    pdf_path = ROOT_DIR / "data" / "uploads" / filename

    # language object (document) loading 
    loader = loadpath_pdf(str(pdf_path))
    data = loader.load()
    # print(data)


    # parent spiliting
    data_Loaded = parent_docs_splitter(data)
    # print(data_Loaded[0:5])
    # print(len(data_Loaded))


    # child spliting
    data_Loaded1 = child_docs_spliter(data_Loaded)
    # print(data_Loaded1[0])
    # print(len(data_Loaded1))


    # store parent document in ram
    d = store_parent_docs(data_Loaded)


    # convert document to str for creating embedding 
    str_text = docs_converted_into_str(data_Loaded1)
    # print(str_text)


    # initilise embedding model 
    embedd_model= get_embedding_model()


    # store embedding vector into database
    embedd_text = vector(chunk_document=data_Loaded1 , embedding_model=embedd_model , persist_dir="data/chroma_db")
    # print (embedd_text)