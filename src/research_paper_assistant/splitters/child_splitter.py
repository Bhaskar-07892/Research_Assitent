from langchain_text_splitters import RecursiveCharacterTextSplitter
from research_paper_assistant.utils.exception import CustomException
from research_paper_assistant.utils.logger import logging


def child_docs_spliter (parent_docs) : 
    try : 
            
        text_spliter = RecursiveCharacterTextSplitter(
            chunk_size = 500 , 
            chunk_overlap = 120 
        )

        child_docs = []

        for doc in parent_docs :
            childern = text_spliter.split_documents([doc])

            for child in childern : 
                child.metadata["doc_id"] = doc.metadata["doc_id"]

            child_docs.extend(childern)

    
            
        logging.info("Child chunking successfully ...")

        return child_docs

    except Exception as e : 
        logging.error("Error during child spliting")
        raise CustomException("Error while spliting child")