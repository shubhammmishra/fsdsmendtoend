from src.DimondPricePridiction.components.data_ingestion import DataIngestion
from src.DimondPricePridiction.components.data_transformation import DataTransformation
from src.DimondPricePridiction.components.model_trainer import ModelTrainer 
import pandas as pd
from src.DimondPricePridiction.exception import customexception
from src.DimondPricePridiction.logger import logging
import os
import sys

obj = DataIngestion()
train_data_path, test_data_path=obj.initiate_data_ingestion()

data_transformation=DataTransformation()
train_arr,test_arr= data_transformation.initialize_data_transformation(train_data_path,test_data_path)

print(train_arr)
print(test_arr)

model_trainer_obj= ModelTrainer()
model_trainer_obj.initiate_model_training(train_arr, test_arr)
