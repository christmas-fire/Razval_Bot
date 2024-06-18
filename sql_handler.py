import sqlite3 as sq

db = sq.connect("RazvalBot.db")
cur = db.cursor()


async def db_start() -> None:
    """
    Создание и запуск БД
    """
    cur.execute(
        """CREATE TABLE IF NOT EXISTS users(
        id_user INTEGER PRIMARY KEY AUTOINCREMENT,
        id INTEGER,
        username TEXT,
        name TEXT)
        """
    )
    db.commit()


async def add_user(user_id, username, name) -> None:
    """
    Добавляет пользователя в таблицу, если такого пользователя еще нет в таблице

    :param user_id: id пользователя в telegram
    :param username: Имя пользователя в telegram
    :param name: Имя пользователя в telegram (first name)
    """
    user = cur.execute(f"SELECT 1 FROM users WHERE id == {user_id}").fetchone()
    if not user:
        cur.execute("INSERT INTO users (id, username, name) VALUES(?, ?, ?)",
                    (user_id, username, name))
        db.commit()


async def get_users() -> list:
    """
    Возвращает список кортежей (один кортеж - это один id пользователя)
    """
    users = cur.execute(f"SELECT id FROM users").fetchall()
    db.commit()
    return users
