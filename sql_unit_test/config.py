from dotenv import load_dotenv
import os
import logging

from sql_unit_test.cli import report_missing_uri

logger = logging.getLogger(__name__)

TARGET_DIR = '.'
LOG_LEVEL = 'WARN'

load_dotenv()

if os.getenv("APP_ENV") == 'dev':
    URI='sqlite:///sample//test_database.db'
    TARGET_DIR='./sample/playlists'

    if os.getenv("LOG_LEVEL"):
        LOG_LEVEL = os.getenv("LOG_LEVEL")

else:
    if os.getenv("URI"):
        URI = os.getenv("URI")

    if os.getenv("TARGET_DIR"):
        TARGET_DIR = os.getenv("TARGET_DIR")

    if os.getenv("LOG_LEVEL"):
        LOG_LEVEL = os.getenv("LOG_LEVEL")

def config_check(uri, target_dir, filepath):
    logger.info('Checking config environment variables.')
    if not uri:
        logging.info("URI object does not exist.")
        raise SystemExit(report_missing_uri())
    
    if not target_dir:
        logger.info(f"Option --target_dir was omitted; defaulting to TARGET_DIR environment variable value.")

    if not filepath:
        logger.info("Option --filepath was omitted; defaulting to TARGET_DIR environment variable value.")

