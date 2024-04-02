import click
import colorama

def init_cli():
    click.echo(f'=======================================================================================================================')
    click.echo(f'                                                  SQL Unit Test                                                        ')
    click.echo(f'=======================================================================================================================')
    click.echo(f'                                                                                                                       ')

def report_file_count(files_list):
    click.echo(f'                                                                                                                       ')
    click.echo(colorama.Fore.BLUE + f'                                                 Running {len(files_list)} test(s)                                      ')
    click.echo(f'                                                                                                                       ')
    
def report_test_start(filename, index=0):
    click.echo(colorama.Fore.WHITE + f'                 test {index + 1}: {filename}                                                  ')

def report_test_result(test_file_path: str, test_result_df):
    if test_result_df.empty:
        click.echo(colorama.Fore.GREEN + f'                    PASS                                       ')
    else:
        click.echo(colorama.Fore.RED + f'                    FAIL                                        ')
        click.echo(colorama.Fore.BLUE + f'                    run file: ./tests                           ')
        click.echo(colorama.Fore.BLUE + f'                    test file: {test_file_path}                 ')

def report_missing_uri():
    click.echo(colorama.Fore.RED + f'                    Error: No database URI was provided. Add one to the sql-unit-test.yaml file or pass the --uri option to sql-unit-test')

def report_invalid_uri(exception):
    click.echo(colorama.Fore.RED + f'                    Error: The database URI that was provided is not valid.\n                    Error msg from sqlalchemy: {exception}')
    click.echo(f'                                                                                                                       ')

def report_non_sql_filetype(filename):
    click.echo(colorama.Fore.RED + f'                    Error: {filename} is not a sql file.                                       ')
    click.echo(colorama.Fore.WHITE + f'                                                                                             ')

def report_test_sql_query_error(exception):
    click.echo(colorama.Fore.RED + f'                    Error: Issue running unit test sql query. \n                    Exception msg: {exception}                                       ')
    click.echo(colorama.Fore.WHITE + f'                                                                                             ')
