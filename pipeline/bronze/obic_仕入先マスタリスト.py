import dlt
from pyspark.sql.types import StructType, StructField, StringType
from pipeline.ingestion import *
from pipeline.dltnames import * 
from pipeline.schemas import *

@dlt.table(name=BRONZE_DLT_TABLES["obic_仕入先マスタリスト"])
def bronze1():
    return read_bronze_stream(
        spark,
        file_subdir="obic_仕入先マスタリスト",
        encoding="Shift-JIS",
        schema=schemas["obic_仕入先マスタリスト"],
        file_pattern=make_date_filename_pattern("obic_仕入先マスタリスト")
    )
