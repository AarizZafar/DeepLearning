import os
import sys
from box.exceptions import BoxValueError
import yaml 
from cnnClassifier import logger,CustomException 
import json 
import joblib 
from ensure import ensure_annotations
from box import ConfigBox 
from pathlib import Path 
from typing import Any 
import base64

@ensure_annotations
def read_yaml(path_to_yaml : Path) -> ConfigBox:
    '''
        reads yaml file and returns

        Args:
            path_to_yaml (str): path like input

        Raise:
            CustomException -> for any kind of exception 

        Return
            ConfigBox: ConfigBox type
    '''
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'YAML FILE {path_to_yaml} LOADED SUCCESSFULLY')
            return ConfigBox(content)
    except BoxValueError:
        raise CustomException('yaml file is empty',sys)
    except Exception as e:
        CustomException(e)

@ensure_annotations
def create_directory(path_to_directory : list, verbose=True):
    '''
        create list of directory 

        args:
            path_to_directory (list)   : list of path of directory
            ignore_log (bool,optional) : ignore if multiple dirs is to be created. Defaults to False
    '''
    for path in path_to_directory:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f'CREATED DIRECTORY AT : {path}')

@ensure_annotations
def save_json(path: Path, data: dict):
    '''
        save json data 

        args:
            path (Path) : path to json file
            data (dict) : data to be saved in json file
    '''
    with open(path,'w') as f:
        json.dump(data,f,indent=4) # (indent = 4) -> SPECIFIES THE NUMBER OF SPACES TO USE FOR EACH LEVEL OF INDENTATION IN JSON

    logger.info(f'JSON FILE SAVED AT : {path}')

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    '''
        loads json file data

        Args:
            path (Path) : Path to json file

        Returns:
            ConfigBox: data as class attributes insted of dict 
    '''
    with open(path) as f:
        content = json.load(path)

    logger.info(f'JSON FILE LOADED SUCCESSFULLY FROM THE PATH {path}')
    return ConfigBox(content)
        