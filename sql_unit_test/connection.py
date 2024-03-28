from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import logging

from sql_unit_test.config import URI

logger = logging.getLogger(__name__)

from sql_unit_test.cli import report_missing_uri

def get_uri_from_env():
    logger.debug(f'URI: {URI}')
    return URI

def create_connection(uri):
    logger.info('Creating sqlalchemy connection object.')
    con = create_engine(uri)
    logger.info('Successfully created sqlalchemy connection object.')

    return con
