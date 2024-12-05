import setuptools
import os


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as fp:
        s = fp.read()
    return s


def get_version(path):
    with open(path, "r") as fp:
        lines = fp.read()
    for line in lines.split("\n"):
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


setuptools.setup(
    name='python-openff',
    version=get_version("python_openff/__init__.py"),
    description='utility functions to process results of functional fitness competitions',
    long_description=read('README.rst'),
    url='http://github.com/openfunctionalfitness/python-openff',
    author='Ulf Hamster',
    author_email='554c46@gmail.com',
    license='Apache License 2.0',
    packages=['openff'],
    install_requires=[
        "numpy>=1,<2",
        "pandas>=2,<3",
        "openpyxl>=3,<4",
        "scipy>=1,<2",
        "unidecode>=1,<2"
    ],
    python_requires='>=3.7',
    zip_safe=True
)
