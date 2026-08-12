from database import connect


def register():
    print("\n========== 📝 REGISTER ==========")

    name = input("Enter Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    conn = connect()

    try:
        conn.execute("""
            INSERT INTO users
            (name, email, password)
            VALUES (?, ?, ?)
        """, (name, email, password))

        conn.commit()

        print("\n✅ Registration successful!")

    except sqlite3.IntegrityError:
        print("\n❌ Email already exists!")

    conn.close()


def view_users():
    conn = connect()

    users = conn.execute("""
        SELECT id, name, email, role
        FROM users
    """).fetchall()

    conn.close()

    print("\n========== 👥 USERS ==========")

    for user in users:
        print(
            f"ID: {user[0]} | "
            f"Name: {user[1]} | "
            f"Email: {user[2]} | "
            f"Role: {user[3]}"
        )