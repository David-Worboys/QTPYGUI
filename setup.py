"""
QTPYGU setup.py file
"""

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = [line.strip() for line in f.readlines()]

setup(
    name="QTPYGUI",
    version="{{VERSION_PLACEHOLDER}}",
    author="David Worboys",
    author_email="davidaworboys@gmail.com",
    description="A Simple Python Declarative User Interface Wrapper Around Pyside6 ",
    url="https://github.com/David-Worboys/QTPYGUI",
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),
    packages=find_packages(),
    install_requires=install_requires,
    keywords=[
        "pypi",
        "cicd",
        "python",
        "pyside6",
        "ui",
        "gui",
        "qt",
        "qtpygui",
        "declarative",
        "wrapper",
        "user-interface",
        "qt-bindings",
        "python-qt",
        "gui-framework",
        "ui-library",
        "pyside6-wrapper",
    ],
    classifiers=[
        "Development Status :: Beta 1 Release",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: Unix",
    ],
)
