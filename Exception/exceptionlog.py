import logging

logging.basicConfig(filename="mylog.log", level=logging.ERROR)
logging.critical("Critical")
logging.error("Error")
logging.info("Info")
logging.debug("Debug")
