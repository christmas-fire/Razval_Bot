import sqlite3 as sq


async def db_start() -> None:
    global db, cur
    
    db = sq.connect("MassageAssistant.db")
    cur = db.cursor()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS users(
        id INTEGER,
        username TEXT,
        name TEXT)
                """
    )

    db.commit()
    
    
async def add_user(id, username, name):
    user = cur.execute(f"SELECT 1 FROM users WHERE id == {id}").fetchone()
    if not user:
        cur.execute("INSERT INTO users VALUES(?, ?, ?)",
                    (id, username, name))
        db.commit()