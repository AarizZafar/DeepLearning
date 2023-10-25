import sys
from cnnClassifier import logging,CustomException
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = 'DATA INGESTION STAGE'

try:
    logging.info(f'>>>>>>>>>>>>> STAGE {STAGE_NAME} STARTED <<<<<<<<<<<<<<<<<<<<')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()                       # THERE IS A main METHOD IN THE DataIngestionTrainingPipeline 
    logging.info(f'>>>>>>>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<<<<<<<<<<<<<<<')
except Exception as e:
    CustomException(e,sys)