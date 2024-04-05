import pandas as pd
import logging
import colorama
import time

from sql_unit_test.cli.outputs import report_test_sql_query_error

logger = logging.getLogger(__name__)

def read_sql_file(test_file_path):
    logger.info('Opening sql unit test file.')

    test_file = open(test_file_path, 'r')

    logger.debug(f'Test file object: {test_file}')
    logger.info('Successfully opened sql unit test file.')

    logger.info('Reading sql unit test file to variable.')
    test_sql = test_file.read()
    logger.debug(f'Test file contents: \n{colorama.Fore.WHITE}{test_sql}{colorama.Fore.CYAN}')
    logger.info('Successfully Read sql unit test file to variable.')



    return test_sql, test_file_path

def run_sql_unit_test(test_sql, con):
    logger.info('Running sql test query.')
    start_time = time.time()
    try:

        test_result = pd.read_sql(test_sql, con)
        test_duration = round(time.time() - start_time, 2) 

    
    except Exception as E:
        raise SystemExit(report_test_sql_query_error(E))

    logger.debug(f'Test result: \n{colorama.Fore.WHITE}{test_result}{colorama.Fore.CYAN}')
    logger.info('Successfully ran sql test query.')

    return test_result, test_duration

