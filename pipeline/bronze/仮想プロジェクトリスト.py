import dlt
from pyspark.sql.types import StructType, StructField, StringType
from pipeline.ingestion import *
from pipeline.dltnames import * 
from pipeline.schemas import *

@dlt.table(name=BRONZE_DLT_TABLES["仮想プロジェクトリスト"])
def bronze1():
    return read_bronze_stream(
        file_subdir="仮想プロジェクトリスト",
        encoding="Shift-JIS",
        schema=schemas["仮想プロジェクトリスト"],
        file_pattern=make_date_filename_pattern("仮想プロジェクトリスト")
    )
