from src.DimondPricePridiction.components.data_ingestion import DataIngestion
import pandas as pd
from src.DimondPricePridiction.exception import customexception
from src.DimondPricePridiction.logger import logging
import os,sys

obj = DataIngestion()
obj.initiate_data_ingestion()

