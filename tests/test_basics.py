# coding: utf-8
""" This module is the first test module"""
import pytest
import os
import os.path
import io
import shutil


# Reference: http://pythontesting.net/framework/pytest/pytest-session-scoped-fixtures/
# Reference: http://pythontesting.net/framework/pytest/pytest-fixtures/

class TestBasics(object):
    """
    This class could have been called anything and can have second class here
    """
    
    # @pytest.mark.parametrize("test_input,expected", [
    #     ("3+5", 8),
    #     ("2+4", 6),
    #     pytest.mark.xfail(("6*9", 42)),
    # ])
    
    # @pytest.fixture(scope="session", autouse=True)
    # scope=module
    # scope=class
    # scope=module
    # scope=function
    # Reference: http://doc.pytest.org/en/latest/fixture.html?highlight=scope
    
    def test_import_six(self):
        """ testing that importing a core package works """
        import six
        
    def test_import_bitprint(self):
        """ testing that I can import myself """
        import bitprint
    
    @pytest.mark.parametrize("input,expected", [
        ("2", []),
        ("abc", []),
        ("@@", []),
    ])
    def test_bin_rep_string_arr(self, input, expected):
        
        





