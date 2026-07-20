from research_paper_assistant.docstore.parent_store import get_parent_doc
from langchain_core.documents import Document


def test_get_parent_doc_returns_stored_document(tmp_path, monkeypatch):
    from research_paper_assistant.docstore import sqlite_store

    db_path = tmp_path / "docstore.db"
    monkeypatch.setattr(sqlite_store, "SQLiteDocStore", lambda: sqlite_store.SQLiteDocStore(db_path=str(db_path)))

    from research_paper_assistant.docstore.parent_store import docstore, store_parent_docs

    doc = Document(page_content="hello", metadata={"doc_id": "doc-1"})
    store_parent_docs([doc])

    result = get_parent_doc("doc-1")

    assert result is not None
    assert result.page_content == "hello"
    assert result.metadata["doc_id"] == "doc-1"
