import dlt
from pyspark.sql.types import StructType, StructField, StringType
from pipeline.ingestion import *
from pipeline.dltnames import * 
from pipeline.schemas import *

@dlt.table(name=BRONZE_DLT_TABLES["obic_原価要素マスタリスト"])
def bronze1():
    return read_bronze_stream(
        spark,
        file_subdir="obic_原価要素マスタリスト",
        encoding="Shift-JIS",
        schema=schemas["obic_原価要素マスタリスト"],
        file_pattern=make_date_filename_pattern("obic_原価要素マスタリスト")
    )
