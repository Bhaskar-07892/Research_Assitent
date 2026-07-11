import os

folders = [
    "data/uploads",
    "data/processed",
    "data/exports",

    "src/research_paper_assistant",

    "src/research_paper_assistant/loaders",
    "src/research_paper_assistant/splitters",
    "src/research_paper_assistant/embeddings",
    "src/research_paper_assistant/vectorstores",
    "src/research_paper_assistant/docstore",
    "src/research_paper_assistant/retrievers",
    "src/research_paper_assistant/prompts",
    "src/research_paper_assistant/chains",
    "src/research_paper_assistant/services",
    "src/research_paper_assistant/utils",
    "src/research_paper_assistant/config",
]

files = [

    # Package
    "src/research_paper_assistant/__init__.py",

    # Loaders
    "src/research_paper_assistant/loaders/__init__.py",
    "src/research_paper_assistant/loaders/pdf_loader.py",

    # Splitters
    "src/research_paper_assistant/splitters/__init__.py",
    "src/research_paper_assistant/splitters/parent_splitter.py",
    "src/research_paper_assistant/splitters/child_splitter.py",

    # Embeddings
    "src/research_paper_assistant/embeddings/__init__.py",
    "src/research_paper_assistant/embeddings/embedding_model.py",

    # Vector Store
    "src/research_paper_assistant/vectorstores/__init__.py",
    "src/research_paper_assistant/vectorstores/chroma_db.py",

    # DocStore
    "src/research_paper_assistant/docstore/__init__.py",
    "src/research_paper_assistant/docstore/parent_store.py",

    # Retrievers
    "src/research_paper_assistant/retrievers/__init__.py",
    "src/research_paper_assistant/retrievers/basic_retriever.py",
    "src/research_paper_assistant/retrievers/parent_child.py",
    "src/research_paper_assistant/retrievers/multi_query.py",
    "src/research_paper_assistant/retrievers/compression.py",

    # Chains
    "src/research_paper_assistant/chains/__init__.py",
    "src/research_paper_assistant/chains/qa_chain.py",
    "src/research_paper_assistant/chains/summary_chain.py",
    "src/research_paper_assistant/chains/compare_chain.py",
    "src/research_paper_assistant/chains/notes_chain.py",
    "src/research_paper_assistant/chains/equation_chain.py",

    # Prompts
    "src/research_paper_assistant/prompts/__init__.py",
    "src/research_paper_assistant/prompts/qa_prompt.py",
    "src/research_paper_assistant/prompts/summary_prompt.py",
    "src/research_paper_assistant/prompts/compare_prompt.py",
    "src/research_paper_assistant/prompts/notes_prompt.py",
    "src/research_paper_assistant/prompts/equation_prompt.py",

    # Services
    "src/research_paper_assistant/services/__init__.py",
    "src/research_paper_assistant/services/indexing_service.py",
    "src/research_paper_assistant/services/query_service.py",
    "src/research_paper_assistant/services/pdf_service.py",

    # Utils
    "src/research_paper_assistant/utils/__init__.py",
    "src/research_paper_assistant/utils/logger.py",
    "src/research_paper_assistant/utils/exception.py",
    "src/research_paper_assistant/utils/helpers.py",

    # Config
    "src/research_paper_assistant/config/__init__.py",
    "src/research_paper_assistant/config/settings.py",

    # Root Files
    "app.py",
    "config.yaml",
    ".env",
    "requirements.txt",
    "setup.py",
    "Dockerfile",
    "README.md",
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file in files:
    open(file, "a").close()

print("Research Paper Assistant project structure created successfully!")# Created by venv; see https://docs.python.org/3/library/venv.html
