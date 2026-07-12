from pathlib import Path
from research_paper_assistant.loaders.pdf_loader import loadpath_pdf
from research_paper_assistant.splitters.parent_splitter import parent_docs_splitter
from research_paper_assistant.splitters.child_splitter import child_docs_spliter
from research_paper_assistant.docstore.parent_store import store_parent_docs
from research_paper_assistant.embeddings.embedding_model import get_embedding_model , docs_converted_into_str
from research_paper_assistant.vectorstores.chroma_db import vector


ROOT_DIR = Path(__file__).resolve().parent

pdf_path = ROOT_DIR / "data" / "uploads" / "Artificial_Intelligence_in_the_21st_Century.pdf"

loader = loadpath_pdf(str(pdf_path))
data = loader.load()
# print(data)

data_Loaded = parent_docs_splitter(data)
# print(data_Loaded[0:5])

print(len(data_Loaded))

data_Loaded1 = child_docs_spliter(data_Loaded)
# print(data_Loaded1[0])


# print(len(data_Loaded1))

d = store_parent_docs(data_Loaded)

str_text = docs_converted_into_str(data_Loaded1)

# print(str_text)

embedd_model= get_embedding_model()

embedd_text = vector(chunk_document=data_Loaded1 , embedding_model=embedd_model , persist_dir="data/chroma_db")

# print (embedd_text)