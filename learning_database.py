"""Persistent storage for upload-limit learning."""

import sqlite3
from pathlib import Path

DB_NAME = "automation_learning.db"

def initialize(db_path=DB_NAME):
    conn = sqlite3.connect(db_path)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS upload_events(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            upload_count INTEGER,
            file_size INTEGER,
            cooldown_minutes INTEGER,
            refresh_required INTEGER
        )
    """)
    conn.commit()
    return conn

def add_event(conn, timestamp, upload_count, file_size, cooldown_minutes, refresh_required):
    conn.execute(
        "INSERT INTO upload_events(timestamp,upload_count,file_size,cooldown_minutes,refresh_required) VALUES (?,?,?,?,?)",
        (timestamp, upload_count, file_size, cooldown_minutes, int(refresh_required)),
    )
    conn.commit()

def recent_events(conn, limit=25):
    return conn.execute(
        "SELECT * FROM upload_events ORDER BY id DESC LIMIT ?",
        (limit,)
    ).fetchall()
