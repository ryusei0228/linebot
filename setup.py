from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup
from setuptools import find_packages

INSTALL_REQUIRES = [
    "torch == 1.10.2",
    "transformers == 2.8.0",
]

setup(
    name = "mylib",
    version = "0.1.0",
    url="https://github.com/ryusei0228/linebot.git",
    packages = find_packages("src"),
    package_dir = {"": "src"},
    download_url = "https://github.com/ryusei0228/linebot.git",
    py_modules = [splitext(basename(path))[0] for path in glob("mylib/*.py")],
    include_package_data = True,
    zip_safe = False,
    install_requires = INSTALL_REQUIRES,
)
