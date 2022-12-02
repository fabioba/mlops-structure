"""
This module performs evaluation of the model

# 1. read test dataset
# 2. read trained model
# 3. create model_evaluation_metadata object
# 4. metadata.ADD( calculate evaluation metrics values )
# 5. store metadata model evaluation dict on S3
# 6. update model_evaluation_metadata_history_table on SF 

Author: Fabio
Date: June, 2022
"""
import pandas as pd
from src.utils.generic_step import GenericStep
import logging

logger=logging.getLogger(__name__)


class ModelEvaluationStep(GenericStep):

    def __init__(self, config_project, pipeline_type_name, staging_level_run_type, version, step_name):

        GenericStep.__init__(self, config_project=config_project, pipeline_type_name=pipeline_type_name, staging_level_run_type=staging_level_run_type, version=version, step_name=step_name)



    def run_workflow(self):
        """
        This is the entrypoint of the step.
        """
        try:

            logger.info('workflow')


            # 1. __read_test_dataset()
            # 2. __read_model(model_key) --> model_key is the version for TRAINING_PIPELINE since you read the model just trained
            # 3. 4. __set_model_evaluation_metadata()
            # 5. 6. __store_model_evaluation_metadata()


        except Exception as err:
            logger.exception(err)
            raise err



    def __read_test_dataset(self):
        """
            This method is responsible for reading the test dataset, either from Snowflkae or S3
        """
        try:
          
            logger.info('__read_test_dataset')

        except Exception as err:
            logger.exception(err)
            raise


    def __set_model_evaluation_metadata(self):
        """
            This method is responsible for setting the metadata for this process
        """
        try:

            model_evaluation_metadata_json={
                "step_name":self.__step_name,
                "version":self.__version,
                "staging_level":self.__staging_level_run_type,
                "pipeline_type_name":self.__pipeline_type_name,
                "current_date":self.__current_date,
                "model_evaluation_metadata":
                    {
                        "model_name":"",
                        "list_metrics":
                        [
                            {
                                "metric_name":"",
                                "value":0
                            }
                        ]
                    }
                
                }
            
            logger.info('model_evaluation_metadata_json: {}'.format(model_evaluation_metadata_json))

            self.__model_evaluation_metadata = pd.DataFrame(model_evaluation_metadata_json)    


        except Exception as err:
            logger.exception(err)
            raise err

    def __store_model_evaluation_metadata(self):
        """
            This method stores the model evaluation params
        """
        try:
            
            # 1. store model_metadata on S3
            # 2. insert current model_metadata in model_evaluation_metadata_history_table on Snowflake 

            logger.info('__store_model_evaluation_metadata')


        except Exception as err:
            logger.exception(err)
            raise err