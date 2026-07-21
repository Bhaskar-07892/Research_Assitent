from research_paper_assistant.llms.llm_model import get_llm

llm = get_llm()

print(llm.invoke("What is Artificial Intelligence?"))