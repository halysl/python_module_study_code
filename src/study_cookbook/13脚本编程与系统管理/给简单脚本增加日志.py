# -*- config: utf-8 -*-

import logging


logging.basicConfig(
    filename="test.log",
    level=logging.ERROR,
    format='%(levelname)s:%(asctime)s:%(message)s')


def main():
    # Variables (to make the calls that follow work)
    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    # Example logging calls (insert into your program)
    logging.critical('Host %s unknown', hostname)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode=%r', filename, mode)
    logging.debug('Got here')

if __name__ == "__main__":
    main()
