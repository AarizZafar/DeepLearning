import sys
from src.cnnClassifier import logging,CustomException
from cnnClassifier.utils.common import get_size,hello
from pathlib import Path

print(get_size(Path('research\\01_data_ingestion.ipynb')))
print(hello())

logging.info("TEST LOGIN")

# try: 
#     a = 1/0
# except Exception as ex:
#     logging.info("zero divisin exception ..........")
#     raise CustomException(ex,sys)