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

@click.command()
@click.option('--uri', help='A sqlalchemy URI that will override the URI provided in .env.')
@click.option('--target_dir', help='The target directory in which run sql-unit-test. Default is the current directory from which the sql-unit-test command is run.')
@click.option('--filepath', help='A path to a single sql unit test file.')
def run(uri, target_dir, filepath):
    """Execute sql unit tests, 'sql-unit-test run --help' for options."""

    logger = logging.getLogger(__name__)

    URI, TARGET_DIR, LOG_LEVEL = retrieve_config_values()

    init_cli()

    if not uri:
        uri = URI

    config_check(uri, target_dir, filepath)


    if not filepath:
        files_list = check_directory(TARGET_DIR)

        report_file_count(files_list)

        for i, f in enumerate(files_list):

            report_test_start(index=i, filename=f)
            
            test_sql, test_file_path = read_sql_file(test_file_path=TARGET_DIR + '/' + f)

            con = create_connection(uri)

            test_result_df, test_duration = run_sql_unit_test(test_sql=test_sql, con=con)

            report_test_result(test_file_path=test_file_path, test_result_df=test_result_df, test_duration=test_duration)
    
    else:
        files_list = [filepath]

        report_file_count(files_list)

        report_test_start(filename=filepath)
            
        test_sql, test_file_path = read_sql_file(test_file_path=filepath)

        con = create_connection(uri)

        test_result_df = run_test(test_sql=test_sql, con=con)

        report_test_result(test_file_path=test_file_path, test_result_df=test_result_df)
