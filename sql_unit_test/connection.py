from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

from sql_unit_test.cli import report_missing_uri

def get_uri_from_env():
    load_dotenv()
    uri = os.getenv("URI")

    return uri

def create_connection(uri):
    return create_engine(uri)
