CREATE TABLE #CATALOG.#DATABASE.team_statistics (
    team_name STRING,
    team_url STRING,
    statistic_name STRING,
    statistic_value FLOAT,
    opponent_name STRING,
    week INTEGER,
    year INTEGER,
    game_type STRING,
    game_date TIMESTAMP,
    sport STRING
)
PARTITIONED BY (sport,year)
TBLPROPERTIES ('format-version'='2')