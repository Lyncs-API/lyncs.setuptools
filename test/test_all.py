import io
import sys
import pytest
from contextlib import redirect_stdout, redirect_stderr
from lyncs_setuptools import (
    find_version,
    get_kwargs,
    print_keys,
    CMakeExtension,
    CMakeBuild,
)
from distutils.dist import Distribution
from lyncs_setuptools import __version__ as version


def capture_stdout_and_err(fnc, *args, **kwargs):
    "Captures stdout and stderr returned as two strings"
    out = io.StringIO()
    err = io.StringIO()
    with redirect_stdout(out):
        with redirect_stderr(err):
            fnc(*args, **kwargs)
    return out.getvalue(), err.getvalue()


def test_kwargs():
    assert find_version() == version

    out, err = capture_stdout_and_err(print_keys, [])
    assert 'version: "' in out
    assert not err

    out, err = capture_stdout_and_err(print_keys, ["author"])
    assert out == get_kwargs()["author"] + "\n"
    assert not err


def test_cmake():
    dist = Distribution()
    build = CMakeBuild(dist)
    build.extensions = [CMakeExtension("test", "test", ["-DMESSAGE=test1234"])]
    build.build_lib = "test"
    build.build_temp = "test/tmp"

    out, err = capture_stdout_and_err(build.run)
    assert "test1234" in out
    assert not err


try:
    from lyncs_setuptools.pylint import print_pylint_badge

    skip_pylint = False
except ModuleNotFoundError:
    skip_pylint = True


@pytest.mark.skipif(skip_pylint, reason="lyncs_setuptools[pylint] not installed")
def test_pylint():
    sys.argv.append(".")
    out, err = capture_stdout_and_err(print_pylint_badge, do_exit=False)
    assert "[![pylint](https://img.shields.io/badge" in out
    assert "Your code has been rated" in err
