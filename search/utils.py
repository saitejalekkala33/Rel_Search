# import logging

# def setup_logging():
#     """Configure logging for the application."""
#     logging.basicConfig(
#         level=logging.INFO,
#         format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#         handlers=[logging.StreamHandler()],
#     )
#     return logging.getLogger(__name__)

import logging
import os

def setup_logging(log_file: str = "log.txt") -> logging.Logger:
    with open(log_file, 'w'):
        pass

    logger = logging.getLogger("rel_search_logger")
    logger.setLevel(logging.INFO)

    if logger.hasHandlers():
        logger.handlers.clear()

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
