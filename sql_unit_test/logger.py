
import logging
import logging.config

from sql_unit_test.config import LOG_LEVEL

LOGGING_CONFIG = { 
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': { 
        'standard': { 
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': { 
        'console': { 
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        }, 
    },
    'loggers': { 
        '__main__': {  # if __name__ == '__main__'
            'handlers': ['console'],
            'level': LOG_LEVEL,
            'propagate': True
        }, 
        'directory_check': {
            'handlers': ['console'],
            'level': LOG_LEVEL,
            'propagate': True
        },
        'config': {
            'handlers': ['console'],
            'level': LOG_LEVEL,
            'propagate': True
        },
    } 
}



