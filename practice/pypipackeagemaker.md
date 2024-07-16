# My Python Package

This guide will walk you through the steps to create a basic Python package.

## Table of Contents

1. [Introduction](#introduction)
2. [Folder Structure](#folder-structure)
4. [Setting Up](#setting-up)
5. [Creating setup.py](#creating-setuppy)
6. [Conclusion](#conclusion)

## Introduction

A Python package is a way of organizing related modules in a single directory. This guide will show you how to create a simple Python package.

## Folder Structure

Your project folder should look like this:

```plaintext
my_python_package/
│
├── my_python_package/
│   ├── __init__.py
│   └── module.py
|
├── setup.py
├── LICENSE
├── README.md
└── .gitignore
```
## Setting Up
First install the following package and make sure that they are availabel to use with you
```bash
pip install twine setuptools wheel
```
## Making of MANIFEST.in
```bash
include README.md
include LICENSE
```
## Making of LICENSE
```bash
MIT License

Copyright (c) 2024 Streamlit-socialmedia

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
## Setting Up setup.py 
### Basic template of setup.py
```bash
from setuptools import setup, find_packages

setup(
    name='Project name',
    version='version',
    packages=find_packages(),
    author='your name',
    author_email='your email',
    description='discription of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='git repo url',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
```
### Advanced template of setup.py
```bash
from setuptools import setup, find_packages

setup(
    name="my_python_package",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple Python package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_python_package",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        # Add your package dependencies here
        # e.g., "numpy>=1.18.0", "requests>=2.23.0"
    ],
    extras_require={
        "dev": [
            "check-manifest",
            "flake8",
            "pytest",
            "sphinx",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",  # Adjust as appropriate
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "my_command=my_python_package.module:main",
        ],
    },
    include_package_data=True,
    package_data={
        # If there are data files included in your packages that need to be installed
        "": ["*.txt", "*.rst"],
        "my_python_package": ["data/*.dat"],
    },
    project_urls={
        "Bug Reports": "https://github.com/yourusername/my_python_package/issues",
        "Source": "https://github.com/yourusername/my_python_package/",
    },
)

```

## Making of dist 
```bash
python setup.py sdist bdist_wheel
```
## Uploading to pypi 
```bash
twine upload dist/*
```
## Conclusion
You have successfully created and uploaded a basic Python package! From here, you can expand your package by adding more modules, writing more tests, and improving the documentation.

For more information, refer to the Python Packaging Documentation.