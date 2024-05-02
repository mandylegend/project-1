from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path: str) -> List[str]:
    """
    this function will return the list of requirements

    """

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n'," ") for req in requirements]

    return requirements




setup(
    name="Project 1",
    author="Mandar",
    version="0.0.1",
    author_email="moremandar026@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('req.txt')
)