import sqlite3


database = "sqlite3.db"


def connect_db():
    conn = sqlite3.connect(database)
    c = conn.cursor()

    try:
        c.execute("CREATE TABLE units (id integer primary key, first_name text, last_name text,"
                  "short_bio text, long_bio text, birthday date, telegram text, github text)")
        conn.commit()
    except sqlite3.OperationalError:
        print("База данных уже существует")

    return conn


def select_query(table):
    conn = connect_db()
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute(f"SELECT * FROM {table}")
    result = [dict(row) for row in c.fetchall()]
    return result
