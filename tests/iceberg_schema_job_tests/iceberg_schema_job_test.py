"""
Tests for the Iceberg Schema Job
"""

from assertpy import assert_that
from src.schema_job import iceberg_schema_job

def test_sanitize_sql():
    """
    Tests the SanitizeSQL function
    """

    sql = 'CREATE DATABASE #CATALOG.#DATABASE'

    result = iceberg_schema_job.sanitize_sql(sql, 'my_catalog', 'my_database')
    assert_that(result).is_equal_to('CREATE DATABASE my_catalog.my_database')

def test_main_fresh(spark):
    """
    Tests the Main Function without the Database existing
    """

    iceberg_schema_job.main('my_database', 'local', './ddl', spark)

    databases = spark.sql('SHOW DATABASES')

    assert_that(databases.count()).is_equal_to(2)

    tables = spark.sql('SHOW TABLES in local.my_database')

    assert_that(tables.count()).is_equal_to(4)

    spark.sql('DROP DATABASE my_database')

def test_main_exiisting_database(spark):
    """
    Tests the Main Function with an existing Database
    """
    spark.sql('CREATE DATABASE my_database')

    iceberg_schema_job.main('my_database', 'local', './ddl', spark)

    databases = spark.sql('SHOW DATABASES')
    assert_that(databases.count()).is_equal_to(2)

    tables = spark.sql('SHOW TABLES in local.my_database')

    assert_that(tables.count()).is_equal_to(4)

    spark.sql('DROP DATABASE my_database')

