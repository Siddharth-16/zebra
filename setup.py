from setuptools import setup, find_packages

VERSION = '0.1.0' 
DESCRIPTION = 'My first Python package'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="zebras", 
        version=VERSION,
        author="Harsh, Abdullah & Siddharth",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['pandas', 'numpy', 'scikit-learn'], 
)