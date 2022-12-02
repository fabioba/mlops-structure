"""
This module is responsible for running the training pipeline.
In detail, it orchestrate the steps to follow by each step.

Author: Fabio
Date: June, 2022
"""
import logging
from src.utils.generic_pipeline import GenericPipeline
from src.data_processing.data_processing import DataProcessingStep
from src.train_test_split.train_test_split import TrainTestSplitStep
from src.model_training.model_training import TrainingModelStep
from src.model_evaluation.model_evaluation import ModelEvaluationStep
from src.model_deployment.model_deployment import ModelDeploymentStep


logger=logging.getLogger(__name__)


class TrainingPipeline(GenericPipeline):

    def __init__(self, config_project, pipeline_type_name, staging_level_run_type):
        """

            Params:
                config_project(dict): dictionary including all the config of the project
        
        """

        GenericPipeline.__init__(self, config_project=config_project, pipeline_type_name=pipeline_type_name, staging_level_run_type=staging_level_run_type)


    def run_steps(
        self
        ):
        """
            This is the management method for running the pipeline orchestrator
        """
        try:
            

            self.run_data_processing_step()

            self.run_train_test_split_step()

            self.run_train_model_step()

        

        except Exception as err:
            logger.exception(err)
            raise err 

  

    def run_data_processing_step(self):
        """
            This method creates the workflow for running data processing
        """
        try:

            data_processing_step=DataProcessingStep(config_project=self._config_project, 
            pipeline_type_name= self._pipeline_type_name,
            staging_level_run_type=self._staging_level_run_type, 
            version= self._version,
            step_name='DATA_PROCESSING')

            # 1. 2. self.__run_preprocessing()
            # 3. self.__store_data_processed_dataset()
            # 4. self.__read_data_processed_sf()
            # 5. 6. 7. 8. self.__set_data_processed_metadata()
            # 9. 10. self.__store_data_processed_metadata()
            # 11. self.__update_step_artifact()

            # 12. self.__set_artifact_pipeline_step('DATA_PROCESSING', data_processing_artifact)


        except Exception as err:
            logger.exception(err)
            raise err


    def run_train_test_split_step(self):
        """
            This method creates the workflow for running train_test_split step
        """
        try:
        
            train_test_split_step=TrainTestSplitStep(config_project=self._config_project,  
            pipeline_type_name= self._pipeline_type_name,
            staging_level_run_type=self._staging_level_run_type, 
            version= self._version,
            step_name='TRAIN_TEST_SPLIT')

            train_test_split_artifact=train_test_split_step.run_workflow()

            self._artifact_pipeline_steps['TRAIN_TEST_SPLIT']=train_test_split_artifact

        except Exception as err:
            logger.exception(err)
            raise

    def run_train_model_step(self):
        """
            This method creates the workflow for running train model step
        """
        try:

            train_model_step=TrainingModelStep(config_project=self._config_project,  
            pipeline_type_name= self._pipeline_type_name,
            staging_level_run_type=self._staging_level_run_type, 
            version= self._version,
            step_name='MODEL_TRAINING')
            
            # 1. __read_train_dataset()
            # 2. __train_model()
            # 3. __store_model()
            # 4. 5. 6. __set_model_metadata()
            # 7 8.. __store_model_metadata()


        except Exception as err:
            logger.exception(err)
            raise err
    
    def __set_artifact_pipeline_step(self, step_name, artifact_step_dict):
        """
            This method is responsible for setting the artifact step dict on the step_name as key in the _artifact_pipeline_steps

            Args:
                step_name(args): name of the step
                artifact_step_dict(dict): output of the step
        """
        try:

            self._artifact_pipeline_steps[step_name]=artifact_step_dict

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
  