from langchain_core.output_parsers import StrOutputParser

from research_paper_assistant.prompts.notes_prompt import notes_prompt


prompt = notes_prompt
parser = StrOutputParser()

def get_notes_chain (llm) : 
    "Created summary chain"

    chain = prompt | llm | parser

    return chain