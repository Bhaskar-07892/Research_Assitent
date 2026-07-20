from pathlib import Path
import sys

from research_paper_assistant.loaders.pdf_loader import loadpath_pdf
from research_paper_assistant.splitters.parent_splitter import parent_docs_splitter
from research_paper_assistant.splitters.child_splitter import child_docs_spliter
from research_paper_assistant.docstore.parent_store import store_parent_docs
from research_paper_assistant.embeddings.embedding_model import get_embedding_model
from research_paper_assistant.vectorstores.chroma_db import get_vector
from research_paper_assistant.utils.logger import logging
from research_paper_assistant.utils.exception import CustomException


def indexing_services(filename: str):
    """
    Index a PDF into the RAG pipeline.

    Pipeline:
    1. Load PDF
    2. Split into Parent Chunks
    3. Split into Child Chunks
    4. Store Parent Documents
    5. Create Embeddings
    6. Store Child Embeddings in ChromaDB
    """

    try:
        logging.info("========== Indexing Started ==========")

        # Project Root
        root_dir = Path(__file__).resolve().parent.parent.parent.parent

        pdf_path = root_dir / "data" / "uploads" / filename

        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF not found: {pdf_path}")

        logging.info(f"Loading PDF: {filename}")

        # Load PDF
        loader = loadpath_pdf(str(pdf_path))
        documents = loader.load()

        logging.info(f"Loaded {len(documents)} document(s).")

        # Parent Split
        parent_docs = parent_docs_splitter(documents)

        logging.info(
            f"Created {len(parent_docs)} parent chunks."
        )

        # Child Split
        child_docs = child_docs_spliter(parent_docs)

        logging.info(
            f"Created {len(child_docs)} child chunks."
        )

        # Store Parent Documents
        store_parent_docs(parent_docs)

        logging.info("Parent documents stored successfully.")

        # Embedding Model
        embedding_model = get_embedding_model()

        logging.info("Embedding model loaded successfully.")

        # Store Child Embeddings
        get_vector(
            chunk_document=child_docs,
            embedding_model=embedding_model,
            persist_dir="data/chroma_db"
        )

        logging.info("Child embeddings stored successfully.")

        logging.info("========== Indexing Completed ==========")

        return {
                "status": "success",
                "filename": filename,
                "parent_chunks": len(parent_docs),
                "child_chunks": len(child_docs),
                }

    except Exception as e:

        logging.exception("Indexing Service Failed.")

        raise CustomException(e, sys)