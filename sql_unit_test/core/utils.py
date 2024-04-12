import logging

logger = logging.getLogger(__name__)

def parse_filename(filename):
    
    logger.debug(f'Passed filename: {filename}')
    logger.info("Parsing filename")
    parsed_filename = filename.split('.')[0]

    logger.debug(f'Parsed filename: {parsed_filename}')
    logger.info(f'Successfully parsed filename.')  

    return parsed_filename