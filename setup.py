from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup
from setuptools import find_packages

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name = "mylib",
    version = "0.1.0",
    url="https://github.com/ryusei0228/linebot.git",
    packages = find_packages("src"),
    package_dir = {"": "src"},
    py_modules = [splitext(basename(path))[0] for path in glob("mylib/*.py")],
    include_package_data = True,
    zip_safe = False,
    install_requires = _requires_from_file("requirements.txt")
)