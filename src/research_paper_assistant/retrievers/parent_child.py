from research_paper_assistant.docstore.parent_store import get_parent_doc


def retrieve_parent_documents(top_docs):

    retrieved_doc_ids = set()

    # Collect unique parent document IDs
    for doc in top_docs:
        retrieved_doc_ids.add(doc.metadata["doc_id"])

    # Fetch parent documents
    parent_docs = []
    for doc_id in retrieved_doc_ids:
        parent_doc = get_parent_doc(doc_id)
        if parent_doc is not None:
            parent_docs.append(parent_doc)

    return parent_docs