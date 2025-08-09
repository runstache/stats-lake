CREATE TABLE #CATALOG.#DATABASE.game_info (
    week INT,
    year INT,
    game_type STRING,
    game_id BIGINT,
    home_team STRING,
    away_team STRING,
    location STRING,
    city STRING,
    state STRING,
    game_date TIMESTAMP,
    is_conference BOOLEAN,
    note STRING,
    home_score INT,
    away_score INT,
    line STRING,
    over_under FLOAT,
    sport STRING
)
PARTITIONED BY (sport,year)
TBLPROPERTIES ('format-version'='2')
