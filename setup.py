from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Returns a list of requirements from the given file, 
    excluding the '-e .' line used for editable installs.
    """
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

from setuptools import setup, find_packages

setup(
    name="research-paper-assistant",
    version="0.0.1",
    author="Bhaskar Pathak",
    author_email="bhaskarpathak5607@gmail.com",

    package_dir={"": "src"},
    packages=find_packages(where="src"),

    install_requires=get_requirements("requirements.txt"),
)