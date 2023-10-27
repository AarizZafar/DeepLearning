import sys
from cnnClassifier import logging,CustomException
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = 'DATA INGESTION STAGE'

try:
    logging.info(f'>>>>>>>>>>>>> STAGE {STAGE_NAME} STARTED <<<<<<<<<<<<<<<<<<<<')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()                       # THERE IS A main METHOD IN THE DataIngestionTrainingPipeline 
    logging.info(f'>>>>>>>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<<<<<<<<<<<<<<<')
except Exception as e:
    CustomException(e,sys)


STAGE_NAME = 'PREPARING BASE MODEL'

try:
    logging.info(f'*************')
    logging.info(f'>>>>>>>> STAGE {STAGE_NAME} STARTED <<<<<<<<<<')
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logging.info(f'>>>>>>>>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<<<<<<<<<<< \n\n x============x')
except Exception as e:
        CustomException(e,sys)

