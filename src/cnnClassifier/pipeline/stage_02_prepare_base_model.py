from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier.utils.common import logging,CustomException
import sys

STAGE_NAME = 'prepare base model'

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == '__main__':
    try:
        logging.info(f'*************')
        logging.info(f'>>>>>>>> STAGE {STAGE_NAME} STARTED <<<<<<<<<<')
        prepare_base_model = PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()
        logging.info(f'>>>>>>>>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<<<<<<<<<<< \n\n x============x')
    except Exception as e:
        CustomException(e,sys)