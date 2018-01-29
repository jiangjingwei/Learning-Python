import logging

logger = logging.getLogger('access')

logger.setLevel(logging.INFO)

fh = logging.FileHandler('access.log')
ch = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

if __name__ == '__main__':

    logger.info('test log')