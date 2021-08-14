"""
Setup tools for Lyncs
"""

__version__ = "0.3.0"

from .version import *
from .data_files import *
from .description import *
from .classifiers import *
from .author import *
from .setuptools import *

try:
    from .cmake import *

    WITH_CMAKE = True
except ImportError:
    WITH_CMAKE = False

try:
    from .pylint import *

    WITH_PYLINT = True
except ImportError:
    WITH_PYLINT = False
