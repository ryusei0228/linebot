from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup
from setuptools import find_packages

setuptools.setup(
    name = "mylib",
    version = "0.1.0",
    url="https://github.com/ryusei0228/linebot.git",
    download_url = "https://github.com/ryusei0228/linebot.git",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3.8.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
