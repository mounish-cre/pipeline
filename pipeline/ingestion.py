
from pyspark.sql.functions import current_timestamp, col, regexp_extract

BRONZE_BASE_PATH = "abfss://work@credatabricksdatastorage.dfs.core.windows.net"

def make_date_filename_pattern(base_name: str) -> str:

    return rf"{base_name}_(\d{{4}}-\d{{2}}-\d{{2}})\.csv"

def read_bronze_stream(spark,file_subdir: str, schema, file_pattern: str,encoding: str):

    full_path = f"{BRONZE_BASE_PATH}/{file_subdir.strip('/')}/"
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .option("encoding", encoding)
        .option("header", "true")
        .schema(schema)
        .load(full_path)
        .withColumn("ingestion_time", current_timestamp())
        .withColumn(
            "file_date",
            regexp_extract(col("_metadata.file_path"), file_pattern, 1)
        )
    )

