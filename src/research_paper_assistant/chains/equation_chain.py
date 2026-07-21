from langchain_core.output_parsers import StrOutputParser

from research_paper_assistant.prompts.equation_prompt import equation_prompt


prompt = equation_prompt
parser = StrOutputParser()

def get_equation_chain (llm) : 
    "Created equation chain "

    chain = prompt | llm | parser

    return chain