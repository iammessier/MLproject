from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> list:
    """
    This function reads the requirements from a file and returns them as a list.
    """
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements ]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.1.0',
    author='Jay Nahata',
    author_email='nahatajay6@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt'),
    description='A machine learning project setup',
    long_description=open('README.md').read(),

)