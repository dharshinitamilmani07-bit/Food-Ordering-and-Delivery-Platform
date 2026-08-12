import tkinter as tk
from food_data import foods
from cart import add_to_cart, view_cart


def view_food(home_window):

    food_window = tk.Toplevel(home_window)

    food_window.title("Food Menu")
    food_window.geometry("600x600")

    tk.Label(
        food_window,
        text="FOOD MENU",
        font=("Arial", 22, "bold")
    ).pack(pady=25)

    for name, price in foods:

        frame = tk.Frame(food_window)
        frame.pack(pady=8)

        tk.Label(
            frame,
            text=f"{name} - Rs. {price}",
            width=30,
            font=("Arial", 12)
        ).pack(side="left")

        tk.Button(
            frame,
            text="ADD TO CART",
            command=lambda n=name, p=price:
            add_to_cart(n, p)
        ).pack(side="left", padx=10)

    tk.Button(
        food_window,
        text="VIEW CART",
        width=20,
        command=lambda: view_cart(home_window)
    ).pack(pady=30)