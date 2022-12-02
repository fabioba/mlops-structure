"""
This module perform train_test_split


# 1. read feature_engineered dataset from S3 or from Snowflake, depends on where you worked
# 2. perform train and test split
# 3. store train and test dataset on S3


Author: Fabio
Date: June, 2022
"""
from src.utils.generic_step import GenericStep
import logging

logger=logging.getLogger(__name__)


class TrainTestSplitStep(GenericStep):


    def __init__(self, config_project, pipeline_type_name, staging_level_run_type, version, step_name):

        GenericStep.__init__(self, config_project=config_project, pipeline_type_name=pipeline_type_name, staging_level_run_type=staging_level_run_type, version=version, step_name=step_name)


    def run_workflow(self):
        """
            This is the entrypoint of the step.

            Returns:
                self.step_artifact(dict): dictioanry with all the metadata of the current step
        """
        try:
            
            logger.info('workflow')

            # 1. __read_feature_engineered_dataset()
            # 2. __split_feature_engineered_dataset_train_test()
            # 3. __store_train_test_datasets()
            # 4. self.__update_step_artifact()


            self.update_step_artifact()

            return self.step_artifact

        except Exception as err:
            logger.exception(err)
            raise err

    def __read_feature_engineered_dataset(self):
        """
            This method is responsible for reading the featur engineered dataset from S3
        """
        try:
            
            logger.info('__read_feature_engineered_dataset')

        except Exception as err:
            logger.exception(err)
            raise err

    def __split_feature_engineered_dataset_train_test(self):
        """
            This method performs splitting of the feature_engineered_dataset
        """
        try:
            
            logger.info('__split_feature_engineered_dataset_train_test')

        except Exception as err:
            logger.exception(err)
            raise err

    def __store_train_test_datasets(self):
        """
            This method stores train and test datasets
        """
        try:
            
            # 1. store train and test datasets on S3

            logger.info('__store_train_test_datasets')


        except Exception as err:
            logger.exception(err)
            raise err