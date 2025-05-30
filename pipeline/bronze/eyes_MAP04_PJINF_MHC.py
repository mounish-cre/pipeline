import dlt
from pyspark.sql.types import StructType, StructField, StringType
from pipeline.ingestion import *
from pipeline.dltnames import * 
from pipeline.schemas import *

@dlt.table(name=BRONZE_DLT_TABLES["eyes_MAP04_PJINF_MHC"])
def bronze1():
    return read_bronze_stream(
        spark,
        file_subdir="eyes_MAP04_PJINF_MHC",
        encoding="Shift-JIS",
        schema=schemas["eyes_MAP04_PJINF_MHC"],
        file_pattern=make_date_filename_pattern("eyes_MAP04_PJINF_MHC")
    )
