import os
import pandas as pd
import numpy as np
import joblib
from src.logger import get_logger
from src.custom_exception import CustomException
from config.path_config import *
import sys

logger = get_logger(__name__)

class DataProcessor():
    def __init__(self):
        self.input_file = ANIMELIST_CSV
        self.output_dir = PROCESSED_DIR

        self.rating_df = None
        self.anime_df = None
        self.x_train_array = None
        self.y_train_array = None
        self.y_train = None
        self.y_test = None

        self.user2user_encoded = {}
        self.user2user_decoded = {}
        self.anime2anime_encoded = {}
        self.anime2anime_decoded = {}

        os.makedirs(self.output_dir,exist_ok=True)
        logger.info('DataProcessing Initialized')

    def load_data(self):
        try:
            usecols = ["user_id","anime_id","rating"]
            self.rating_df = pd.read_csv(self.input_file,low_memory=True,usecols=usecols)
            logger.info("Data loaded successfully")
        except Exception as e:
            raise CustomException("Failed to load data",e)
    
    def filter_users(self,min_rating = 400):
        try:
            n_ratings = self.rating_df['user_id'].value_counts()
            self.rating_df = self.rating_df[self.rating_df['user_id'].isin(n_ratings[n_ratings>400].index)].copy()
            logger.info("Data filter successfully")
        except Exception as e:
            raise CustomException("Failed to filter data",e)
        
    def scale_rating(self):
        try:
            min_rating = min(self.rating_df.rating)
            max_rating = max(self.rating_df.rating)
            self.rating_df['rating'] = self.rating_df['rating'].apply(lambda x:(x-min_rating)/(max_rating-min_rating)).values.astype(np.float64)
            logger.info('Data scaled successfully')
        except Exception as e:
            raise CustomException('Failed to scale data',e)
        
    def encode_data(self):
        try:
            #user encoding
            user_id = self.rating_df['user_id'].unique().tolist()
            self.user2user_encoded = {x:i for i,x in enumerate(user_id)}
            self.user2user_decoded = {i:x for i,x in enumerate(user_id)}
            self.rating_df['user'] = self.rating_df['user_id'].map(self.user2user_encoded)
            logger.info("User encoded successfully")

            #anime encoding
            anime_ids = self.rating_df["anime_id"].unique().tolist()
            self.anime2anime_encoded = {x : i for i , x in enumerate(anime_ids)}
            self.anime2anime_decoded = {i : x for i , x in enumerate(anime_ids)}
            self.rating_df["anime"] = self.rating_df["anime_id"].map(self.anime2anime_encoded)
            logger.info('Anime encoded successfully')
        except Exception as e:
            raise CustomException('Failed to encode data',e)
        
    def split_data(self,test_size = 1000,random_state = 42):
        try:
            self.rating_df = self.rating_df.sample(frac=1,random_state=random_state).reset_index(drop=True)
            x = self.rating_df[['user','anime']]
            y = self.rating_df[['rating']]
            split_index = self.rating_df.shape[0]-test_size
            x_train,x_test,y_train,y_test = (x[:split_index],
                                            x[split_index:],
                                            y[:split_index],
                                            y[split_index:])
            self.x_train_array = [x_train.loc[:,'user'].to_numpy(),x_train.loc[:,'anime'].to_numpy()]
            self.x_test_array = [x_test.loc[:,'user'].to_numpy(),x_test.loc[:,'anime'].to_numpy()]
            logger.info('Data Splitting Successful')
        except Exception as e:
            raise CustomException("Data splitting failed",e)
    
    def save_artifacts(self):
        try:
            artifacts = {
                "user2userencoded":self.user2user_encoded,
                "user2userdecoded": self.user2user_decoded,
                "anime2anime_encoded": self.anime2anime_encoded,
                "anime2anime_decoded": self.anime2anime_decoded
            }
            for name, data  in artifacts.items():
                joblib.dump(data,os.path.join(self.output_dir,f"{name}.pkl"))
                logger.info(f"{name} saved successfull in the directory")

            joblib.dump(self.x_train_array,X_TRAIN_ARRAY)
            joblib.dump(self.x_test_array,X_TEST_ARRAY)
            joblib.dump(self.y_train,Y_TRAIN)
            joblib.dump(self.y_test,Y_TEST)
            self.rating_df.to_csv(RATING_DF,index=False)
            logger.info('Training and testing datasets save successfully')
        except Exception as e:
            raise CustomException("Failed while saving artifacts",e)
        
    def process_anime_data(self):
        try:
            self.anime_df = pd.read_csv(ANIME_CSV,low_memory = True)
            self.anime_df.replace('Unknown',np.nan)
            cols = ["MAL_ID","Name","Genres","sypnopsis"]
            self.synopsis_df = pd.read_csv(SYNONPSIS_CSV,usecols=cols)
            def getAnimeName(anime_id):
                try:
                    name = self.anime_df[self.anime_df.anime_id==anime_id].eng_version.values[0]
                    if name is np.nan:
                        name = self.anime_df[self.anime_df.anime_id==anime_id].Name.values[0]
                except:
                    print('Error')
                return name
            self.anime_df["anime_id"] = self.anime_df["MAL_ID"]
            self.anime_df["eng_version"] = self.anime_df["English name"]
            self.anime_df["eng_version"] = self.anime_df.anime_id.apply(lambda x:getAnimeName(x))
            self.anime_df.sort_values(by=["Score"],
                                inplace=True,
                                ascending=False,
                                kind="quicksort",
                                na_position="last")
            self.anime_df = self.anime_df[['anime_id','eng_version', 'Score', 'Genres','Episodes','Type','Premiered','Members']]
            self.anime_df.to_csv(ANIME_DF,index = False)
            self.synopsis_df.to_csv(SYNONPSIS_DF,index=False)
            logger.info('Anime and synopsis df save successfully')
        except Exception as e:
            raise CustomException("Failed to save Anime and Synopsis df",e)
    
    def run(self):
        try:
            self.load_data()
            self.filter_users()
            self.scale_rating()
            self.encode_data()
            self.split_data()
            self.save_artifacts()
            self.process_anime_data()
            logger.info('Data processing pipeline completed successfully')
        except Exception as e:
            logger.error(str(e))

if __name__=="__main__":
    data_processor = DataProcessor()
    data_processor.run()

