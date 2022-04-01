import logging

logger = logging.getLogger("Selinium-pytest")
logger.setLevel(logging.INFO)

handler_warn = logging.FileHandler("my_app.log")
handler_warn.setLevel(logging.WARNING)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s -%(message)s")
handler_warn.setFormatter(formatter)
logger.addHandler(handler_warn)

logger.info("Test starts")
logger.warning("THis is a warning")
