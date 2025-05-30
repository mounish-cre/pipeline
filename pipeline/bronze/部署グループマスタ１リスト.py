import dlt
from pyspark.sql.types import StructType, StructField, StringType
from pipeline.ingestion import *
from pipeline.dltnames import * 
from pipeline.schemas import *

@dlt.table(name=BRONZE_DLT_TABLES["部署グループマスタ１リスト"])
def bronze1():
    return read_bronze_stream(
        file_subdir="部署グループマスタ１リスト",
        encoding="Shift-JIS",
        schema=schemas["部署グループマスタ１リスト"],
        file_pattern=make_date_filename_pattern("部署グループマスタ１リスト")
    )
