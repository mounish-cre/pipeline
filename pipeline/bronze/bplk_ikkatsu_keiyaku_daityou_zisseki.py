import dlt
from pyspark.sql.types import StructType, StructField, StringType
from pipeline.ingestion import *
from pipeline.dltnames import * 
from pipeline.schemas import *

@dlt.table(name=BRONZE_DLT_TABLES["bplk_ikkatsu_keiyaku_daityou_zisseki"])
def bronze1():
    return read_bronze_stream(
        file_subdir="bplk_ikkatsu_keiyaku_daityou_zisseki",
        encoding="Shift-JIS",
        schema=schemas["bplk_ikkatsu_keiyaku_daityou_zisseki"],
        file_pattern=make_date_filename_pattern("bplk_ikkatsu_keiyaku_daityou_zisseki")
    )
