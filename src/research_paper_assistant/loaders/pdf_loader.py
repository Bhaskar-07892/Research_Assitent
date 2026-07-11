from langchain_community.document_loaders import PyMuPDFLoader
from research_paper_assistant.utils.exception import CustomException
import sys
from research_paper_assistant.utils.logger import logging


def loadpath_pdf(filepath):
    # load data into docs format 
    try:
        pdf_loader = PyMuPDFLoader(filepath)
        logging.info("File loaded successfully ...")
        return pdf_loader

    # error handling 
    except Exception as e:
        logging.error("Error in loading pdf: %s", e)
        raise CustomException(e, sys)


