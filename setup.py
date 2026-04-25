from setuptools import find_packages,setup
from typing import List

E_DOT="-e ."

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if E_DOT in requirements:
            requirements.remove(E_DOT)
    return requirements


setup(
    name="Titanic",
    version="0.0.1",
    author="Manthan",
    author_email="bhisemanthan985@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)