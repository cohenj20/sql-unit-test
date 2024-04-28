import pytest
import os
import glob

from sql_unit_test.core.utils import parse_filename, clean_run_dir
from sql_unit_test.core.config import locate_root_dir



def test_parse_filename():
    proper_filename = 'test.sql'
    filename_no_filetype = 'test.string.sql'
    not_a_string = 12
    
    assert parse_filename(proper_filename) == 'test'
    assert parse_filename(filename_no_filetype) == 'test'
    
    with pytest.raises(Exception):
        parse_filename(not_a_string)


def test_clean_run_dir():
    root = locate_root_dir()
    os.chdir(root)

    open('./.sql-unit-test/runs/test_file.json', 'w')

    failure_files = clean_run_dir()

    assert failure_files == ['./.sql-unit-test/runs\\test_file.json']

    assert glob.glob(f'./.sql-unit-test/runs/*') == []
