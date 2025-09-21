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

X_TRAIN_ARRAY = os.path.join('artifacts','processed','x_train_array.pkl')
X_TEST_ARRAY = os.path.join('artifacts','processed','x_test_array.pkl')
Y_TRAIN = os.path.join('artifacts','processed','y_train.pkl')
Y_TEST = os.path.join('artifacts','processed','y_test.pkl')
user2user_encoded_filename = "user2user_encoded"
user2user_decoded_filename = "user2user_decoded"
anime2anime_encoded_filename = "anime2anime_encoded"
anime2anime_decoded_filename = "anime2anime_decoded"

RATING_DF = os.path.join(PROCESSED_DIR,'rating_df.csv')
ANIME_DF = os.path.join(PROCESSED_DIR,'anime_df.csv')
SYNONPSIS_DF = os.path.join(PROCESSED_DIR,'synopsis_df.csv')

USER2USERENCODED = os.path.join('artifacts','processed',f"{user2user_encoded_filename}.pkl")
USER2USERDECODED = os.path.join('artifacts','processed',f"{user2user_decoded_filename}.pkl")
ANIME2ANIMEENCODED = os.path.join('artifacts','processed',f"{anime2anime_encoded_filename}.pkl")
ANIME2ANIMEDECODED = os.path.join('artifacts','processed',f"{anime2anime_decoded_filename}.pkl")


CHECKPOINT_FILE_PATH = "artifacts/model_checkpoint/weights.weights.h5"
MODEL_DIR = "artifacts/model"
WEIGHTS_DIR = "artifacts/weights"
MODEL_PATH = os.path.join(MODEL_DIR,"model.h5")
ANIME_WEIGHTS_PATH = os.path.join(WEIGHTS_DIR,"anime_weights.pkl")
USER_WEIGHTS_PATH = os.path.join(WEIGHTS_DIR,"user_weights.pkl")
