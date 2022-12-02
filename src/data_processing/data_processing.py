"""
This module performs data_processing

Logic:
# 1. run cleaning step
# 2. run pre-processing step
# 3. store data_processed table, which is essentially the output from the previous steps
# 4. read 1 line of the output table from Snowlflake (if used) or from current data_processed (if the input data was on S3). this must be done to retrieve schema of the table
# 5. create metadata data_processed object
# 6. metadata.ADD( extract schema from output table)
# 7. metadata.ADD( count number of features)
# 8. metadata.ADD( extract feature distribution (mean, median, max, min))   FUTURE STEP
# 9. store data_processing_metadata dict on S3
# 10. update data_processing_metadata_history_table on SF
# 11. update __step_artifact

Pseudocode:
# 1. 2. self.__run_preprocessing()
# 3. self.__store_data_processed_dataset()
# 4. self.__read_data_processed_sf()
# 5. 6. 7. 8. self.__set_data_processed_metadata()
# 9. 10. self.__store_data_processed_metadata()
# 11. self.__update_step_artifact()



Author: Fabio
Date: June, 2022
"""
import pandas as pd

from src.utils.generic_step import GenericStep
import logging

logger=logging.getLogger(__name__)


class DataProcessingStep(GenericStep):

    def __init__(self, config_project, pipeline_type_name, staging_level_run_type, version, step_name):

        GenericStep.__init__(self, config_project=config_project, pipeline_type_name=pipeline_type_name, staging_level_run_type=staging_level_run_type, version=version, step_name=step_name)



    def run_preprocessing(self):
        """
            This method performs all the tasks necessary to clean and pre-process the input table
        """
        try:
            # 1. perform cleaning and pre-processing steps (either on Snowlflake running sequence of query or on S3 running steps on python)
            # 2. add version of the pipeline on the output table

            logger.info('__run_preprocessing')


        except Exception as err:
            logger.exception(err)
            raise err

    def store_data_processed_dataset(self):
        """
            This method stores the table cleaned and pre-processed
        """
        try:
            
            # 1. store either on S3 or Snowflkae, depends on where you prefer to work
            # if you work on Snowflake, this part could be skipped. Otherwise, if you work on python (data source: S3) you should store the output table on S3

            logger.info('__store_data_processed_dataset')


        except Exception as err:
            logger.exception(err)
            raise err

    def read_data_processed_sf(self):
        """
            This method is responsible for reading the data processed table from Snwoflake. If the input table was there
        """
        try:

            # run this query read_one_line_data_processed.sql to retrieve just the first line of the table. Then, extract information
            

            logger.info('__read_data_processed_sf')

        except Exception as err:
            logger.exception(err)
            raise err        

    def set_data_processed_metadata(self):
        """
            This method is responsible for setting the metadata for this process
        """
        try:

            # run query create_data_processing_metadata_history_table.sql to create the table on Snoflake
            # run query command

            list_columns_metadata = self.__get_metadata_data_processed_output()

            # encapsulate [list_columns_metadata] for converting it in list on PD Dataframe
            data_processed_metadata_json={
                "step_name":self.__step_name,
                "version":self.__version,
                "staging_level":self.__staging_level_run_type,
                "pipeline_type_name":self.__pipeline_type_name,
                "current_date":self.__current_date,
                "num_columns":0,
                "list_columns_metadata": [list_columns_metadata]
                }
            
            logger.info('data_processed_metadata_json: {}'.format(data_processed_metadata_json))

            self.__data_processed_metadata = pd.DataFrame(data_processed_metadata_json)    


        except Exception as err:
            logger.exception(err)
            raise err

    
    def get_data_processed_metadata(self):
        """
            This method is responsible for getting the metadata of the processed data

            Returns:
                data_processed_metadata(pandas DF): this dataframe contains all the information of the processed data
        """
        try:

            data_processed_metadata=self.__data_processed_metadata

            return data_processed_metadata

        except Exception as err:
            logger.exception(err)
            raise err

    def get_metadata_data_processed_output(self):
        """
            This method is responsible for getting the schema of the data_processed output table of this step

            Output:
                list_columns_type(list): this list contains the column information: name and type
        """
        try:

            list_columns_type=list()

            for col_name in self.__data_processing_output_table.columns:

                col_type=self.__data_processing_output_table[col_name].dtype

                col_name_type={"column_name":col_name, "type_column":col_type}

                list_columns_type.append(col_name_type)

            return list_columns_type

        except Exception as err:
            logger.exception(err)
            raise err


    def store_data_processed_metadata(self):
        """
            This method stores the table cleaned and pre-processed
        """
        try:
            
            # 1. store data_processing_metadata on S3
            # 2. insert current data_processing_metadata in data_processing_metadata_history_table on Snowflake 

            logger.info('__store_data_processed_metadata')


        except Exception as err:
            logger.exception(err)
            raise err


