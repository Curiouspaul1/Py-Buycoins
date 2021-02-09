from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='buycoins-sdk',
    packages=find_packages(include=['pycoins']),
    version='1.0',
    description='Python client library for BuyCoins Africa API',
    long_description=long_description
    author='Paul <paulcurious7@gmail.com>, Emmanuel Bashorun <>',
    license=’MIT’,
    url='https://github.com/Bashorun97/BuyCoins-Python-SDK',
    classifiers='Development Status :: 4 - Beta'
)