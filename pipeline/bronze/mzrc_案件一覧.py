import dlt
from pyspark.sql.types import StructType, StructField, StringType
from pipeline.ingestion import *
from pipeline.dltnames import * 
from pipeline.schemas import *

@dlt.table(name=BRONZE_DLT_TABLES["mzrc_案件一覧"])
def bronze1():
    return read_bronze_stream(
        spark,
        file_subdir="mzrc_案件一覧",
        encoding="Shift-JIS",
        schema=schemas["mzrc_案件一覧"],
        file_pattern=make_date_filename_pattern("mzrc_案件一覧")
    )
