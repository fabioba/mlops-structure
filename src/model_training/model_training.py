"""
This module performs training of the model


# 1. read train dataset
# 2. run training model process
# 3. store model object on S3
# 4. create model_metadata object
# 5. metadata.ADD( extract features used for training the model )
# 6. metadata.ADD( extract model parameters used for training the model )
# 7. store metadata model dict on S3
# 8. update model_metadata_history_table on SF  


Author: Fabio
Date: June, 2022
"""
import pandas as pd
from src.utils.generic_step import GenericStep
import logging

logger=logging.getLogger(__name__)


class TrainingModelStep(GenericStep):

    def __init__(self, config_project, pipeline_type_name, staging_level_run_type, version, step_name):

        GenericStep.__init__(self, config_project=config_project, pipeline_type_name=pipeline_type_name, staging_level_run_type=staging_level_run_type, version=version, step_name=step_name)


    def read_train_dataset(self):
        """
            This method is responsible for reading the train dataset, either from Snowflkae or S3
        """
        try:
          
            logger.info('__read_train_dataset')

        except Exception as err:
            logger.exception(err)
            raise err


    def train_model(self):
        """
            This method is responsible for running the model from the train dataset
        """
        try:
          
            logger.info('__train_model')

        except Exception as err:
            logger.exception(err)
            raise err



    def store_model(self):
        """
            This method is responsible for storing the model on S3
        """
        try:
          
            logger.info('__store_model')

        except Exception as err:
            logger.exception(err)
            raise err

    def set_model_metadata(self):
        """
            This method is responsible for setting the metadata for this process
        """
        try:

            model_metadata_json={
                "step_name":self.__step_name,
                "version":self.__version,
                "staging_level":self.__staging_level_run_type,
                "pipeline_type_name":self.__pipeline_type_name,
                "current_date":self.__current_date,
                "model_metadata":
                {
                    "model_name":"",
                    "hyperparameters":{}
                }
                
                }
            
            logger.info('model_metadata_json: {}'.format(model_metadata_json))

            self.__model_metadata = pd.DataFrame(model_metadata_json)    


        except Exception as err:
            logger.exception(err)
            raise err

    def store_model_metadata(self):
        """
            This method stores the model parameters
        """
        try:
            
            # 1. store model_metadata on S3
            # 2. insert current model_metadata in model_metadata_history_table on Snowflake 

            logger.info('__store_model_metadata')


        except Exception as err:
            logger.exception(err)
            raise err