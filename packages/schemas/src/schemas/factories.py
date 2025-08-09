"""
Schema Factories
"""

from pyspark.sql.types import (
    BooleanType,
    FloatType,
    IntegerType,
    LongType,
    StringType,
    StructField,
    StructType,
    TimestampType,
)


class IcebergSchemaFactory:
    """
    Factory for generating iceberg Spark Schemas
    """

    _common_fields_ = {
        'week': IntegerType(),
        'year': IntegerType(),
        'game_type': StringType(),
        'sport': StringType(),
    }

    @classmethod
    def _generate_schema_(cls, fields: dict) -> StructType:
        """
        Generates the Schema from a Dictionary.
        :param fields: Dictionary of fields
        :return: Struct Type
        """
        schema_fields = []
        for item in fields.items():
            schema_fields.append(StructField(item[0], item[1], True))
        return StructType(fields=schema_fields)

    @classmethod
    def statistics_schema(cls) -> StructType:
        """
        Generates the Statistics Iceberg Table Schema
        :return: StructType
        """
        return cls._generate_schema_(
            {
                **cls._common_fields_,
                'player_name': StringType(),
                'player_url': StringType(),
                'statistic_code': StringType(),
                'statistic_name': StringType(),
                'statistic_type': StringType(),
                'statistic_value': FloatType(),
                'team_name': StringType(),
                'opponent_name': StringType(),
                'game_date': TimestampType(),
            }
        )

    @classmethod
    def team_statistics_schema(cls) -> StructType:
        """
        Generates the Team Statistics Iceberg Table Schema
        :return: StructType
        """
        return cls._generate_schema_(
            {
                **cls._common_fields_,
                'team_name': StringType(),
                'team_url': StringType(),
                'statistic_name': StringType(),
                'statistic_value': FloatType(),
                'opponent_name': StringType(),
                'game_date': TimestampType(),
            }
        )

    @classmethod
    def game_info_schema(cls) -> StructType:
        """
        Generates the Game Info Table Schema
        :return: StructType
        """
        return cls._generate_schema_(
            {
                'game_id': LongType(),
                'home_team': StringType(),
                'away_team': StringType(),
                'location': StringType(),
                'city': StringType(),
                'state': StringType(),
                'game_date': TimestampType(),
                'is_conference': BooleanType(),
                'note': StringType(),
                'home_score': IntegerType(),
                'away_score': IntegerType(),
                'line': StringType(),
                'over_under': FloatType(),
                **cls._common_fields_,
            }
        )

    @classmethod
    def schedules_schema(cls) -> StructType:
        """
        Generates the Schedule Table Schema
        :return: StructType
        """
        return cls._generate_schema_(
            {
                **cls._common_fields_,
                'game_id': LongType(),
                'home_team': StringType(),
                'away_team': StringType(),
                'game_date': TimestampType(),
            }
        )
