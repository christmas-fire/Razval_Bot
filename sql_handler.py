import sqlite3 as sq
from datetime import datetime

current_time = datetime.now().replace(microsecond=0)

async def db_start() -> None:
    global db, cur
    
    db = sq.connect("RazvalBot.db")
    cur = db.cursor()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        username TEXT,
        name TEXT)
        """
    )

    cur.execute(
        """CREATE TABLE IF NOT EXISTS orders(
        order_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        date DATETIME,
        FOREIGN KEY (user_id) REFERENCES users (id))
        """
    )
    
    db.commit()
    
async def add_user(id, username, name):
    user = cur.execute(f"SELECT 1 FROM users WHERE id == {id}").fetchone()
    if not user:
        cur.execute("INSERT INTO users VALUES(?, ?, ?)",
                    (id, username, name))
        db.commit()