import dlt
from pyspark.sql.types import StructType, StructField, StringType
from pipeline.ingestion import *
from pipeline.dltnames import * 
from pipeline.schemas import *

@dlt.table(name=BRONZE_DLT_TABLES["obic_セグメントマスタリスト"])
def bronze1():
    return read_bronze_stream(
        file_subdir="obic_セグメントマスタリスト",
        encoding="Shift-JIS",
        schema=schemas["obic_セグメントマスタリスト"],
        file_pattern=make_date_filename_pattern("obic_セグメントマスタリスト")
    )
