import python_module
import unittest


def test_basic_import():
    from python_module import sample

    assert "A" == "A", "something wrong, could not import the module"
