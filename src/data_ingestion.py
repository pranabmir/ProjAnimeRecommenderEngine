import os
import pandas as pd
from google.cloud import storage
from src.logger import get_logger
from src.custom_exception import CustomException
from config.path_config import *
from utils.common_functions import read_yaml,load_data

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self,config):
        self.config = config['data_ingestion']
        self.bucket_name = self.config['bucket_name']
        self.file_names = self.config['bucket_file_names']

    os.makedirs(RAW_DIR,exist_ok=True)
    logger.info("Starting Data Ingestion")

    def download_data_from_gcp(self):
        try:
            client = storage.Client.from_service_account_json(KEY_PATH)
            bucket = client.bucket(self.bucket_name)
            for i in self.file_names:
                file_path = os.path.join(RAW_DIR,i)
                if i== 'animelist.csv':
                    blob = bucket.blob(i)
                    blob.download_to_filename(file_path)
                    data = pd.read_csv(file_path,nrows = 5000000)
                    data.to_csv(file_path,index = False)
                    logger.info('large file detected, dowloading only 5MM rows')
                else:
                    blob = bucket.blob(i)
                    blob.download_to_filename(file_path)
                    logger.info(f"Downloading {i} file")
        except Exception as e:
            logger.error("Error while downloading Data")
            raise CustomException('Error while downloading data',e)
        
    def run(self):
        try:
            logger.info('Starting data ingestion process.....')
            self.download_data_from_gcp()
            logger.info('Data ingestion completed...')
        except Exception as e:
            logger.error(f'CustomExceptions: {str(e)}')
            raise CustomException('Error while data ingestion Process',e)
        finally:
            logger.info("data ingestion code exceution done")


if __name__=="__main__":
    data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()