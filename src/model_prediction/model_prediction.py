"""
This module performs prediction on new data

# 1. read data_processing dataset from PREDICTION_PIPELINE
# 2. read metadata_active_model
# 3. from metadata_active_model, read model_trained object
# 4. perform prediction on new data
# 5. store prediction (including version model used for predicting)

Author: Fabio
Date: June, 2022
"""
from src.utils.generic_step import GenericStep
import logging

logger=logging.getLogger(__name__)


class ModelPredictionStep(GenericStep):

    def __init__(self, config_project, pipeline_type_name, staging_level_run_type, version, step_name):

        GenericStep.__init__(self, config_project=config_project, pipeline_type_name=pipeline_type_name, staging_level_run_type=staging_level_run_type, version=version, step_name=step_name)


    def run_workflow(self):
        """
            This is the entrypoint of the step.
        """
        try:
            
            logger.info('workflow')


            # 1. __read_data_processing(PREDICTION_PIPELINE)
            # 2. __read_metadata_active_model()
            # 3. __read_model(model_key) --> model_key is the version of the active trained model
            # 4. __run_prediction()
            # 5. __store_prediction()


        except Exception as err:
            logger.exception(err)
            raise err



    def __run_prediction(self):
        """
            This method performs prediction on new data
        """
        try:
            
            logger.info('__run_prediction')


        except Exception as err:
            logger.exception(err)
            raise err

    



    def __store_prediction(self):
        """
            This method performs prediction on new data
        """
        try:
            
            logger.info('__store_prediction')


        except Exception as err:
            logger.exception(err)
            raise err
