import tkinter as tk
from tkinter import messagebox
from home import open_home


def login_page(root):

    tk.Label(
        root,
        text="🍔 FOOD ORDERING",
        font=("Arial", 24, "bold")
    ).pack(pady=40)

    tk.Label(
        root,
        text="Email"
    ).pack()

    email_entry = tk.Entry(
        root,
        width=35
    )
    email_entry.pack(pady=10)

    tk.Label(
        root,
        text="Password"
    ).pack()

    password_entry = tk.Entry(
        root,
        width=35,
        show="*"
    )
    password_entry.pack(pady=10)

    def login():

        email = email_entry.get()
        password = password_entry.get()

        if email == "user@gmail.com" and password == "1234":

            messagebox.showinfo(
                "Login Successful",
                "Welcome!"
            )

            root.destroy()
            open_home()

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid Email or Password!"
            )

    tk.Button(
        root,
        text="LOGIN",
        width=25,
        command=login
    ).pack(pady=25)