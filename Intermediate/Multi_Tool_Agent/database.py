import sqlite3

conn = sqlite3.connect(
    "searches.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS searches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    query TEXT,
    result TEXT
)
""")

conn.commit()


def save_search(query, result):

    cursor.execute(
        "INSERT INTO searches (query, result) VALUES (?, ?)",
        (query, result)
    )

    conn.commit()


def get_history():

    cursor.execute(
        "SELECT query, result FROM searches"
    )

    return cursor.fetchall()