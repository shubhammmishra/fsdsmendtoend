import pandas as pd
import numpy as np
import os
import sys

from src.DimondPricePridiction.exception import customexception
from src.DimondPricePridiction.logger import logging
from dataclasses import dataclass
from src.DimondPricePridiction.utils import save_object
from src.DimondPricePridiction.utils import evaluate_model

from sklearn.model_selection import LinearRegression, Ridge, Lasso, ElasticNet

class ModelTrainerConfig:
    trained_model_file_path= os.path.join("artifacts","model.pkl")

class ModelTrainer:
    
    def __init__(self):
        self.model_trainer_config= ModelTrainerConfig()


    def initiate_model_training(self):
        try:
            logging.info("spiltting Dependent and Independent variable from train and test data")
            X_train, y_train, X_test, y_test=(
                train_arrary[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models={
                'LinearRegression':LinearRegression(),
                'Lasso':Lasso(),
                'Ridge':Ridge(),
                'ElasticNet':ElasticNet()
            }
            model_report:dict= evaluate_model(X_train,y_train,X_test,y_test,models)
            print(model_report)
            print("\n=================================================\n")
            logging.info(f'Model Report:{model_report}')


            # to get best model from dictionary
            best_model_score= max(sorted(model_report.values()))

            best_model_name= list(best_model_score.keys())[
                    list(best_model_score.values().index(best_model_score))
            ]

            best_model= models[best_model_name]
            print(f'best model found, model name:{best_model_name} , R2 Score :{best_model_score}')
            print('\n=======================================\n')
            logging.info(f'best model found, model name:{best_model_name}, R2 Score: {best_model_score}')
            
            train_arr= np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr= np.c_[input_feature_test_arr, np.array(target_feature_test_df)]
            
            
            
            save_object(
                file_path= self.model_trainer_config.trained_model_file_path,
                obj= best_model
            )

            logging.info(" preprocessing pickle file object")

            return(
                train_arr,
                test_arr
            )

        except Exception as e:
            pass