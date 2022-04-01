import logging
import pytest

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(filename)s [line:%(lineno)s] %(levelname)s %(message)s ",
                    datefmt="%a %m %d %Y %H:%M:%S",
                    # filename="C:\\Users\jsun\Documents\Desk_2\Test_Auto\logging_1\\test.log",
                    filename="test1.log",
                    filemode="a+")
logging.debug("Debug message")
logging.info("Info mes")
logging.warning("Warnings")
logging.error("Errors")
logging.critical("Critical")

def test_logs():
    logging.debug("Debug message")
    logging.info("Info mes")
    logging.warning("Warnings")
    logging.error("Errors")
    logging.critical("Critical")
    #