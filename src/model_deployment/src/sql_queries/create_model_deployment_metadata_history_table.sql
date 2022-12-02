CREATE TABLE IF NOT EXISTS "{SNOWFLAKE_DATABASE}"."{SNOWFLAKE_SCHEMA}"."MODEL_DEPLOYMENT_METADATA_HISTORY_TABLE"(
    "version" VARCHAR,
    "staging_level"	VARCHAR,
    "pipeline_type_name"	VARCHAR,
    "current_date" TIMESTAMP_TZ(9),
    "start_date" TIMESTAMP_TZ(9),
    "end_date" TIMESTAMP_TZ(9),
    "is_active_model" BOOLEAN
)