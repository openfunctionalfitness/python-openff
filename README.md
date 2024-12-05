[![PyPI version](https://badge.fury.io/py/python-openff.svg)](https://badge.fury.io/py/python-openff)
[![PyPi downloads](https://img.shields.io/pypi/dm/python-openff)](https://img.shields.io/pypi/dm/python-openff)


# python-openff

## Usage

```py
import openff.transform as offt

y = offt.parse_cap("CAP +36")
# 36

y = offt.parse_time("02:52")
# 172 sec.

y = offt.parse_time("24:31.18")
# 1471.18 sec.

y = offt.parse_time("1:15:59")
# 4559 sec.

y = extrap_cap2sec("cap +150", 10, 200)
# 800 sec.
```


## Appendix

### Installation
The `python-openff` [git repo](http://github.com/openfunctionalfitness/python-openff) is available as [PyPi package](https://pypi.org/project/python-openff)

```sh
pip install python-openff
pip install git+ssh://git@github.com/openfunctionalfitness/python-openff.git
```

### Install a virtual environment

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
pip install -r requirements-dev.txt --no-cache-dir
```

(If your git repo is stored in a folder with whitespaces, then don't use the subfolder `.venv`. Use an absolute path without whitespaces.)

### Python commands

* Jupyter for the examples: `jupyter lab`
* Check syntax: `flake8 --ignore=F401 --exclude=$(grep -v '^#' .gitignore | xargs | sed -e 's/ /,/g')`
* Run Unit Tests: `PYTHONPATH=. pytest`

Publish

```sh
pandoc README.md --from markdown --to rst -s -o README.rst
python setup.py sdist 
twine upload -r pypi dist/*
```

### Clean up 

```sh
find . -type f -name "*.pyc" | xargs rm
find . -type d -name "__pycache__" | xargs rm -r
rm -r .pytest_cache
rm -r .venv
```


### Support
Please [open an issue](https://github.com/openfunctionalfitness/python-openff/issues/new) for support.


### Contributing
Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/openfunctionalfitness/python-openff/compare/).
