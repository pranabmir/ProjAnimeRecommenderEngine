import os
import pandas as pd
from src.custom_exception import CustomException
from src.logger import get_logger
import yaml

logger = get_logger(__name__)

def read_yaml(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found in given path")
        with open(file_path,'r') as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info('Successfully read yaml file')
            return config
    except Exception as e:
        logger.error("Error while reading yaml file")
        raise CustomException("Failed to read yaml file",e)

def load_data(path):
    try:
        logger.info('Loading Data')
        return pd.read_csv(path)
    except Exception as e:
        logger.error('Error while loading data {e}')
        raise CustomException('Failed to load data',e)