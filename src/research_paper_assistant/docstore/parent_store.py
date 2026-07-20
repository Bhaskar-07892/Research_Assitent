from research_paper_assistant.docstore.sqlite_store import SQLiteDocStore

docstore = SQLiteDocStore()


def store_parent_docs(parent_docs):

    pairs = []

    for doc in parent_docs:

        pairs.append(
            (
                doc.metadata["doc_id"],
                doc
            )
        )

    docstore.mset(pairs)


def get_parent_doc(doc_id):
    return docstore.mget([doc_id])[0]