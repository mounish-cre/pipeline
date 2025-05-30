import dlt
from pyspark.sql.types import StructType, StructField, StringType
from pipeline.dltnames import * 
from pyspark.sql.functions import col, to_date
from pyspark.sql.types import IntegerType


@dlt.table(name=GOLD_DLT_TABLES["obic_プロジェクトリスト"])
def silver():
      return spark.sql(f"""
        SELECT
            TO_DATE(`登録日`, 'yyyy-MM-dd') AS `登録日_date`
        FROM {SILVER_DLT_TABLES["obic_プロジェクトリスト"]}
    """)
   