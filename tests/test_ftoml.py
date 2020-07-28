import toml
import ftoml
import pytest
import sys
import os

# helper to load files named the same as the test-function
def _load_compare(func_name):
    d=os.path.dirname(os.path.realpath(__file__))
    assert ftoml.load(os.path.join(d,f"{func_name}.in.ftoml")) == toml.load(os.path.join(d,f"{func_name}.out.toml"))

# TBD: dynamically generate those from file listing
def test_simple_fstring():
    _load_compare(sys._getframe().f_code.co_name)

def test_recursive_variables():
    _load_compare(sys._getframe().f_code.co_name)

def test_inheritance():
    _load_compare(sys._getframe().f_code.co_name)

def test_defaults():
    _load_compare(sys._getframe().f_code.co_name)

def test_absolute_reference():
    _load_compare(sys._getframe().f_code.co_name)

def test_arrays():
    _load_compare(sys._getframe().f_code.co_name)

def test_leave_others():
    _load_compare(sys._getframe().f_code.co_name)

def test_reserved_words():
    _load_compare(sys._getframe().f_code.co_name)
