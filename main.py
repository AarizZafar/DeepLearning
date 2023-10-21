import sys
from src.cnnClassifier import logging,CustomException

logging.info("TEST LOGIN")

try: 
    a = 1/0
except Exception as ex:
    logging.info("zero divisin exception ..........")
    raise CustomException(ex,sys)