import tkinter as tk
from tkinter import messagebox

from order import orders
from food import view_food
from cart import view_cart
from restaurant import view_restaurants
from delivery import delivery_page
from review import review_page


def my_orders(home_window):

    order_window = tk.Toplevel(home_window)

    order_window.title("My Orders")
    order_window.geometry("550x600")

    tk.Label(
        order_window,
        text="MY ORDERS",
        font=("Arial", 22, "bold")
    ).pack(pady=25)

    if not orders:

        tk.Label(
            order_window,
            text="No orders available.",
            font=("Arial", 14)
        ).pack(pady=30)

        return

    for i, order in enumerate(orders, 1):

        tk.Label(
            order_window,
            text=f"Order {i}",
            font=("Arial", 16, "bold")
        ).pack(pady=5)

        for name, price in order["items"]:

            tk.Label(
                order_window,
                text=f"{name} - Rs. {price}"
            ).pack()

        tk.Label(
            order_window,
            text=f"Total: Rs. {order['total']}",
            font=("Arial", 13, "bold")
        ).pack(pady=5)

        tk.Label(
            order_window,
            text=f"Payment: {order.get('payment', 'Pending')}"
        ).pack()

        tk.Label(
            order_window,
            text=f"Order Status: {order['status']}"
        ).pack()

        tk.Label(
            order_window,
            text=f"Delivery Status: "
                 f"{order.get('delivery_status', 'Order Confirmed')}"
        ).pack(pady=10)

        tk.Label(
            order_window,
            text="-----------------------------"
        ).pack()


def open_home():

    home_window = tk.Tk()

    home_window.title("Food Ordering & Delivery")
    home_window.geometry("600x750")

    # TITLE

    tk.Label(
        home_window,
        text="FOOD ORDERING & DELIVERY",
        font=("Arial", 22, "bold")
    ).pack(pady=30)

    tk.Label(
        home_window,
        text="Welcome to our Food Ordering App!",
        font=("Arial", 14)
    ).pack(pady=10)

    # VIEW FOOD

    tk.Button(
        home_window,
        text="VIEW FOOD",
        width=30,
        height=2,
        command=lambda: view_food(home_window)
    ).pack(pady=8)

    # RESTAURANTS

    tk.Button(
        home_window,
        text="RESTAURANTS",
        width=30,
        height=2,
        command=view_restaurants
    ).pack(pady=8)

    # MY CART

    tk.Button(
        home_window,
        text="MY CART",
        width=30,
        height=2,
        command=lambda: view_cart(home_window)
    ).pack(pady=8)

    # MY ORDERS

    tk.Button(
        home_window,
        text="MY ORDERS",
        width=30,
        height=2,
        command=lambda: my_orders(home_window)
    ).pack(pady=8)

    # DELIVERY TRACKING

    tk.Button(
        home_window,
        text="DELIVERY TRACKING",
        width=30,
        height=2,
        command=lambda: delivery_page(
            home_window,
            orders[-1]
        ) if orders else messagebox.showwarning(
            "Delivery",
            "Please place an order first!"
        )
    ).pack(pady=8)

    # REVIEW & RATING

    tk.Button(
        home_window,
        text="REVIEW & RATING",
        width=30,
        height=2,
        command=lambda: review_page(
            home_window,
            orders[-1]
        ) if orders else messagebox.showwarning(
            "Review",
            "Please place an order first!"
        )
    ).pack(pady=8)

    # EXIT

    tk.Button(
        home_window,
        text="EXIT",
        width=30,
        height=2,
        command=home_window.destroy
    ).pack(pady=15)

    home_window.mainloop()