import sqlite3
import os
import pandas as pd

DB_PATH = "all_csv_files.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS csv_files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            path TEXT NOT NULL
        );
    """)

    conn.commit()
    conn.close()

def create_csv_files_table():
    conn = sqlite3.connect("all_csv_files.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS csv_files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            path TEXT NOT NULL);""")

    conn.commit()
    conn.close()

def csv_in_database(csv_folder_path, database_name):
    conn = sqlite3.connect(database_name)
    cur = conn.cursor()

    # make sure table exists
    cur.execute("""
        CREATE TABLE IF NOT EXISTS csv_files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            path TEXT NOT NULL
        );
    """)

    # insert files
    for filename in os.listdir(csv_folder_path):
        if filename.endswith(".csv"):
            full_path = os.path.join(csv_folder_path, filename)

            cur.execute("INSERT INTO csv_files (name, path) VALUES (?, ?)", 
                        (filename, full_path))

    conn.commit()
    conn.close()

def get_all_links():
    conn = sqlite3.connect("all_csv_files.db")
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM csv_files")
    rows = cur.fetchall()

    conn.close()
    return rows





  