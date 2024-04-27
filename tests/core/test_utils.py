from ast import Not
import pytest

from sql_unit_test.core.utils import parse_filename


def test_parse_filename():
    proper_filename = 'test.sql'
    filename_no_filetype = 'test.string.sql'
    not_a_string = 12
    
    assert parse_filename(proper_filename) == 'test'
    assert parse_filename(filename_no_filetype) == 'test'
    
    with pytest.raises(Exception):
        parse_filename(not_a_string)