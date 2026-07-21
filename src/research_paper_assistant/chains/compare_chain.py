from langchain_core.output_parsers import StrOutputParser
from research_paper_assistant.prompts.compare_prompt import compare_prompt


prompt = compare_prompt
parser = StrOutputParser()

def get_comprision_chain (llm) : 
    "Created comperision chain"

    chain = prompt | llm | parser

    return chain