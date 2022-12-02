"""
This module is the super-class for both prediction and training pipeline.

Author: Fabio
Date: July, 2022
"""
import logging
from datetime import datetime


logger=logging.getLogger(__name__)


class GenericPipeline():

    def __init__(self, config_project, pipeline_type_name, staging_level_run_type):
        """

        Params:
            config_project(dict): dictionary including all the config of the project
        
        """

        self.__init_config_params(config_project, pipeline_type_name, staging_level_run_type)



    def __init_config_params(self, config_project, pipeline_type_name, staging_level_run_type):
        """
        This method is responsible for setting the dictionary using params from config file
        """
        try:

            self._config_project=config_project

            self._pipeline_type_name=pipeline_type_name

            self._pipeline_type_config=self._config_project[self._pipeline_type_name]

            self._staging_level_run_type=staging_level_run_type

            self._dict_steps_pipeline=self._pipeline_type_config['STEPS']

            self._artifact_pipeline_steps=dict()

            self.__set_version()

        except Exception as err:
            logger.exception(err)
            raise

     

    def __set_version(
        self
        ):
        """
            This method is responsible for versioning both model and data artifact
        """
        try:
            current_date=datetime.today().strftime("%Y-%m-%d, %H:%M:%S")

            concat_date_pipeline_staging='{}_{}_{}'.format(current_date, self._pipeline_type_name, self._staging_level_run_type)

            self._version=concat_date_pipeline_staging

        except Exception as err:
            logger.exception(err)
            raise err

    def run_workflow(
        self
        ):
        """
            This is the management method for running the pipeline orchestrator
        """
        try:

            pass


        except Exception as err:
            logger.exception(err)
            raise err 