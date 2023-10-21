import os
import sys 
import logging
from datetime import datetime

# PYTHON ONLY KNOWS THE DIRECTORY WHERE I RAN THE SCRIPT NOT THE DIRECTORY OF THE SCRIPT ITSELF 
# THIS IS ....\proj1
# NOT ....\proj1\src\cnnClassifier

logs_path = os.path.join(os.getcwd(),'logs')
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log")

logging.basicConfig(
    format = '[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level    = logging.INFO,
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),       # THE LOGGING OUTPUT WILL BE SENT TO A FILE 
        logging.StreamHandler(sys.stdout)         # ALSO WILL BE PRINTED ON THE CONSOLE
    ]
)

logger = logging.getLogger("LOGGIN HAS STARTED")

if __name__ == '__main__':
    logging.info("LOGGING HAS STARTED")
    

#<<<<<<<<<<<<<<<<<< CUSTOM EXCEPTION HANDLING >>>>>>>>>>>>>>>>>>>>>>>

def error_message_detail(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info()               
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "error occured in python \nscript name [{0}] \nline number [{1}] \nerror message [{2}]".format(
                                                                                                                    file_name,
                                                                                                                    exc_tb.tb_lineno,
                                                                                                                    str(error)
                                                                                                                )
    return error_message
    
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail)
    
    def __str__(self) -> str:
        return self.error_message
    
# Testing the custam exception 
# try: 
#     a = 1/0
# except Exception as ex:
#     logging.info("zero divisin exception ..........")
#     raise CustomException(ex,sys)



    
