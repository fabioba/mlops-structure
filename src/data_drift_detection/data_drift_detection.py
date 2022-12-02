"""
This module performs data drift detection. Data drift refers to a meaningful change in distribution between the training data and production data.
Data drift refers to a meaningful change in distribution between the training data and production data.
Oftentimes, the changes that degrade model performance the most are changes made to the most important features that the model uses to “connect the dots” and make predictions.


# 1. read metadata_active_model
# 2. from metadata_active_model, read data_processing metadata from TRAINING_PIPELINE
# 3. read data_processing metadata from PREDICTION_PIPELINE
# 4. from metadata_active_model, read data_processing dataset from TRAINING_PIPELINE
# 5. read data_processing dataset from PREDICTION_PIPELINE
# 6. compare those datasets and metadatas
# 7. if DATA_DRIFT_DETECTED = True then trigger TRAINING_PIPELINE, otherwise calculate predictions

Author: Fabio
Date: June, 2022
"""
from src.utils.generic_step import GenericStep
import logging

logger=logging.getLogger(__name__)


class DataDriftDetectionStep(GenericStep):

    def __init__(self, config_project, pipeline_type_name, staging_level_run_type, version, step_name):

        GenericStep.__init__(self, config_project=config_project, pipeline_type_name=pipeline_type_name, staging_level_run_type=staging_level_run_type, version=version, step_name=step_name)


    def run_workflow(self):
        """
        This is the entrypoint of the step.
        """
        try:
            
            logger.info('workflow')

            # 1. __read_metadata_active_model()
            # 2. __read_metadata_data_processing(TRAINING_PIPELINE)
            # 3. __read_metadata_data_processing(PREDICTION_PIPELINE)
            # 4. __read_data_processing(TRAINING_PIPELINE)
            # 5. __read_data_processing(PREDICTION_PIPELINE)
            # 6. 7. __detect_data_drift()
           



            self.__update_step_artifact()

        except Exception as err:
            logger.exception(err)
            raise err

    

    def __read_metadata_data_processing(self, type_pipeline):
        """
            This method is responsible for reading the metadata from data-processing step
        """
        try:
            
            logger.info('__read_metadata_data_processing')


        except Exception as err:
            logger.exception(err)
            raise err




    def __detect_data_drift(self):
        """
            This method is responsible for comparing data-processing from TRAINING_PIPELINE and PREDICTION_PIPELINE
        """
        try:
            
            logger.info('__detect_data_drift')


        except Exception as err:
            logger.exception(err)
            raise err


    def __update_step_artifact(self):
        """
            This method update the artifact of the current step. It determines if the current step triggers another pipeline
        """
        try:

            self.step_artifact['pipeline_to_trigger']='TRAINING_PIPELINE'

        except Exception as err:
            logger.exception(err)
            raise err