import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y:%H:%M:%S',
    level=logging.DEBUG,
    filename='logs.txt')

logger = logging.getLogger('my_app')
logger.error("Error")

another_logger = logging.getLogger('my_app.database')  # gets a child logger called 'database' of 'my_app'
another_logger.error("Error")