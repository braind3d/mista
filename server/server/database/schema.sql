CREATE TABLE IF NOT EXISTS details (
    detail_id INTEGER PRIMARY KEY,
    detail_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS developers (
    developer_id INTEGER PRIMARY KEY,
    developer_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS games (
    game_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    desc_snippet TEXT NOT NULL,
    recent_reviews TEXT NOT NULL,
    all_reviews TEXT NOT NULL,
    release_date TEXT NOT NULL,
    achievements TEXT NOT NULL,
    description TEXT NOT NULL,
    minimum_requirements TEXT NOT NULL,
    recommended_requirements TEXT NOT NULL,
    original_price NUMERIC NOT NULL
);

CREATE TABLE IF NOT EXISTS game_details (
    game_id INTEGER NOT NULL,
    detail_id INTEGER NOT NULL,
    FOREIGN KEY (game_id) REFERENCES games (game_id),
    FOREIGN KEY (detail_id) REFERENCES details (detail_id)
);

CREATE TABLE IF NOT EXISTS game_developers (
    game_id INTEGER NOT NULL,
    developer_id INTEGER NOT NULL,
    FOREIGN KEY (game_id) REFERENCES games (game_id),
    FOREIGN KEY (developer_id) REFERENCES developers (developer_id)
);

CREATE TABLE IF NOT EXISTS game_genres (
    game_id INTEGER NOT NULL,
    genre_id INTEGER NOT NULL,
    FOREIGN KEY (game_id) REFERENCES games (game_id),
    FOREIGN KEY (genre_id) REFERENCES genres (genre_id)
);

CREATE TABLE IF NOT EXISTS game_languages (
    game_id INTEGER NOT NULL,
    language_id INTEGER NOT NULL,
    FOREIGN KEY (game_id) REFERENCES games (game_id),
    FOREIGN KEY (language_id) REFERENCES languages (language_id)
);

CREATE TABLE IF NOT EXISTS game_popular_tags (
    game_id INTEGER NOT NULL,
    popular_tag_id INTEGER NOT NULL,
    FOREIGN KEY (game_id) REFERENCES games (game_id),
    FOREIGN KEY (popular_tag_id) REFERENCES popular_tags (popular_tag_id)
);

CREATE TABLE IF NOT EXISTS game_publishers (
    game_id INTEGER NOT NULL,
    publisher_id INTEGER NOT NULL,
    FOREIGN KEY (game_id) REFERENCES games (game_id),
    FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id)
);

CREATE TABLE IF NOT EXISTS genres (
    genre_id INTEGER PRIMARY KEY,
    genre_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS languages (
    language_id INTEGER PRIMARY KEY,
    language_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS popular_tags (
    popular_tag_id INTEGER PRIMARY KEY,
    popular_tag_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS publishers (
    publisher_id INTEGER PRIMARY KEY,
    publisher_name TEXT NOT NULL
);