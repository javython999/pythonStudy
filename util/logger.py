import logging

format = "%(asctime)s %(levelname)s [%(name)s] - %(message)s"


def debug(log_message):
    logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%Y-%m-%d %H:%M:%S")
    logging.debug(log_message)


def info(log_message):
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S")
    logging.info(log_message)


def warning(log_message):
    logging.basicConfig(format=format, level=logging.WARNING, datefmt="%Y-%m-%d %H:%M:%S")
    logging.warning(log_message)


def fatal(log_message):
    logging.basicConfig(format=format, level=logging.FATAL, datefmt="%Y-%m-%d %H:%M:%S")
    logging.fatal(log_message)


def error(log_message):
    logging.basicConfig(format=format, level=logging.ERROR, datefmt="%Y-%m-%d %H:%M:%S")
    logging.error(log_message)