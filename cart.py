import tkinter as tk
from tkinter import messagebox

from order import add_order
from payment import payment_page

cart = []


def add_to_cart(name, price):

    cart.append((name, price))

    messagebox.showinfo(
        "Cart",
        f"{name} added to cart!"
    )


def view_cart(home_window):

    cart_window = tk.Toplevel(home_window)

    cart_window.title("My Cart")
    cart_window.geometry("550x600")

    tk.Label(
        cart_window,
        text="MY CART",
        font=("Arial", 22, "bold")
    ).pack(pady=25)

    if not cart:

        tk.Label(
            cart_window,
            text="Your cart is empty.",
            font=("Arial", 14)
        ).pack(pady=30)

        return

    total = 0

    for name, price in cart:

        tk.Label(
            cart_window,
            text=f"{name} - Rs. {price}",
            font=("Arial", 13)
        ).pack(pady=5)

        total += price

    tk.Label(
        cart_window,
        text=f"Total: Rs. {total}",
        font=("Arial", 17, "bold")
    ).pack(pady=20)


    def create_order():

        if not cart:

            messagebox.showwarning(
                "Order",
                "Your cart is empty!"
            )

            return

        order = add_order(cart, total)

        payment_page(
            home_window,
            order,
            cart_window
        )


    tk.Button(
        cart_window,
        text="PLACE ORDER",
        width=25,
        height=2,
        command=create_order
    ).pack(pady=15)


    tk.Button(
        cart_window,
        text="CLOSE",
        width=25,
        command=cart_window.destroy
    ).pack(pady=10)