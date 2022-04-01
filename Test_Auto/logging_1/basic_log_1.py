import logging
import pytest

# logging.debug("Debug message")
logging.info("Info mes")
# logging.warning("Warnings")
# logging.error("Errors")
# logging.critical("Critical")

def test_logs():
    logging.debug("Debug message")
    logging.info("Info mes")
    logging.warning("Warnings")
    logging.error("Errors")
    logging.critical("Critical")
    #