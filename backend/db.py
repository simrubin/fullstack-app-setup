import sqlite3
import os
from datetime import datetime

def get_db_connection():
    # Create db in backend directory - this will be /app/db/app.db which maps to ./backend/db/
    os.makedirs("db", exist_ok=True)
    conn = sqlite3.connect("db/app.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute(
        """CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY,
            content TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )"""
    )
    
    # Check if table is empty and add sample data
    count = conn.execute("SELECT COUNT(*) FROM messages").fetchone()[0]
    if count == 0:
        sample_messages = [
            ("Hello, how are you?", datetime.now().isoformat()),
            ("This is a test!", datetime.now().isoformat()),

        ]
        conn.executemany("INSERT INTO messages (content, timestamp) VALUES (?, ?)", sample_messages)
        print("[INFO] Sample data added to database")
    
    conn.commit()
    conn.close()