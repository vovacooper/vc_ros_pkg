import logging
import sys
import os
from os.path import basename

LOG_PATH = "/var/log/vc_ros_pkg/"


if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)

print(LOG_PATH + basename(sys.argv[0]) + ".log")

fh = logging.FileHandler(LOG_PATH + basename(sys.argv[0]) + ".log")
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s %(module)s.%(funcName)s -> %(lineno)d-%(levelname)s: %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s %(module)s.%(funcName)s -> %(lineno)d-%(levelname)s: %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)

