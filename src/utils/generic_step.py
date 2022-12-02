"""
This superclass encapsulates all the methods and parameters that will be inheritanced by all steps

Author: Fabio
Date: June, 2022
"""
import logging
from datetime import datetime

logger=logging.getLogger(__name__)


class GenericStep():
    """
    
    """

    def __init__(self, config_project, pipeline_type_name, staging_level_run_type, version, step_name):

        logger.info('init {}'.format(step_name))


        self.__init_config_params(config_project, pipeline_type_name, staging_level_run_type, version, step_name)


    def __init_config_params(self, config_project, pipeline_type_name, staging_level_run_type, version, step_name):
        """
            This method is responsible for setting the dictionary using params from config file

            Args:
                config_project(dict): dictionary of params
                pipeline_type_name(str): type of pipeline (TRAINING, PREDICTION)
                staging_level_run_type(str)
                version(str): version of the current running
                step_name(str): name of the step
                
        """
        try:
            self.__current_date=datetime.today().strftime("%Y-%m-%d %H:%M:%S")

            self.config_project=config_project

            self.pipeline_type_name=pipeline_type_name

            self.staging_level_run_type=staging_level_run_type
            
            self.s3_bucket_name=config_project['STAGING_LEVEL'][staging_level_run_type]['S3']['BUCKET_NAME']

            self.version=version

            self.step_name=step_name
            
            self.__merge_config_step_default_value()

            self.__init_step_artifact()
            

        except Exception as err:
            logger.exception(err)
            raise

    def __merge_config_step_default_value(self):
        """
            This method merge the default config values for the step with the values set by the current pipeline.

            Returns:
                config_step_merged(dict): merged values of the current step
        """
        try:
            config_step_default = self.config_project['STEPS'][self.step_name]

            if self.step_name in self.config_project[self.pipeline_type_name]['STEPS'].items():

                config_step_current_pipeline=self.config_project[self.pipeline_type_name]['STEPS'][self.step_name]

                # merge dictionary where the second overwrite values of the first. overwrite default values
                config_step_merged = {**config_step_default, **config_step_current_pipeline}

                logger.info('config_step_merged: {}'.format(config_step_merged))

                self.config_step=config_step_merged

            else:

                self.config_step=config_step_default



        except Exception as err:
            logger.exception(err)
            raise err



    def __init_step_artifact(self):
        """
            This method initialize the step_artifacts
        """
        try:
            
            self.step_artifact= dict()

            self.step_artifact['step_name']=self.step_name
            self.step_artifact['staging_level_run_type']=self.staging_level_run_type
            self.step_artifact['current_pipeline']=self.pipeline_type_name
            self.step_artifact['pipeline_to_trigger']=None
            self.step_artifact['status_current_step']='INIT'
            self.step_artifact['start_time_current_step']=datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            self.step_artifact['end_time_current_step']=None

            logger.info('step_artifact: {}'.format(self.step_artifact))


        except Exception as err:
            logger.exception(err)
            raise err


    def __get_password_key_staging_level(
        self,
        key_password):
        """
            This method returns the KEY name for the PASSWORD parameter, based on the current STAGING_LEVEL

            Output:
                password_staging_level(str)
        """
        try:

            logger.info('key_password: {}'.format(key_password))

            snowflake_password_staging_level= '{}_{}'.format(key_password,self.staging_level_run_type)

            logger.info('snowflake_password_staging_level: {}'.format(snowflake_password_staging_level))

            return snowflake_password_staging_level

        
        except Exception as err:
            logger.exception(err)
            raise err


    def read_data(self):
        """
            This method is responsible for reading data
        """
        try:

            pass

        except Exception as err:
            logger.exception(err)
            raise err

    def write_data(self):
        """
            This method is responsible for writing data
        """
        try:

            pass

        except Exception as err:
            logger.exception(err)
            raise err

    
    def read_model(self, model_key):
        """
            This method is responsible for reading the trained model

            Args:
                model_key(str): this key distinguish each model from the others
        """
        try:
          
            logger.info('__read_model')

        except Exception as err:
            logger.exception(err)
            raise


    def read_metadata_active_model(self):
        """
            This method is responsible for reading the metadata of the active model. This data contains information about the data processing of the current model
        """
        try:
            
            logger.info('__read_metadata_active_model')


        except Exception as err:
            logger.exception(err)
            raise err


    def read_data_processing(
        self, 
        type_pipeline):
        """
            This method is responsible for reading artifacts from data-processing step

            Args:
                type_pipeline(str): type of the pipeline used to run data-processing (TRAINING_PIPELINE vs PREDICTION_PIPELINE). This parameter has been used to read data from the right bucket folder
        """
        try:
            
            logger.info('__read_data_processing')


        except Exception as err:
            logger.exception(err)
            raise err

    def update_step_artifact(
        self,
        pipeline_to_trigger=None
    ):
        """
            This method update the artifact of the current step. It determines if the current step triggers another pipeline
        """
        try:

            self.step_artifact['pipeline_to_trigger']=pipeline_to_trigger
            self.step_artifact['status_current_step']='COMPLETE'
            self.step_artifact['end_time_current_step']=datetime.today().strftime("%Y-%m-%d %H:%M:%S")

        except Exception as err:
            logger.exception(err)
            raise err
