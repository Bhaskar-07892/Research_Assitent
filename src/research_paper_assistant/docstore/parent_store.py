from langchain_core.stores import InMemoryStore

docstore = InMemoryStore()


def store_parent_docs(parent_docs):

    pairs = []

    for doc in parent_docs:

        

        pair = (
            doc.metadata["doc_id"],
            doc
        )

        pairs.append(pair)
        
    docstore.mset(pairs)


def get_parent_doc(doc_id):


    parent = docstore.mget([doc_id])

    return parent[0]