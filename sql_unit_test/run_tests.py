import pandas as pd

def read_sql_file(test_file_path):
    test_file = open(test_file_path, 'r')

    test_sql = test_file.read()

    return test_sql, test_file_path

def run_test(test_sql, con):
    test_result = pd.read_sql(test_sql, con)

    return test_result


