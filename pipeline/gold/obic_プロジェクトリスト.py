import dlt
from pyspark.sql.types import StructType, StructField, StringType
from pipeline.dltnames import * 
from pyspark.sql.functions import col, to_date
from pyspark.sql.types import IntegerType


@dlt.table(name=GOLD_DLT_TABLES["obic_プロジェクトリスト"])
def silver():
   return(
      spark.read.table(SILVER_DLT_TABLES["obic_プロジェクトリスト"])
      .withColumn("登録日", to_date(col("登録日"), "yyyy-MM-dd"))
   )