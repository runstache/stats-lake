"""
Job for applying the DDL Schemas in Iceberg
"""

import argparse
import logging
import os

from pyspark.sql import SparkSession
from pyspark.sql.functions import col


def sanitize_sql(sql_string: str, catalog: str, database: str) -> str:
    """
    Replaces the Catalog and Database in the SQL String.
    :param sql_string: SQL String
    :param catalog: Catalog Name
    :param database: Database Name
    :return: SQL String
    """

    new_sql = sql_string.replace('#DATABASE', database).replace('#CATALOG', catalog)
    return new_sql


def main(db_name: str, catalog_id: str, ddl_path: str, spark_session: SparkSession) -> None:
    """
    Executes the SQL Files in the provided DDL Location
    :param db_name: Iceberg Database Name
    :param catalog_id: Catalog Id
    :param ddl_path: Path to the DDL Files
    :param spark_session: Spark Session
    :return: None
    """

    logger = logging.getLogger(__name__)
    logger.info('Checking for Database: %s', db_name)
    databases = spark_session.sql('SHOW DATABASES')
    if databases.filter(col('namespace') == db_name).isEmpty():
        logger.info('Database %s no found. Created...', db_name)
        spark_session.sql(f'CREATE DATABASE {db_name}')

    ddl_files = os.listdir(ddl_path)

    statements = []
    for file in ddl_files:
        with open(os.path.join(ddl_path, file)) as sql_file:
            content = sql_file.read()
            statements.append(sanitize_sql(content, catalog_id, db_name))

    for statement in statements:
        try:
            spark_session.sql(statement)
        except Exception:
            logger.error('Failed to execute statement: %s', statement)

    logger.info('Finished Applying Schema')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--database', type=str, required=True, help='Iceberg Database Name')
    parser.add_argument('-c', '--catalog', type=str, required=True, help='Iceberg Catalog Id')
    parser.add_argument('-s', '--sql', type=str, required=True, help='DDL Path')
    parser.add_argument('-i', '--ip', type=str, required=True, help='Spark Connect IP')
    args = parser.parse_args()

    spark = SparkSession.builder.appName('cluster').remote(f'sc://{args.ip}:15002').getOrCreate()
    main(args.database, args.catalog, args.sql, spark)
