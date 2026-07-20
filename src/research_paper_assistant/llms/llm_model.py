import os
import sys

from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint

from research_paper_assistant.utils.logger import logging
from research_paper_assistant.utils.exception import CustomException

load_dotenv()


def get_llm():
    """
    Initialize and return the Hugging Face LLM.
    """

    try:
        logging.info("Initializing Hugging Face LLM...")

        api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN") or os.getenv("HF_TOKEN")

        if not api_key:
            logging.warning("No Hugging Face token found; LLM features will be disabled.")
            return None

        model_name = os.getenv("HF_LLM_MODEL", "google/gemma-2-2b-it")
        provider = os.getenv("HF_LLM_PROVIDER", "hf-inference")

        llm = HuggingFaceEndpoint(
            repo_id=model_name,
            provider=provider,
            task="conversational",
            huggingfacehub_api_token=api_key,
            temperature=0,
            max_new_tokens=256,
        )

        logging.info("LLM initialized successfully.")

        return llm

    except Exception as e:
        logging.exception("Failed to initialize LLM.")
        raise CustomException(e, sys)