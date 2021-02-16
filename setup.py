from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='py-buycoins',
    packages=find_packages(),
    version='0.1.0',
    description='Python client library for BuyCoins Africa API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Paul <paulcurious7@gmail.com>, Emmanuel Bashorun <bashorun.emma@gmail.com>',
    url='https://github.com/Bashorun97/BuyCoins-Python-SDK',
    classifiers=[
        # Project Maturity
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        "Operating System :: OS Independent",

        # License
        'License :: OSI Approved :: MIT License',

        # Python versions Support
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3'
)
