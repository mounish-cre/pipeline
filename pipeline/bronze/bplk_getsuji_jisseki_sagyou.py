import dlt
from pyspark.sql.types import StructType, StructField, StringType
from pipeline.ingestion import *
from pipeline.dltnames import * 
from pipeline.schemas import *

@dlt.table(name=BRONZE_DLT_TABLES["bplk_getsuji_jisseki_sagyou"])
def bronze1():
    return read_bronze_stream(
        file_subdir="bplk_getsuji_jisseki_sagyou",
        encoding="Shift-JIS",
        schema=schemas["bplk_getsuji_jisseki_sagyou"],
        file_pattern=make_date_filename_pattern("bplk_getsuji_jisseki_sagyou")
    )
