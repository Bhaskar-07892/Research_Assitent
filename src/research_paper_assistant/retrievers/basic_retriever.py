from research_paper_assistant.utils.exception import CustomException
from research_paper_assistant.utils.logger import logging
import sys 

def retrieve_documents(vectordb, user_query):

    try:
        if vectordb is None:
            raise ValueError("Vector database is not initialized.")

        retriever = vectordb.as_retriever(
            search_kwargs={"k": 5}
        )

        retrieved_docs = retriever.invoke(user_query)

        return retrieved_docs

    except ValueError as e:
        logging.error(f"Value Error: {e}")
        raise CustomException("vectordb has no data , it's empty" , sys)

    except Exception as e:
        logging.exception(f"Error while retrieving documents: {e}")
        raise CustomException("error in vectordb" , sys)