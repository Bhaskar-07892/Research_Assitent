from langchain_community.retrievers import MultiQueryRetriever

def retrieve_multi_query(user_query, vectordb, llm) :

    retriever = vectordb.as_retriever(
        search_kwargs={"k": 5}
    )

    multi_retriever = MultiQueryRetriever.from_llm(
        retriever=retriever,
        llm=llm
    )

    docs = multi_retriever.invoke(user_query)

    return docs