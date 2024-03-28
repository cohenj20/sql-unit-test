import click
import colorama
from dotenv import load_dotenv
import logging

from sql_unit_test.connection import get_uri_from_env, create_connection
from sql_unit_test.cli import init_cli, report_file_count, report_test_start, report_test_result
from sql_unit_test.logger import configure_logger
from sql_unit_test.directory_check import *
from sql_unit_test.run_tests import read_sql_file, run_test

from sql_unit_test.config import TEST_FOLDER_PATH, config_check

configure_logger()

logger = logging.getLogger(__name__)

logger.info(f'Configured logger with LEVEL= ')

colorama.init()

@click.command()
@click.option('--uri', help='A sqlalchemy URI that will override the URI provided in .env.')
@click.option('--dir', help='The directory in which to run sql-unit-test. Default is the current directory from which the sql-unit-test command is run.')
@click.option('--filepath', help='A path to a single sql unit test file.')
def main(uri, dir, filepath):
    init_cli()


    if not uri:
        uri = get_uri_from_env()

    config_check(uri, dir, filepath)


    if not filepath:
        files_list = check_directory(TEST_FOLDER_PATH)

        report_file_count(files_list)

        for i, f in enumerate(files_list):

            report_test_start(index=i, filename=f)
            
            test_sql, test_file_path = read_sql_file(test_file_path=TEST_FOLDER_PATH + '/' + f)

            con = create_connection(uri)

            test_result_df = run_test(test_sql=test_sql, con=con)

            report_test_result(test_file_path=test_file_path, test_result_df=test_result_df)
    
    else:
        files_list = [filepath]

        report_file_count(files_list)

        report_test_start(filename=filepath)
            
        test_sql, test_file_path = read_sql_file(test_file_path=filepath)

        con = create_connection(uri)

        test_result_df = run_test(test_sql=test_sql, con=con)

        report_test_result(test_file_path=test_file_path, test_result_df=test_result_df)

            
if __name__ == "__main__":
    main()
