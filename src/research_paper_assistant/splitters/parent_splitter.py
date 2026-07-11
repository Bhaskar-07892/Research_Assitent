from research_paper_assistant.utils.exception import CustomException
import sys
from research_paper_assistant.utils.logger import logging


from langchain_text_splitters import RecursiveCharacterTextSplitter
import uuid 



def parent_docs_splitter (docs) : 
    try : 
        # obj of RecursiveCharacterTextSplitter
        docs_spliter = RecursiveCharacterTextSplitter(
            chunk_size = 2000 , 
            chunk_overlap = 200 ,
        )

        # use RecursiveCharacterTextSplitter give docs 
        splited_docs = docs_spliter.split_documents(docs)

        for doc in splited_docs : 
            doc.metadata["doc_id"] = str(uuid.uuid4())
            
        # for doc in splited_docs:
        #     print(doc.metadata["doc_id"])

        logging.info("Child chunking successfully ...")
        return splited_docs

    # Error Handling
    except Exception as e : 
        logging.error("Error during Parent spliting" , e)
        raise CustomException(e , sys)