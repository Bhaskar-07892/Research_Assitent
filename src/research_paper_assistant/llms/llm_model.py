import os
import sys

from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint

from research_paper_assistant.utils.exception import CustomException

load_dotenv()


def get_llm():
    try:
        token = os.getenv("HUGGINGFACEHUB_API_TOKEN") or os.getenv("HF_TOKEN")
        llm_kwargs = {
            "repo_id": "meta-llama/Llama-3.1-8B",
            'provider':"featherless-ai",
            "max_new_tokens": 200,
            "temperature": 0.7,
        }
        if token:
            llm_kwargs["huggingfacehub_api_token"] = token

        llm = HuggingFaceEndpoint(**llm_kwargs)
        return llm

    except Exception as e:
        raise CustomException(e, sys)