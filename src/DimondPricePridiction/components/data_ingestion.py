import os,sys
import pandas as pd
import numpy as np
from src.DimondPricePridiction.logger import logging
from src.DimondPricePridiction.exception import customexception
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

class DataIngestionConfig:
    raw_data_path:str= os.path.join("artifacts","raw.csv")
    train_data_path:str= os.path.join("artifacts","train.csv")
    test_data_path:str= os.path.join("artifacts","test.csv") 



class DataIngestion:


    
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("data ingestion started")

        try:
            #data= str(Path(os.path.join(os.getcwd(),"data\gemstone.csv"))}
            #data= Path('C:\\Users\\DEELL\\Desktop\\fsdsmendtoend\\notebook\\data\\gemstone.csv')
            #data= pd.read_csv(data)
            #data= pd.read_csv(Path(os.path.join("notebook/data","gemstone.csv")))
            data= pd.read_csv(Path(os.path.join("C:\\Users\\DEELL\\Desktop\\files\\gemstone.csv")))
            #data= pd.read_csv(os.path.join(os.getcwd(),"data\\gemstone.csv"))
            logging.info(" i have read dataset as a df")
            
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok= True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info(" i have saved the raw dataset in artifact folder")


            logging.info(" i have performed train test split")
            
            train_data, test_data= train_test_split(data,test_size=0.25)
            logging.info(" train test split completed")

            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)
            
            logging.info("data ingestion part completed")
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            logging.info("exception during data ingestion steps")
            raise customexception(e,sys)