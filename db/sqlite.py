import sqlite3
from core.config import settings

conn = sqlite3.connect("db/chat.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS chats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message TEXT,
    response TEXT,
    timestamp TEXT,
    user_id TEXT,
    session_id TEXT,
    intent TEXT,
    response_length INTEGER,
    language TEXT,
    processing_time REAL,
    tool_used TEXT
)
""")
conn.commit()

def insert_chat(data: dict):
    cursor.execute("""
    INSERT INTO chats (
        message, response, timestamp,
        user_id, session_id, intent,
        response_length, language, processing_time, tool_used
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["message"],
        data["response"],
        data["timestamp"],
        data["user_id"],
        data["session_id"],
        data["intent"],
        data["response_length"],
        data["language"],
        data["processing_time"],
        data["tool_used"]
    ))
    conn.commit()
