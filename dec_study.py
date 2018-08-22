from functools import wraps

import logging

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


def log_info(func):
    def wrapper(*args, **kwargs):
        logging.info('%s is running...' % func.__name__)
        return func(*args, **kwargs)
    return wrapper


@log_info
def aaa():
    print('aaa')


aaa()