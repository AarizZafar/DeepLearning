from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.evaluation import Evaluation
from cnnClassifier import logging,CustomException
import sys

STAGE_NAME = 'EVALUATION PIPELINE'

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()

if __name__ == '__main__':
    try:
        logging.info(f'*****************')
        logging.info(f'>>>>>>>>>>>> stage {STAGE_NAME} <<<<<<<<<<<<<<<<<')
        EVALobj = EvaluationPipeline()
        EVALobj.main()
        logging.info(f'>>>>>>>>>>>> {STAGE_NAME} <<<<<<<<<<<<<<\n\n X===================X')

    except Exception as e:
        logging.info(e)
        CustomException(e,sys)
        
