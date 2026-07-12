from research_paper_assistant.embeddings.embedding_model import get_embedding_model



user_question = input("Enter your question :")

# embedd user question 
embedd_init = get_embedding_model()

embedd_question = embedd_init.embed_query(user_question)

print(embedd_question)


