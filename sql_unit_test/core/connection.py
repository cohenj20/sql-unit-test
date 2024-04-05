from sqlalchemy import create_engine
from dotenv import load_dotenv
import logging

from sql_unit_test.core.config import locate_root_dir
from sql_unit_test.cli.outputs import report_invalid_uri

logger = logging.getLogger(__name__)

from sql_unit_test.cli import report_missing_uri

def create_connection(uri):
    logger.info('Creating sqlalchemy connection object.')
    try:
        con = create_engine(uri)
        logger.info('Successfully created sqlalchemy connection object.')

        return con


    except Exception as e:
        SystemExit(report_invalid_uri(e))

