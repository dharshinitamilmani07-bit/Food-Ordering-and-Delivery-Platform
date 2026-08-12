import tkinter as tk
from tkinter import messagebox
from user import check_login
from home import open_home


def login_page(root):

    for widget in root.winfo_children():
        widget.destroy()

    root.title("Food Ordering - Login")
    root.geometry("500x500")

    tk.Label(
        root,
        text="FOOD ORDERING",
        font=("Arial", 24, "bold")
    ).pack(pady=40)

    tk.Label(
        root,
        text="Email",
        font=("Arial", 14)
    ).pack()

    email_entry = tk.Entry(root, width=35)
    email_entry.pack(pady=10)

    tk.Label(
        root,
        text="Password",
        font=("Arial", 14)
    ).pack()

    password_entry = tk.Entry(
        root,
        width=35,
        show="*"
    )
    password_entry.pack(pady=10)

    def login():

        email = email_entry.get().strip()
        password = password_entry.get()

        if check_login(email, password):

            messagebox.showinfo(
                "Success",
                "Login Successful!"
            )

            root.destroy()
            open_home()

        else:

            messagebox.showerror(
                "Error",
                "Invalid User ID or Password!"
            )

    tk.Button(
        root,
        text="LOGIN",
        width=25,
        command=login
    ).pack(pady=25)