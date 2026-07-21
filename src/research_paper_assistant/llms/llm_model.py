import os
import sys

from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint

from research_paper_assistant.utils.exception import CustomException

load_dotenv()


def get_llm():
    try:

        llm = HuggingFaceEndpoint(
            repo_id=os.getenv("HF_LLM_MODEL"),
            provider=os.getenv("HF_LLM_PROVIDER"),
            huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
            temperature=0,
            max_new_tokens=512,
        )

        return llm

    except Exception as e:
        raise CustomException(e, sys)