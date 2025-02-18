import os
import sys
from pathlib import Path
import pandas as pd
import joblib

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from prediction_model.config import config

def load_dataset(file_name):
    filepath = os.path.join(config.DATAPATH,file_name)
    _data = pd.read_csv(filepath)
    return _data

#Serialization
def save_pipeline(pipeline_to_save):
    save_path = os.path.join(config.SAVE_MODEL_PATH,config.MODEL_NAME)
    joblib.dump(pipeline_to_save, save_path)
    print("Model has been saved under the name {config.MODEL_NAME}")

#deserialization
def load_pipeline(pipeline_to_load):
    save_path = os.path.join(config.SAVE_MODEL_PATH,config.MODEL_NAME)
    print(save_path)
    model_loaded = joblib.load(save_path)
    print("Model has been loaded")
    return model_loaded
