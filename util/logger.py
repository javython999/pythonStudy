import logging

format = "%(asctime)s: %(message)s"

def debug(log_message):
    logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S")
    logging.debug(log_message)


def info(log_message):
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info(log_message)


def warning(log_message):
    logging.basicConfig(format=format, level=logging.WARNING, datefmt="%H:%M:%S")
    logging.warning(log_message)


def fatal(log_message):
    logging.basicConfig(format=format, level=logging.FATAL, datefmt="%H:%M:%S")
    logging.fatal(log_message)


def error(log_message):
    logging.basicConfig(format=format, level=logging.ERROR, datefmt="%H:%M:%S")
    logging.error(log_message)