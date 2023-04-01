"""
Processing JOB
"""

import sys
import pyspark.sql.functions as f
sys.path.insert(0, './helpers')
from helpers.spark import get_spark_session
sys.path.insert(0, './config')
from config.aws import LANDING_BUCKET, PROCESSING_BUCKET, ENEM_FOLDER
from pyspark.sql import (
    SparkSession, 
    DataFrame
)
import re

 
def read_csv(spark: SparkSession, bucket: str) -> DataFrame:
    """Read CSV files from S3 bucket"""
    print("Reading CSV for file")

    df = (
        spark
        .read
        .format("csv")
        .options(header='true', inferSchema='true', delimiter=';')
        .load(f"s3a://{bucket}/enem2020/*.csv")
        .withColumn("file_name", f.input_file_name())
    )
    return df


def write_parquet(bucket: str, df: DataFrame) -> DataFrame:
    """Write PARQUET files to S3 bucket"""
    print("Saving parquet for file")
    df_path = f"s3a://{bucket}/enem2020"
    print(f"Path: {df_path}")
    (
        df
        .write
        .format("parquet")
        .mode("overwrite")
        .save(df_path)
    )
    return True


if __name__ == "__main__":
    """Main ETL script definition."""
    spark = get_spark_session()

    print("Processing enem2020 data from landing to processing")
    
    df = read_csv(spark, LANDING_BUCKET)
    print("Done ----->")
    print("Writing Dataframe!")
    write_parquet(PROCESSING_BUCKET, df)
    print("Done!")
    spark.stop()