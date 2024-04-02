import click
import colorama
from dotenv import load_dotenv
import logging
import yaml
import subprocess

from sql_unit_test.connection import create_connection
from sql_unit_test.cli import init_cli, report_file_count, report_test_start, report_test_result
from sql_unit_test.logger import configure_logger
from sql_unit_test.directory_check import *
from sql_unit_test.run_tests import read_sql_file, run_test

from sql_unit_test.config import URI, TARGET_DIR, config_check

configure_logger()

logger = logging.getLogger(__name__)

colorama.init()

@click.group
def my_commands():
    pass

@click.command()
@click.option('--uri', help='A sqlalchemy URI that will override the URI provided in .env.')
@click.option('--target_dir', help='The target directory in which run sql-unit-test. Default is the current directory from which the sql-unit-test command is run.')
@click.option('--filepath', help='A path to a single sql unit test file.')
def run(uri, target_dir, filepath):
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

@click.command()
def init():
    
    cwd = os.getcwd()

    print(cwd)

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
        
    else:
        SystemExit(print('This directory has already initialized as a sql-unit-test directory.'))


my_commands.add_command(run)
my_commands.add_command(init)

            
if __name__ == "__main__":
    my_commands()
