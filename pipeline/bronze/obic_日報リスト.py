import dlt
from pyspark.sql.types import StructType, StructField, StringType
from pipeline.ingestion import *
from pipeline.dltnames import * 
from pipeline.schemas import *

@dlt.table(name=BRONZE_DLT_TABLES["obic_日報リスト"])
def bronze1():
    return read_bronze_stream(
        file_subdir="obic_日報リスト",
        encoding="Shift-JIS",
        schema=schemas["obic_日報リスト"],
        file_pattern=make_date_filename_pattern("obic_日報リスト")
    )
