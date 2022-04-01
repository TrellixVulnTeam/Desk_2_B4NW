import logging
import pytest

logger = logging.getLogger()

logger1=logging.getLogger("logger1")
logger1.setLevel(logging.INFO)

#Create a filehandler to write to file
fh = logging.FileHandler("fh_log.log")
# Create stream for console output
ch = logging.StreamHandler()

formatter=logging.Formatter("%(asctime)s - %(name)s %(filename)s- %(levelname)s - %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger1.addHandler(fh)
logger1.addHandler(ch)

logger1.warning("warn message 3")
logger1.info("info message 3")
logger1.error("error message 3")

#
# 2022-03-11 17:45:40,073 - logger1 - WARNING - warn message 1
# 2022-03-11 17:45:40,073 - logger1 - INFO - info message 1
# 2022-03-11 17:45:40,073 - logger1 - ERROR - error message 1
    #