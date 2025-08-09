"""
Tests for the Schema Factory
"""

from assertpy import assert_that

from schemas.factories import IcebergSchemaFactory


def test_game_info_schema():
    """
    Tests the Game Info Schema Structure
    """

    schema = IcebergSchemaFactory.game_info_schema()
    assert_that(schema.fieldNames()) \
        .contains_only(
        *['week', 'year', 'game_type', 'game_id', 'home_team', 'away_team', 'location',
          'city', 'state', 'game_date', 'is_conference', 'note', 'home_score',
          'away_score', 'line', 'over_under', 'sport'])


def test_schedules_schema():
    """
    Tests the Schedule Schema Structure
    """

    schema = IcebergSchemaFactory.schedules_schema()
    assert_that(schema.fieldNames()) \
        .contains_only(*['week', 'year', 'game_type', 'game_id', 'home_team', 'away_team',
                         'game_date', 'sport'])


def test_statistics_schema():
    """
    Tests the Statistics Schema Structure
    """
    schema = IcebergSchemaFactory.statistics_schema()
    assert_that(schema.fieldNames()) \
        .contains_only(*['player_name', 'player_url', 'statistic_code', 'statistic_name',
                         'statistic_value', 'statistic_type', 'team_name', 'opponent_name', 'week',
                         'year', 'game_type',
                         'game_date', 'sport'])


def test_team_statistics_schema():
    """
    Tests Team Statistics Schema Structure
    """
    schema = IcebergSchemaFactory.team_statistics_schema()
    assert_that(schema.fieldNames()) \
        .contains_only(
        *['team_name', 'team_url', 'statistic_name', 'statistic_value', 'opponent_name',
          'week', 'year', 'game_type', 'game_date', 'sport'])
