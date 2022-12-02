"""
This is the entrypoint of the project.
This module is responsible for orchestrating which pipeline to run and handle with the output.

Author: Fabio
Date: June, 2022
"""
import src.utils.utils as utils

utils.setup_logging('config/logging_config.yaml')

import logging
import argparse

# import steps
from src.prediction_pipeline import PredictionPipeline
from src.training_pipeline import TrainingPipeline


logger=logging.getLogger(__name__)


def main(args):
    """
    This is the entrypoint of the module. It starts the PipelineOrchestrator

    Args:
        args(dict): argument passed by user
    """
    try:

        config_project=utils.read_yaml('config/config_project.yaml')


        pipeline_type_name=args.pipeline_type_name
        staging_level_run_type=args.staging_level_run_type

        orchestrate_pipeline(config_project, pipeline_type_name, staging_level_run_type)

    except Exception as err:
        logger.exception(err)
        raise err


def orchestrate_pipeline(
    config_project, 
    pipeline_type_name, 
    staging_level_run_type):
    """
        This method manages which pipeline to run

        Args:
            config_project(dict): config from config.yaml
            pipeline_type(str): type of pipeline
            staging_level_run_type(str): level of staging
    """
    try:
        
        if pipeline_type_name=='TRAINING_PIPELINE':

            logger.info('TRAINING_PIPELINE starting')

            training_pipeline=TrainingPipeline(config_project=config_project, pipeline_type_name=pipeline_type_name, staging_level_run_type=staging_level_run_type)

            training_pipeline.run_steps()

            training_pipeline.store_pipeline_artifact()

            logger.info('TRAINING_PIPELINE finish')

             
        if pipeline_type_name=='PREDICTION_PIPELINE':
            # create instance prediction pipeline
            # run prediction pipeline
            # check if there's data drift. If there's data drift, trigger training pipeline otherwise run another prediciton pipeline for predicting

            pass




    except Exception as err:
        logger.exception(err)
        raise err





if __name__=='__main__':
    
    parser = argparse.ArgumentParser()

    parser.add_argument("--staging_level_run_type", help="staging level", default='DEV')
    parser.add_argument("--pipeline_type_name", help="pipeline type", default='TRAINING_PIPELINE')

    args = parser.parse_args()
  
    main(args)