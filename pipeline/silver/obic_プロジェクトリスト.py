import dlt
from pyspark.sql.types import StructType, StructField, StringType
from pipeline.dltnames import * 
from pyspark.sql.functions import col, to_date
from pyspark.sql.types import IntegerType


@dlt.table(name=SILVER_DLT_TABLES["obic_プロジェクトリスト"])
def silver():
   return(
      spark.read.table(BRONZE_DLT_TABLES["obic_プロジェクトリスト"])
      .withColumn("file_date", to_date(col("file_date"), "yyyy-MM-dd"))
   )