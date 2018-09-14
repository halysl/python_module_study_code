import logging


def get_logger():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s  %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        )
    _logger = logging.getLogger("collect-log")
    _logger.setLevel(logging.INFO)
    return _logger


logger = get_logger()


def func():
    for i in range(10000):
        logger.info(i)


func()
