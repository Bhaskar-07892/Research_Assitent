import sys

from langchain_chroma import Chroma

from research_paper_assistant.embeddings.embedding_model import get_embedding_model
from research_paper_assistant.llms.llm_model import get_llm

from research_paper_assistant.retrievers.compression import get_compression_retriever
from research_paper_assistant.retrievers.parent_child import retrieve_parent_documents

from research_paper_assistant.utils.logger import logging
from research_paper_assistant.utils.exception import CustomException

# answer genretion imports
from research_paper_assistant.chains.qa_chain import get_qa_chain
from research_paper_assistant.chains.summary_chain import get_summary_chain
from research_paper_assistant.chains.notes_chain import get_notes_chain
from research_paper_assistant.chains.compare_chain import get_comprision_chain
from research_paper_assistant.chains.equation_chain import get_equation_chain



def query_services(user_query: str):

    try:

        logging.info("========== Query Started ==========")

        # Embedding Model
        embedding_model = get_embedding_model()

        # Load Chroma
        vectordb = Chroma(
            persist_directory="data/chroma_db",
            embedding_function=embedding_model,
        )

        # Load LLM
        llm = None
        try:
            llm = get_llm()

        except Exception as exc:
            logging.warning(f"LLM initialization failed; continuing with basic retrieval: {exc}")

        # Create Compression Retriever
        compression_retriever = get_compression_retriever(
            vectordb=vectordb,
            llm=llm,
        )

        # Retrieve Documents
        try:
            child_docs = compression_retriever.invoke(user_query)
        except Exception as exc:
            logging.warning(f"Compression retrieval failed; falling back to basic retrieval: {exc}")
            child_docs = vectordb.as_retriever(search_kwargs={"k": 5}).invoke(user_query)

        logging.info(
            f"Retrieved {len(child_docs)} child documents."
        )

        # Parent Retrieval
        parent_docs = retrieve_parent_documents(child_docs)


        logging.info(
            f"Retrieved {len(parent_docs)} parent documents."
        )

        # join all page_content 
        context = '/n/n'.join(
            doc.page_content for doc in parent_docs
        )

        query = user_query.lower()

        

        if "summary" in query : 
            chain = get_summary_chain(llm = llm)

        elif "note" in query or "notes" in query:
            chain = get_notes_chain(llm)

        elif "compare" in query or "difference" in query:
            chain = get_comprision_chain(llm)

        elif "equation" in query or "formula" in query:
            chain = get_equation_chain(llm)

        else:
            chain = get_qa_chain(llm)

    
        response = chain.invoke({
            "context" : context , 
            "question" : query      
                    })
        return response

    except Exception as e:
        logging.exception("Query Service Failed.")
        raise CustomException(e, sys)