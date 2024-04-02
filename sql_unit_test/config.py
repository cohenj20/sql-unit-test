from dotenv import load_dotenv
import os
import logging
import yaml
import time

from sql_unit_test.cli import report_missing_uri

logger = logging.getLogger(__name__)

TARGET_DIR = '.'
LOG_LEVEL = 'WARN'
URI = ''

def config_check(uri, target_dir, filepath):
    logger.info('Checking config environment variables.')
    if not uri:
        logging.info("URI object does not exist.")
        raise SystemExit(report_missing_uri())
    
    if not target_dir:
        logger.info(f"Option --target_dir was omitted; defaulting to TARGET_DIR environment variable value.")

    if not filepath:
        logger.info("Option --filepath was omitted; defaulting to TARGET_DIR environment variable value.")

def locate_root_dir():
    cwd = os.getcwd()
    timeout = time.time() + 2
    while True:
        if 'sql-unit-test.yaml' in os.listdir('.'):
            root = os.getcwd()

            os.chdir(cwd)
            
            return root
            break

        if time.time() > timeout:
            os.chdir(cwd)
            break

        else:
            os.chdir('..')
    
def parse_config_yaml(path):
    with open(path) as stream:
            try:
                data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                logger.warning(exc)
    
    app_env = data['app_env']
    uri = data['uri']
    target_dir = data['target_dir']
    log_level = data['log_level']

    return app_env, uri, target_dir, log_level



if locate_root_dir() is not None:

    yaml_path = locate_root_dir() + "\sql-unit-test.yaml"

    app_env, uri, target_dir, log_level = parse_config_yaml(yaml_path)

    if app_env == 'dev':
        URI='sqlite:///sample//test_database.db'
        TARGET_DIR='./sample/playlists'

        if log_level:
            LOG_LEVEL = log_level

    else:
        if uri:
            URI = uri

        if target_dir:
            TARGET_DIR = target_dir

        if log_level:
            LOG_LEVEL = log_level


