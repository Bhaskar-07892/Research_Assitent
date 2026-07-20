from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors.chain_extract import LLMChainExtractor

from research_paper_assistant.utils.logger import logging


def get_compression_retriever(vectordb, llm=None):
    base_retriever = vectordb.as_retriever(
        search_kwargs={"k": 5}
    )

    if llm is None:
        logging.warning("No LLM provided; using basic retriever without contextual compression.")
        return base_retriever

    try:
        compressor = LLMChainExtractor.from_llm(llm)

        compression_retriever = ContextualCompressionRetriever(
            base_retriever=base_retriever,
            base_compressor=compressor,
        )

        return compression_retriever
    except Exception as exc:
        logging.warning(f"Falling back to basic retriever because contextual compression failed: {exc}")
        return base_retriever