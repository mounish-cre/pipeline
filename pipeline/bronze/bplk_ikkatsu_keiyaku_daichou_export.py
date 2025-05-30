import dlt
from pyspark.sql.types import StructType, StructField, StringType
from pipeline.ingestion import *
from pipeline.dltnames import * 
from pipeline.schemas import *

@dlt.table(name=BRONZE_DLT_TABLES["bplk_ikkatsu_keiyaku_daichou_export"])
def bronze1():
    return read_bronze_stream(
        spark,
        file_subdir="bplk_ikkatsu_keiyaku_daichou_export",
        encoding="Shift-JIS",
        schema=schemas["bplk_ikkatsu_keiyaku_daichou_export"],
        file_pattern=make_date_filename_pattern("bplk_ikkatsu_keiyaku_daichou_export")
    )
