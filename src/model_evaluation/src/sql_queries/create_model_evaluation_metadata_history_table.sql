CREATE TABLE IF NOT EXISTS "{SNOWFLAKE_DATABASE}"."{SNOWFLAKE_SCHEMA}"."MODEL_EVALUATION_METADATA_HISTORY_TABLE"(
    "step_name" VARCHAR,
    "version" VARCHAR,
    "staging_level"	VARCHAR,
    "pipeline_type_name"	VARCHAR,
    "current_date" TIMESTAMP_TZ(9),
    "model_evaluation_metadata" OBJECT
)