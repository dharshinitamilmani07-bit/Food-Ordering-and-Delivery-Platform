import tkinter as tk
from login import login_page
from admin import admin_page


def open_admin():

    admin_login = tk.Toplevel()

    admin_login.title("Admin Login")
    admin_login.geometry("450x400")

    tk.Label(
        admin_login,
        text="ADMIN LOGIN",
        font=("Arial", 22, "bold")
    ).pack(pady=40)

    tk.Label(
        admin_login,
        text="Username"
    ).pack()

    username = tk.Entry(
        admin_login,
        width=30
    )
    username.pack(pady=10)

    tk.Label(
        admin_login,
        text="Password"
    ).pack()

    password = tk.Entry(
        admin_login,
        width=30,
        show="*"
    )
    password.pack(pady=10)

    def check_admin():

        if username.get() == "admin" and password.get() == "1234":

            admin_login.destroy()
            admin_page()

        else:

            tk.messagebox.showerror(
                "Error",
                "Invalid Admin Login"
            )

    tk.Button(
        admin_login,
        text="LOGIN",
        width=20,
        command=check_admin
    ).pack(pady=25)


root = tk.Tk()

root.title("Food Ordering & Delivery")
root.geometry("500x550")

login_page(root)

tk.Button(
    root,
    text="ADMIN LOGIN",
    width=25,
    command=open_admin
).pack(pady=20)

root.mainloop()