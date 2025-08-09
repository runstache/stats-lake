"""
Pytest Fixtures
"""

import posixpath

import pytest
from pyspark import SparkConf
from pyspark.sql import SparkSession


@pytest.fixture()
def spark(tmp_path):
    """
    Creates Spark Session for Tests
    """

    conf = SparkConf()
    conf.setAll([("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog"),
                 ("spark.sql.catalog.local.type", "hadoop"),
                 ("spark.sql.catalog.local.warehouse",
                  f"{posixpath.join(tmp_path.as_posix()), 'tmp', 'iceberg_warehouse'}"),
                 ("spark.jars.packages",
                  "org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.9.2")])
    spark = SparkSession.builder.config(conf=conf).getOrCreate()
    yield spark
    spark.stop()
