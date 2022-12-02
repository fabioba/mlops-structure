CREATE TABLE IF NOT EXISTS "{SNOWFLAKE_DATABASE}"."{SNOWFLAKE_SCHEMA}"."DATA_PROCESSING_METADATA_HISTORY_TABLE"(
    "step_name" VARCHAR,
    "version" VARCHAR,
    "staging_level"	VARCHAR,
    "pipeline_type"	VARCHAR,
    "current_date" TIMESTAMP_TZ(9),
    "num_columns" BIGINT,
    "list_columns_metadata" ARRAY
)