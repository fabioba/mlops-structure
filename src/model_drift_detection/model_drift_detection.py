"""
This module performs model drift detection
Model drift happens because the real-world changes (consequently the ground truth/target the model has been trained to predict)—the answers to business questions are always evolving. 
What holds today may no longer hold tomorrow, and we are expected to reflect this fact in our machine learning applications.

The dependent feature (target label) for the inference target class maybe not be present upfront in production. Once the dependent feature is present, 
there are various techniques to measure the drift and come to a conclusion of whether the model performance has deteriorated or not.
- compare the distribution of target class labels between the inference data and base data.
- once the actual target class label is made available, 
  then the model drift can be detected by evaluating and comparing the performance of the model on standard metrics. 



# 1. read metadata_active_model
# 2. from metadata_active_model, read model_evaluation dataset from TRAINING_PIPELINE
# 5. read model_prediction dataset from PREDICTION_PIPELINE
# 6. compare those datasets and metadatas
# 7. if MODEL_DRIFT_DETECTED = True then trigger TRAINING_PIPELINE, otherwise serve the predictions


Author: Fabio
Date: June, 2022
"""
from src.utils.generic_step import GenericStep
import logging

logger=logging.getLogger(__name__)


class ModelDriftDetectionStep(GenericStep):


    def __init__(self, config_project, pipeline_type_name, staging_level_run_type, version, step_name):

        GenericStep.__init__(self, config_project=config_project, pipeline_type_name=pipeline_type_name, staging_level_run_type=staging_level_run_type, version=version, step_name=step_name)



    def run_workflow(self):
        """
        This is the entrypoint of the step.
        """
        try:
            
            logger.info('workflow')

        except Exception as err:
            logger.exception(err)
            raise err
