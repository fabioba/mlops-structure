"""
This module performs serving predictions after model drift check.
Serving prediction could be either storing the outcomes or answer to an API request


Author: Fabio
Date: June, 2022
"""
from ..utils.generic_step import GenericStep
import logging

logger=logging.getLogger(__name__)


class ServePredictionStep(GenericStep):

    def __init__(self, config_project, pipeline_type_name, staging_level_run_type, version, step_name):

        GenericStep.__init__(self, config_project=config_project, pipeline_type_name=pipeline_type_name, staging_level_run_type=staging_level_run_type, version=version, step_name=step_name)


    def run_workflow(self):
        """
        This is the entrypoint of the step.
        """
        try:
            
            logger.info('workflow')
            # 1. store prediciton with model version used  or return to API call

        except Exception as err:
            logger.exception(err)
            raise err
