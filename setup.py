from setuptools import setup,find_packages
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name = 'Anime recommender',
    version = '0.1',
    author = 'pranabmir',
    packages=find_packages(),
    install_requires= requirements
)