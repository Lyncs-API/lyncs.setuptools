# Setup tools for Lyncs and CMake support

[![python](https://img.shields.io/pypi/pyversions/lyncs_setuptools.svg?logo=python&logoColor=white)](https://pypi.org/project/lyncs_setuptools/)
[![pypi](https://img.shields.io/pypi/v/lyncs_setuptools.svg?logo=python&logoColor=white)](https://pypi.org/project/lyncs_setuptools/)
[![license](https://img.shields.io/github/license/Lyncs-API/lyncs.setuptools?logo=github&logoColor=white)](https://github.com/Lyncs-API/lyncs.setuptools/blob/master/LICENSE)
[![build & test](https://img.shields.io/github/workflow/status/Lyncs-API/lyncs.setuptools/build%20&%20test?logo=github&logoColor=white)](https://github.com/Lyncs-API/lyncs.setuptools/actions)
[![codecov](https://img.shields.io/codecov/c/github/Lyncs-API/lyncs.setuptools?logo=codecov&logoColor=white)](https://codecov.io/gh/Lyncs-API/lyncs.setuptools)
[![pylint](https://img.shields.io/badge/pylint%20score-9.8%2F10-green?logo=python&logoColor=white)](http://pylint.pycqa.org/)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg?logo=codefactor&logoColor=white)](https://github.com/ambv/black)

In this package we provide a wrap around the standard setutools to be used in Lyncs projects.

## Installation

The package can be installed via `pip`:

```
pip install [--user] lyncs_setuptools
```

## Usage

Lyncs setuptools automizes the deduction of many setup.py options.

Its use in a `setup.py` file is the following

```python
from lyncs_setuptools import setup

setup(package_name, **kwargs)
```

where package_name is the name of the package and kwargs are a list of arguments additional or replacement of the one automatically deduced.

**NOTE:** For seeing the list of the automatically deduced options, run `lyncs_setuptools` from command line in the directory containing the file `setup.py`.

**NOTE:** for correctly installing your package via `pip`, you need to add a file named `pyproject.toml` with the following content.

```
[build-system]
requires = ["lyncs_setuptools", ]
```

Add `"cmake"` to the requirements list if you use the following CMake extension.

### CMakeExension

Based on https://www.benjack.io/2017/06/12/python-cpp-tests.html we provide a CMakeExtension to support CMake files.

A CMakeExtension can be added as follow

```python
from lyncs_setuptools import setup, CMakeExtension

ext = CMakeExtension(install_dir, source_dir='.', cmake_args=[])

setup(package_name, ext_modules = [ext])
```

## Setup parameters

The following are the parameter used by default in the setup

### Automatically deduced:

- **author**: (git) author of first commit
- **author_email:** (git) email of author of first commit
- **version:** (python) value of `__version__` defined in `__init__.py` 
- **url:** (git) remote address of origin
- **project_urls:** (git) defines Source, Documentation, Tracker, Download
- **description:** (file) first title of the README
- **long_description:** (file) content of the README
- **long_description_content_type:** (file) type of README (md/rst)
- **classifiers:** (partially) 
  - ***version***: *Planning* (<0.1.0), *Pre-Alpha* (<0.3.0), *Alpha* (<0.6.0), *Beta* (<1.0.0), *Production/Stable* (<3.0.0), *Mature* (>=3.0.0)
  - ***license***: TODO
- **keywords:** (>3 chars or capital) words in description

### Defaulted values

- **classifiers:** python 3-only, science
