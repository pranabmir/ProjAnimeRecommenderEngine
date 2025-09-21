from utils.common_functions import *
from config.path_config import *
from src.data_processing import DataProcessor
from src.model_training import ModelTraining

if __name__=="__main__":
    data_processor = DataProcessor()
    data_processor.run()
    model_trainer = ModelTraining()
    model_trainer.train_model()