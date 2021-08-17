from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="EvtxReader",
    version="0.0.1",
    author="SpaSmALX",
    description="Python Module for parsing and reading Windows Evtx files",
    url="https://github.com/SpaSmALX/EvtxReader",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
)
