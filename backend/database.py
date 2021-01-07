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


def insert_unit(unit):
    conn = connect_db()
    c = conn.cursor()
    unit_data = (unit.first_name,
                 unit.last_name,
                 unit.short_bio,
                 unit.long_bio,
                 unit.birthday,
                 unit.telegram,
                 unit.github,)
    fields = "first_name, last_name, short_bio, long_bio, birthday, telegram, github"
    c.execute(f"INSERT INTO units({fields}) VALUES (?, ?, ?, ?, ?, ?, ?)", unit_data)
    conn.commit()
    conn.close()
    return f"Юнит {unit.first_name} {unit.last_name} добавлен"


def delete_query(table, pk):
    conn = connect_db()
    c = conn.cursor()
    c.execute(f"DELETE FROM {table} WHERE id={pk}")
    conn.commit()
    conn.close()
