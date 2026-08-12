import tkinter as tk
from tkinter import messagebox

from restaurant_data import restaurant_list


def add_restaurant():

    window = tk.Toplevel()

    window.title("Add Restaurant")
    window.geometry("450x350")

    tk.Label(
        window,
        text="ADD RESTAURANT",
        font=("Arial", 22, "bold")
    ).pack(pady=30)

    tk.Label(
        window,
        text="Restaurant Name"
    ).pack()

    name_entry = tk.Entry(
        window,
        width=35
    )

    name_entry.pack(pady=15)

    def save_restaurant():

        name = name_entry.get().strip()

        if name == "":
            messagebox.showwarning(
                "Warning",
                "Please enter restaurant name!"
            )
            return

        restaurant_list.append(name)

        messagebox.showinfo(
            "Success",
            f"{name} added successfully!"
        )

        window.destroy()

    tk.Button(
        window,
        text="SAVE RESTAURANT",
        width=25,
        command=save_restaurant
    ).pack(pady=25)


def view_restaurants():

    window = tk.Toplevel()

    window.title("Restaurants")
    window.geometry("500x500")

    tk.Label(
        window,
        text="RESTAURANTS",
        font=("Arial", 22, "bold")
    ).pack(pady=25)

    for restaurant in restaurant_list:

        tk.Label(
            window,
            text="🏪 " + restaurant,
            font=("Arial", 13)
        ).pack(pady=8)