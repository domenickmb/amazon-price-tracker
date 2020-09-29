import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
my_format = logging.Formatter(
        '%(asctime)s [%(name)s] %(levelname)s: %(message)s',
        datefmt="%Y-%m-%d %H:%M:%S")

my_handler = logging.StreamHandler()
my_handler.setFormatter(my_format)
logger.addHandler(my_handler)
