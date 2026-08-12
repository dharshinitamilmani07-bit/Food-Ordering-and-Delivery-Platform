USERS = [
    {
        "name": "Admin",
        "email": "admin@gmail.com",
        "password": "1234"
    },
    {
        "name": "User",
        "email": "user@gmail.com",
        "password": "1234"
    }
]


def check_login(email, password):

    for user in USERS:

        if user["email"] == email and user["password"] == password:
            return True

    return False


def register(name, email, password):

    for user in USERS:

        if user["email"] == email:
            return False

    USERS.append({
        "name": name,
        "email": email,
        "password": password
    })

    return True