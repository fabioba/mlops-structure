"""
This module performs model deployment

# 1. read model_metadata
# 2. read model_evaluation metadata
# 3. read data_processing metadata
# 4. update model_active_history_table on SF (it includes the merge of the previous tables)


- table MODEL_DEPLOYMENT_METADATA_HISTORY_TABLE on Snowflake:
    - start_date: refers to when the model has been deployed
    - end_date: refers to when the model has been replaced by another model

Author: Fabio
Date: June, 2022
"""
import pandas as pd
from src.utils.generic_step import GenericStep
import logging

logger=logging.getLogger(__name__)


class ModelDeploymentStep(GenericStep):

    def __init__(self, config_project, pipeline_type_name, staging_level_run_type, version, step_name):

        GenericStep.__init__(self, config_project=config_project, pipeline_type_name=pipeline_type_name, staging_level_run_type=staging_level_run_type, version=version, step_name=step_name)



    def run_workflow(self):
        """
        This is the entrypoint of the step.
        """
        try:
            
            logger.info('workflow')
            # 1. __read_model_metadata()
            # 2. __read_model_evaluation_metadata()
            # 3. __read_data_processing_metadata()
            # 4. __deploy_model()

        except Exception as err:
            logger.exception(err)
            raise err


    def __read_model_metadata(self):
        """
            This method is responsible for reading the trained model metadata
        """
        try:
          
            logger.info('__read_model_metadata')

        except Exception as err:
            logger.exception(err)
            raise
        
 
    def __read_model_evaluation_metadata(self):
        """
            This method is responsible for reading the trained model evaluation metadata
        """
        try:
          
            logger.info('__read_model_evaluation_metadata')

        except Exception as err:
            logger.exception(err)
            raise
        
 
    def __read_data_processing_metadata(self):
        """
            This method is responsible for reading the data processing metadata
        """
        try:
          
            logger.info('__read_data_processing_metadata')

        except Exception as err:
            logger.exception(err)
            raise

 
    def __deploy_model(self):
        """
            This method is responsible for deploying the model.
        """
        try:
          
            logger.info('__deploy_model')

            # 1. update the model_active_history_table on Snowflake with the current version of the model

        except Exception as err:
            logger.exception(err)
            raise