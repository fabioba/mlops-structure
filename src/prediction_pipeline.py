"""
This module is responsible for running the training pipeline.
In detail, it orchestrate the steps to follow by each step.

Author: Fabio
Date: June, 2022
"""
import logging
from datetime import datetime
from src.utils.generic_pipeline import GenericPipeline
from src.data_processing.data_processing import DataProcessingStep
from src.data_drift_detection.data_drift_detection import DataDriftDetectionStep
from src.model_prediction.model_prediction import ModelPredictionStep
from src.model_drift_detection.model_drift_detection import ModelDriftDetectionStep
from src.serve_prediction.serve_prediction import ServePredictionStep


logger=logging.getLogger(__name__)


class PredictionPipeline(GenericPipeline):


    def __init__(self, config_project, pipeline_type_name, staging_level_run_type):
        """

            Params:
                config_project(dict): dictionary including all the config of the project
        
        """

        GenericPipeline.__init__(self, config_project=config_project, pipeline_type_name=pipeline_type_name, staging_level_run_type=staging_level_run_type)


    def run_workflow(
        self
        ):
        """
        This is the management method for running the pipeline orchestrator
        """
        try:

            
            self.run_data_processing_step()


        except Exception as err:
            logger.exception(err)
            raise err 


    def run_data_processing_step(
        self
        ):
        """
        This is the management method for running the pipeline orchestrator
        """
        try:

    
            data_processing_step=DataProcessingStep(config_project=self.__config_project, 
            pipeline_type_name= self.__pipeline_type_name,
            staging_level_run_type=self.__staging_level_run_type, 
            version= self.__version,
            step_name='DATA_PROCESSING')
        

        except Exception as err:
            logger.exception(err)
            raise err 

    

    def store_pipeline_artifact(self):
        """
            This method is responsible for storing pipeline artifact
        """
        try:
            
            pass

        except Exception as err:
            logger.exception(err)
            raise err

  