from setuptools import setup, find_packages
from typing import List


EDOT = "-e ."
def get_requirements(path_file:str)->List[str]:

    requirements = []
    with open(path_file)as file_obj:
        requirements = file_obj.readlines()
        requirements = [r.replace('\n', " ") for r in requirements]

        if EDOT in requirements:
            requirements.remove(EDOT)

    return requirements



setup(
    name='mlproject',
    version='0.0.1',
    author='Dayo',
    author_email='onitemidayo@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)