"""
QTPYGU setup.py file
"""

from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\\n" + fh.read()

setup(
    name="QTPYGUI",
    version="{{VERSION_PLACEHOLDER}}",
    author="David Worboys",
    author_email="davidaworboys@gmail.com",
    description="A Simple Python Declarative User Interface Wrapper Around Pyside6 ",
    url="https://github.com/David-Worboys/QTPYGUI",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        "appdirs",
        "attrs",
        "certifi",
        "charset-normalizer",
        "fs",
        "idna",
        "Naked",
        "netifaces",
        "numpy",
        "pathvalidate",
        "platformdirs",
        "pycryptodome" "PySide6",
        "PySide6_Addons",
        "PySide6_Essentials",
        "python-dateutil",
        "PyYAML",
        "requests",
        "shellescape",
        "shiboken6",
        "six",
        "titlecase",
        "urllib3",
    ],
    keywords=["pypi", "cicd", "python"],
    classifiers=[
        "Development Status :: Beta 1 Release",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
        "Operating System :: Unix",
    ],
)
