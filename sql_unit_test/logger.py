
import logging
import colorama

from sql_unit_test.config import LOG_LEVEL

logger = logging.getLogger(__name__)

def configure_logger():
    logger.info('Configuring logger.')
    logging.basicConfig(
        level=LOG_LEVEL,
        format=colorama.Fore.CYAN   + "%(asctime)s [%(levelname)s] %(name)s: %(message)s" + colorama.Fore.WHITE,
        handlers=[
            logging.StreamHandler()
        ]
    )

    logger.info('Successfully configured logger.')
    logger.debug(f'Log level set to {LOG_LEVEL}')





