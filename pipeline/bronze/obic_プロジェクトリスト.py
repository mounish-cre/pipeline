import dlt
from pyspark.sql.types import StructType, StructField, StringType
from pipeline.ingestion import *
from pipeline.dltnames import * 
from pipeline.schemas import *

@dlt.table(name=BRONZE_DLT_TABLES["obic_プロジェクトリスト"])
def bronze1():
    return read_bronze_stream(
        file_subdir="obic_プロジェクトリスト",
        encoding="Shift-JIS",
        schema=schemas["obic_プロジェクトリスト"],
        file_pattern=make_date_filename_pattern("obic_プロジェクトリスト")
    )

# @dlt.table(name=silver_dltname["segment_master"])
# def silver():
#     spark.sql('''

#  CREATE TABLE FROM xxxxx
#               ''')
#     spark.read(work.bronze.table2)
#     df=spark.read(bronze_dltnames["segment_master"])
#     return

# @dlt.table(name=gold_dltnames["segment_master"])
# def gold()
#     df=spark.read(silver_dltnames["segment_master"])
#     return