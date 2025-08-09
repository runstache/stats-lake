CREATE TABLE #CATALOG.#DATABASE.statistics (
    player_name STRING,
    player_url STRING,
    statistic_code STRING,
    statistic_name STRING,
    statistic_value FLOAT,
    statistic_type STRING,
    team_name STRING,
    opponent_name STRING,
    week INTEGER,
    year INTEGER,
    game_type STRING,
    game_date TIMESTAMP,
    sport STRING
)
PARTITIONED BY (sport,year)
TBLPROPERTIES ('format-version'='2')