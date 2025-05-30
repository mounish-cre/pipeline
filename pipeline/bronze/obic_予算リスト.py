import dlt
from pyspark.sql.types import StructType, StructField, StringType
from pipeline.ingestion import *
from pipeline.dltnames import * 
from pipeline.schemas import *

@dlt.table(name=BRONZE_DLT_TABLES["obic_予算リスト"])
def bronze1():
    return read_bronze_stream(
        spark,
        file_subdir="obic_予算リスト",
        encoding="Shift-JIS",
        schema=schemas["obic_予算リスト"],
        file_pattern=make_date_filename_pattern("obic_予算リスト")
    )
