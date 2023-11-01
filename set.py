from setuptools import find_packages,setup

from typing import List

def get_requirements()->List[str]:

REQUIREMENT_FILE_NAME="requirements.txt"    

setup(
    name = "sesnor",
    version="0.0.1",
    author_email="ashwin.dhamnaskar22@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),
)