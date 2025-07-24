# setup.py
import sys
from setuptools import setup

# Add Python version check
PY_310_OR_HIGHER = sys.version_info >= (3, 10)

setup(
    name="PyJSONCanvas",
    version="1.0.2",
    description="A simple library for working with JSON Canvas (previously known as Obsidian Canvas) files.",
    author="Chaitanya Sharma",
    url="https://github.com/CheeksTheGeek/PyJSONCanvas",
    license="MIT",
    py_modules=["pyjsoncanvas"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.9",  # Specify minimum Python version
    # Add classifiers to indicate supported Python versions
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],
)
