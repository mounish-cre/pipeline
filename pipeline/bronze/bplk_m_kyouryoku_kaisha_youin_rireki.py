import dlt
from pyspark.sql.types import StructType, StructField, StringType
from pipeline.ingestion import *
from pipeline.dltnames import * 
from pipeline.schemas import *

@dlt.table(name=BRONZE_DLT_TABLES["bplk_m_kyouryoku_kaisha_youin_rireki"])
def bronze1():
    return read_bronze_stream(
        spark,
        file_subdir="bplk_m_kyouryoku_kaisha_youin_rireki",
        encoding="Shift-JIS",
        schema=schemas["bplk_m_kyouryoku_kaisha_youin_rireki"],
        file_pattern=make_date_filename_pattern("bplk_m_kyouryoku_kaisha_youin_rireki")
    )
