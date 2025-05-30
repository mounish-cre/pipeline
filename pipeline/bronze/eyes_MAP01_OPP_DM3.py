import dlt
from pyspark.sql.types import StructType, StructField, StringType
from pipeline.ingestion import *
from pipeline.dltnames import * 
from pipeline.schemas import *

@dlt.table(name=BRONZE_DLT_TABLES["eyes_MAP01_OPP_DM3"])
def bronze1():
    return read_bronze_stream(
        spark,
        file_subdir="eyes_MAP01_OPP_DM3",
        encoding="Shift-JIS",
        schema=schemas["eyes_MAP01_OPP_DM3"],
        file_pattern=make_date_filename_pattern("eyes_MAP01_OPP_DM3")
    )
