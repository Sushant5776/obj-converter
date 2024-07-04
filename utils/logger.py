import logging


def get_logger(name="API Logger", log_file="api.log"):
    """
    Creates a logger with a FileHandler and Formatter.

    Args:
        name (str, optional): The name of the logger. Defaults to "Background Remover".

    Returns:
        logging.Logger: The configured logger object.
    """

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler(log_file)
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s: %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger
