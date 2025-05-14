import sqlite3
import os


class DB:
    PROJECT_DIR: str = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, URI: str):
        self.URI: str = os.path.join(self.PROJECT_DIR, URI)
        self.conn: sqlite3.Connection = sqlite3.connect(
            self.URI, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.cursor: sqlite3.Cursor = self.conn.cursor()

    def execute(self, query, params=(), fetch='all'):
        self.cursor.execute(query, params)
        self.conn.commit()

        if fetch == 'all':
            return [dict(row) for row in self.cursor.fetchall()]
        elif fetch == 'one':
            row = self.cursor.fetchone()
            return dict(row) if row else None
        else:
            return None

    def close(self):
        self.conn.close()
