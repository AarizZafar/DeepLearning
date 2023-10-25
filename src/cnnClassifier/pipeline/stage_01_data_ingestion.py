from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logging,CustomException
import sys


STAGE_NAME = 'DATA INGESTION STAGE'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass 

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        logging.info(f'>>>>>>>>>> stage {STAGE_NAME} STARTED <<<<<<<<<<<<')
        dts1 = DataIngestionTrainingPipeline()
        dts1.main()
        logging.info(f">>>>>>>>>>>>>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<<<<<<<<<<<< \n\n x===============x")
    except Exception as e:
        CustomException(e,sys)