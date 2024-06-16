import sqlite3 as sq
from datetime import datetime

current_time = datetime.now().replace(microsecond=0)


async def db_start() -> None:
    global db, cur
    
    db = sq.connect("RazvalBot.db")
    cur = db.cursor()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS users(
        id_user INTEGER PRIMARY KEY AUTOINCREMENT,
        id INTEGER,
        username TEXT,
        name TEXT)
        """
    )
    db.commit()
    
async def add_user(id, username, name) -> None:
    """
    Добавляет пользователя в таблицу, если такого пользователя еще нет в таблице
    """
    user = cur.execute(f"SELECT 1 FROM users WHERE id == {id}").fetchone()
    if not user:
        cur.execute("INSERT INTO users (id, username, name) VALUES(?, ?, ?)",
                    (id, username, name))
        db.commit()
        
async def get_users() -> list:
    """
    Возвращает список кортежей (один кортеж - это один id-шник)
    """
    users = cur.execute(f"SELECT id FROM users").fetchall()
    db.commit()
    return users