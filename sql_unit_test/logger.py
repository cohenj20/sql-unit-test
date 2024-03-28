
import logging
import colorama

from sql_unit_test.config import LOG_LEVEL

def configure_logger():
    logging.basicConfig(
        level=LOG_LEVEL,
        format=colorama.Fore.CYAN   + "%(asctime)s [%(levelname)s] %(name)s: %(message)s" + colorama.Fore.WHITE,
        handlers=[
            logging.StreamHandler()
        ]
    )




