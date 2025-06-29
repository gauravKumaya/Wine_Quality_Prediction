import os
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlProject.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    # We can do any kind of transformation here
    
    # In this we are doing only train test split
    
    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)
        train, test = train_test_split(data)
        
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        
        logger.info("Splitted into trainig and testing sets")
        logger.info(f"training data shape: {train.shape}")
        logger.info(f"testing data shape: {test.shape}")
        
        print(train.shape)
        print(test.shape) 