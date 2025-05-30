import dlt
from pyspark.sql.types import StructType, StructField, StringType
from pipeline.ingestion import *
from pipeline.dltnames import * 
from pipeline.schemas import *

@dlt.table(name=BRONZE_DLT_TABLES["eyes_MAP03_MM_COST3"])
def bronze1():
    return read_bronze_stream(
        file_subdir="eyes_MAP03_MM_COST3",
        encoding="Shift-JIS",
        schema=schemas["eyes_MAP03_MM_COST3"],
        file_pattern=make_date_filename_pattern("eyes_MAP03_MM_COST3")
    )
