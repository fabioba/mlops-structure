"""
This module includes all the unit tests of the step

Author: Fabio
Date: July, 2022
"""
import pytest
import src.utils.utils as utils

from src.data_processing.data_processing import DataProcessingStep

@pytest.fixture(scope="session")
def config_data():
    """
        This method returns the conifg_project as dictionary
    """


    config_data=utils.read_yaml('config/config_project.yaml')

    return config_data

    

def test_init_data_processing(config_data):
    """
        This method tests the initialization of data processing
    """
    version='fake_version'
    staging_level_run_type='DEV'
    step_name='DATA_PROCESSING'
    pipeline_type_name='TRAINING_PIPELINE'


    data_processing_step=DataProcessingStep(config_project=config_data, pipeline_type_name=pipeline_type_name,staging_level_run_type=staging_level_run_type, version=version,step_name=step_name)


    assert data_processing_step is not None, 'data_processing_step is None'
    assert data_processing_step.version==version ,'version does not match'
    assert data_processing_step.staging_level_run_type==staging_level_run_type ,'staging_level does not match'
    assert data_processing_step.step_name==step_name ,'step_name does not match'
    assert data_processing_step.pipeline_type_name==pipeline_type_name ,'pipeline_type_name does not match'




