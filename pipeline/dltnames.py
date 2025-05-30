# dltnames.py
from pipeline.catalog import *

def bronze_table(name: str) -> str:
    return f"{catalog}.bronze.`{name}`" if not name.isidentifier() else f"{catalog}.bronze.{name}"

def silver_table(name: str) -> str:
    return f"{catalog}.silver.{name}"

def gold_table(name: str) -> str:
    return f"{catalog}.gold.{name}"

# Optional: predefined table names
BRONZE_DLT_TABLES = {
    "obic_プロジェクトリスト": bronze_table("obic_プロジェクトリスト"),
    "orders": bronze_table("orders")
}

SILVER_DLT_TABLES = {
    "segment_master": silver_table("segment_master")
}

GOLD_DLT_TABLES = {
    "segment_master": gold_table("segment_master")
}
