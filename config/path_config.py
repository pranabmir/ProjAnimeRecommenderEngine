import os

#data ingestion paths
RAW_DIR = "artifacts/raw"
CONFIG_PATH = "config/config.yaml"
KEY_PATH = "gcp_key/aerial-day-470509-c5-a038d47b7460.json"

#data processing paths
PROCESSED_DIR = 'artifacts/processed'
ANIMELIST_CSV = 'artifacts/raw/animelist.csv'
ANIME_CSV = 'artifacts/raw/anime.csv'
SYNONPSIS_CSV = 'artifacts/raw/anime_with_synopsis.csv'

X_TRAIN_ARRAY = os.path.join(PROCESSED_DIR,'x_train_array.pkl')
X_TEST_ARRAY = os.path.join(PROCESSED_DIR,'x_test_array.pkl')
Y_TRAIN = os.path.join(PROCESSED_DIR,'y_train.pkl')
Y_TEST = os.path.join(PROCESSED_DIR,'y_test.pkl')

RATING_DF = os.path.join(PROCESSED_DIR,'rating_df.csv')
ANIME_DF = os.path.join(PROCESSED_DIR,'anime_df.csv')
SYNONPSIS_DF = os.path.join(PROCESSED_DIR,'synopsis_df.csv')