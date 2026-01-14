import sqlite3

class CSVDatabase:
    def __init__(self, db_path="all_csv_files.db"):
        # Runs automatically when the object is created.
        # Stores the database path and ensures the table exists.
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        # Creates the csv_files table if it does not exist.
        # The underscore (_) means this is an internal helper method.
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS csv_files (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE,
                    path TEXT NOT NULL
                );
            """)

    def add_csv(self, name, path):
        # Saves ONE CSV file into the database.
        # INSERT OR IGNORE prevents duplicates.
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT OR IGNORE INTO csv_files (name, path)
                VALUES (?, ?);
            """, (name, path))

    def get_all_csvs(self):
        # Returns all saved CSV file names.
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("SELECT id, name FROM csv_files;")
            return cur.fetchall()
