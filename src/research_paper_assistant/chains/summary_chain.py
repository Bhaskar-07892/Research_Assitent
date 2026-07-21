from langchain_core.output_parsers import StrOutputParser
from research_paper_assistant.prompts.summary_prompt import summary_prompt

prompt = summary_prompt
parser = StrOutputParser()

def get_summary_chain (llm) : 
    "Created Summary chain" 

    chain = prompt | llm | parser

    return chain
