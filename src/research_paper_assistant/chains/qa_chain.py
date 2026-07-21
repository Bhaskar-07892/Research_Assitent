from langchain_core.output_parsers import StrOutputParser
from research_paper_assistant.prompts.qa_prompt import qa_prompt

prompt = qa_prompt
parser = StrOutputParser()

def get_qa_chain (llm) : 
    " Creat Question Answering chain" 

    chain = prompt | llm | parser 

    return chain 

