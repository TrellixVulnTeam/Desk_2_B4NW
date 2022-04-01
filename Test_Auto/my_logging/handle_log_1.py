# There are six log levels in Python; each level is associated
# with an integer that indicates the log severity:
#     NOTSET=0, DEBUG=10, INFO=20, WARN=30, ERROR=40, and CRITICAL=50.

import logging
class LogClass:

    def getLogger(self):
        loggerName = "Selenium_AuTo" #inspect.stack()[1][3]

        logger          = logging.getLogger(loggerName)
        fileHandler     = logging.FileHandler('selenium_auto.log')
        formatter       = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")

        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)

        return logger

##
import logging
import sys
from logging import Logger
from logging.handlers import TimedRotatingFileHandler


class MyLogger(Logger):
    def __init__(
        self,
        log_file=None,
        log_format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        *args,
        **kwargs
    ):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file

        Logger.__init__(self, *args, **kwargs)

        self.addHandler(self.get_console_handler())
        if log_file:
            self.addHandler(self.get_file_handler())

        # with this pattern, it's rarely necessary to propagate the| error up to parent
        self.propagate = False

    def get_console_handler(self):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.formatter)
        return console_handler

    def get_file_handler(self):
        file_handler = TimedRotatingFileHandler(self.log_file, when="midnight")
        file_handler.setFormatter(self.formatter)
        return file_handler


##-----------------------------------------------------------------------------------
import logging
import sys
from logging.handlers import TimedRotatingFileHandler

FORMATTER = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
LOG_FILE = "my_app.log"

def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    console_handler.setLevel(logging.WARNING)
    return console_handler

def get_file_handler():
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(FORMATTER)
    # file_handler.setLevel(logging.DEBUG)
    return file_handler

def get_logger(logger_name):
    logger = logging.getLogger(logger_name)



    # logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.setLevel(logging.DEBUG)  # better to have too much log than not enough
    # with this pattern, it's rarely necessary to propagate the error up to parent
    logger.propagate = False
    return logger

if "__main__" == __name__:
    logger = get_logger("Selenium-Test")
    logger.info("Beginng Test case 1")
    # 2021-08-17 14:49:22,220 - auto_test - INFO - Test starts
    # logger = get_logger(__file__)
    logger.warning(f"Auto Test stated")
    # 2021-08-17 15:07:56,716 - C:/Users/jsun/Documents/Desk_2/Test_Auto/handle_log.py - INFO - Auto Test stated