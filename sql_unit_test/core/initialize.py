import click
import colorama
from dotenv import load_dotenv
import logging
import yaml
import subprocess

from sql_unit_test.core.connection import create_connection
from sql_unit_test.cli.outputs import init_cli, report_file_count, report_test_start, report_test_result, report_successful_project_initialization
from sql_unit_test.core.logger import configure_logger
from sql_unit_test.core.directory_check import *
from sql_unit_test.core.run_test import read_sql_file, run_sql_unit_test

from sql_unit_test.core.config import config_check
from sql_unit_test.core.config_manager import retrieve_config_values

configure_logger()

logger = logging.getLogger(__name__)

URI, TARGET_DIR, LOG_LEVEL = retrieve_config_values()

@click.command()
def init():
    
    cwd = os.getcwd()

    config_dict = {
        'uri' : '',
        'target_dir' : '',
        'log_level' : 'WARN',
        'app_env' : ''
    }

    if not os.path.exists(cwd + '/.sql-unit-test'):
        os.mkdir('.sql-unit-test')
        os.mkdir(cwd + '/.sql-unit-test/runs')

        with open('sql-unit-test.yaml', 'w') as file:
            yaml.dump(config_dict, file)

        with open('.gitignore', 'w') as fp:
            fp.write("venv/\n.env\n**/__pycache__/\n.sql-unit-test\nsql-unit-test.yaml")

        init_cli()
        report_successful_project_initialization(cwd)
        
    else:
        SystemExit(print('This directory has already initialized as a sql-unit-test directory.'))

