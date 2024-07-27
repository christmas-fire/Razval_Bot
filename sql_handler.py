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
    cur.execute(
        """CREATE TABLE IF NOT EXISTS orders(
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


async def add_order(user_id, username, name) -> None:
    """
    Добавляет пользователя, который сделал заказ в таблицу, если такого пользователя еще нет в таблице

    :param user_id: id пользователя в telegram
    :param username: Имя пользователя в telegram
    :param name: Имя пользователя в telegram (first name)
    """
    user = cur.execute(f"SELECT 1 FROM orders WHERE id == {user_id}").fetchone()
    if not user:
        cur.execute("INSERT INTO orders (id, username, name) VALUES(?, ?, ?)",
                    (user_id, username, name))
        db.commit()


async def get_users_id() -> list:
    """
    Возвращает список кортежей (один кортеж - это один id пользователя)
    """
    users_id = cur.execute(f"SELECT id FROM users").fetchall()
    db.commit()
    return users_id


async def get_users_username() -> list:
    """
    Возвращает список кортежей (один кортеж - это один username пользователя)
    """
    users_username = cur.execute(f"SELECT username FROM users").fetchall()
    db.commit()
    return users_username


async def get_orders_username() -> list:
    """
    Возвращает список кортежей (один кортеж - это один username пользователя, который сделал заказ)
    """
    orders_username = cur.execute(f"SELECT username FROM orders").fetchall()
    db.commit()
    return orders_username
