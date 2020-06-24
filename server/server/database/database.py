import sqlite3 as sqlite


DB_NAME = "server/database/mista.db"

conn = sqlite.connect(DB_NAME)

conn.commit()

class Database:
    def __enter__(self):
        self.conn = sqlite.connect(DB_NAME)
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()
