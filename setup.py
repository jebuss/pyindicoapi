from setuptools import setup, find_packages

setup(
    name="pyIndicoApi",
    version="0.1.0",
    description="A Python client for the CERN Indico API",
    author="Jens Buss",
    author_email="jens.buss@tu-dortmund.de",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.7",
    url="https://github.com/jebuss/pyIndicoapi",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)