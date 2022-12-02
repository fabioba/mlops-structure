"""
This module supports others

Author: Fabio
"""
import logging
import yaml
import logging.config

logger=logging.getLogger(__name__)


def set_version_current_running():
    """

    """
    try:

        pass

    except Exception as err:
        logger.exception(err)
        raise err


def read_yaml(path):
    """
        This method read yaml
        Args:
            path(str): path of the yaml file
        Output:
            dict_output(dict)
    """
    try:
        with open(path, 'r') as yaml_file:
            dict_output = yaml.load(yaml_file, Loader=yaml.Loader)

            return dict_output
            
    except Exception as err:
        logger.exception(err)
        raise

def setup_logging(path_logging_config):
    """
        This method is responsible for setting the logging

        Args:
            path_logging_config(str): path of the logging config file
    """
    try:
        with open(path_logging_config, 'r') as f:

            log_config = yaml.safe_load(f.read())

            logging.config.dictConfig(log_config)

    except Exception as err:
        logger.exception(err)
        raise