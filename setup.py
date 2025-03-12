from setuptools import find_packages,setup #finds all the packages in ml application
from typing import List
HYPEN_E_DOT ='-e .'
def get_requirements(file_path:str)->List[str]: 
    '''
    this function will return the list of requirements
    '''
    requiremnts=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        if HYPEN_E_DOT in requiremnts:
            requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
    name='mlproject',
    version='0.0.1',
    authors='esha',
    author_email='eshakundercs2004@gmail.com',
    packages=find_packages(),
    install_requirements=get_requirements('requirements.txt')

)