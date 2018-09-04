import logging


def get_logger():
    logging.basicConfig(filename='/home/light/Documents/qcollects.log',
                        level=logging.DEBUG,
                        mode="w",
                        format='%(asctime)s %(levelname)s  %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        )
    _logger = logging.getLogger("collect-log")
    _logger.setLevel(logging.INFO)
    return _logger


logger = get_logger()


def run():
    logger.info('aaa')
    logger.info('bbb')


def get_node_type():
    try:
        from get_info.info_cluster import get_nodetype
        node_type = get_nodetype()
    except Exception as e:
        logger.exception(e)
        print("can't get you node type")
        node_type = 'compute'
    return node_type


def main():
    run()


if __name__ == "__main__":
    main()