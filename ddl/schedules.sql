CREATE TABLE #CATALOG.#DATABASE.schedules (
    week INT,
    year INT,
    game_type STRING,
    game_id BIGINT,
    home_team STRING,
    away_team STRING,
    game_date TIMESTAMP,
    sport STRING
)
PARTITIONED BY (sport,year)
TBLPROPERTIES ('format-version'='2')
