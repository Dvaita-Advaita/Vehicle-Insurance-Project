import sys
import pandas as pd
import numpy as np
from typing import Optional

from src.configuration.mongo_db_connection import MongoDBClient
from src.constants import DATABASE_NAME
from src.exception import MyException

class Proj1Data:
    """
    A class to export MongoDB records as a pandas DataFrame
    """

    def __init__(self) -> None:
        """
        Initializes the MongoDB records as a pandas DataFrame
        """
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise MyException(e,sys)
    
    def export_collection_as_dataframe(self,collection_name:str,database_name:Optional[str]=None) ->pd.DataFrame:
        """
        Exports an entire MongoDB collection as a pandas DataFrame

        Parameters:
        ------------
        collection_name : str
           The name of the MOngoDB collection to export
        database_name : OPtional[str]
            Name of the database (optional).Default to DATABASE_NAME

        Returns:
        ------------
        pd.DataFrame containing the collection data,with '_id' column removed and 'na' vlaues replaced with NaN
                         
        """
        try:
            # Access specifid collection from the default or spcified database
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]

            # Convert collection data to DataFRame and preprocess
            print("Fetching data from mongoDB")
            df = pd.DataFrame(list(collection.find()))
            print(f"Data fetched with len:{len(df)}")
            if "id" in df.columns.to_list():
                df = df.drop(columns=["id"],axis=1)
            df.replace({"na":np.nan},inplace=True)
            return df
        
        except Exception as e:
            raise MyException(e,sys)

    

    