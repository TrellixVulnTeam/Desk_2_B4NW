import pytest
import logging
import time, traceback

log_basic = logging.getLogger('log_basic')
log_basic.setLevel(logging.WARNING)

fh = logging.FileHandler("pytest_logging_1.log")

fmt = "%(asctime)-16s - %(name)s %(filename)s- %(funcName)s [line:%(lineno)d] %(levelname)s - %(message)s"
datefmt = "%m/%d/%Y %H:%M:%S"
formatter = logging.Formatter(fmt, datefmt)
fh.setFormatter(formatter)
log_basic.addHandler(fh)

def test_basic():

    log_basic.info("This is info")
    log_basic.warning("this is warning")
    log_basic.error("this is error")
    log_basic.critical("this is critical")
    time.sleep(5)
    try:
        assert 1==2, "1!==2"
    except Exception as error:
        # log_basic.debug(traceback.format_exc())
        log_basic.exception(error)
        raise
    log_basic.error("OH, NO, it can be passed!")


def test_basic1():

    log_basic.info("This is info")
    log_basic.warning("this is warning")
    log_basic.error("this is error")
    log_basic.critical("this is critical")
    log_basic.warning("Starting a=1/0")
    a = 1/0
    log_basic.critical("reaching a=1/0")
    time.sleep(15)
    try:
        assert 1==1, "1!==2"
    except Exception as error:
        # log_basic.debug(traceback.format_exc())
        log_basic.exception(error)
        raise


def test_basic2():

    log_basic.info("This is info")
    log_basic.warning("this is warning")
    log_basic.error("this is error")
    log_basic.critical("this is critical")
    time.sleep(10)
    assert 1==2, "1!==2"
    time.sleep(5)