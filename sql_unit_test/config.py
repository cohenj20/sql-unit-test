from dotenv import load_dotenv
import os
import logging

from sql_unit_test.cli import report_missing_uri

logger = logging.getLogger(__name__)

TEST_FOLDER_PATH = '.'
LOG_LEVEL = 'WARN'

load_dotenv()

if os.getenv("TEST_FOLDER_PATH"):
    TEST_FOLDER_PATH = os.getenv("TEST_FOLDER_PATH")

if os.getenv("LOG_LEVEL"):
    LOG_LEVEL = os.getenv("LOG_LEVEL")

def config_check(uri, dir, filepath):
    if not uri:
        raise SystemExit(report_missing_uri())
    
    if not dir:
        logger.info("Option --dir was omitted; using current directory by default.")

    if not filepath:
        logger.info("Option --filepath was omitted; checking current directory by difault.")


