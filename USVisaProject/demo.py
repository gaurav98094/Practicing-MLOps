from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys
import os
print(os.getcwd())
logging.info("Welcome to our custom log")

try:
    a = 2/0
except Exception as e:
    raise USvisaException(e, sys)