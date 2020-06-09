import sqlite3 as sqlite


DB_NAME = "server/database/mista.db"

conn = sqlite.connect(DB_NAME)

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS games
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        reviews TEXT NOT NULL,
        release_data TEXT NOT NULL,
        developer TEXT NOT NULL,
		publisher TEXT NOT NULL,
        genre TEXT NOT NULL,
        minimum_requirements TEXT NOT NULL,
        recommended_requirements TEXT NOT NULL,
		price TEXT NOT NULL
    )
''')
conn.commit()


class Database:
    def __enter__(self):
        self.conn = sqlite.connect(DB_NAME)
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()
