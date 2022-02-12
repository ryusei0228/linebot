from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup
from setuptools import find_packages

INSTALL_REQUIRES = [
    "transformers == 2.8.0",
]

setuptools.setup(
    name = "mylib",
    version = "0.1.0",
    url="https://github.com/ryusei0228/linebot.git",
    download_url = "https://github.com/ryusei0228/linebot.git",
    include_package_data = True,
    zip_safe = False,
    install_requires = INSTALL_REQUIRES,
)
