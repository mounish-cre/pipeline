import dlt
from pyspark.sql.types import StructType, StructField, StringType
from pipeline.ingestion import *
from pipeline.dltnames import * 
from pipeline.schemas import *

@dlt.table(name=BRONZE_DLT_TABLES["eyes_待機要員一覧_コスト"])
def bronze1():
    return read_bronze_stream(
        file_subdir="eyes_待機要員一覧_コスト",
        encoding="Shift-JIS",
        schema=schemas["eyes_待機要員一覧_コスト"],
        file_pattern=make_date_filename_pattern("eyes_待機要員一覧_コスト")
    )
