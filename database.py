import sqlite3

DB_NAME = "food_delivery.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT DEFAULT 'customer'
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS restaurants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS food (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            restaurant_id INTEGER,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            category TEXT,
            FOREIGN KEY (restaurant_id)
                REFERENCES restaurants(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            food_id INTEGER,
            quantity INTEGER,
            total REAL,
            status TEXT DEFAULT 'Ordered',
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (food_id) REFERENCES food(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            restaurant_id INTEGER,
            rating INTEGER,
            comment TEXT
        )
    """)

    conn.commit()
    conn.close()