import tkinter as tk
from tkinter import messagebox

from order import orders


# -----------------------------
# ADD FOOD
# -----------------------------
def add_food():

    window = tk.Toplevel()
    window.title("Add Food")
    window.geometry("400x350")

    tk.Label(
        window,
        text="ADD FOOD",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    tk.Label(window, text="Food Name").pack()
    name_entry = tk.Entry(window, width=30)
    name_entry.pack(pady=5)

    tk.Label(window, text="Price").pack()
    price_entry = tk.Entry(window, width=30)
    price_entry.pack(pady=5)

    def save_food():

        name = name_entry.get()
        price = price_entry.get()

        if name == "" or price == "":
            messagebox.showwarning(
                "Food",
                "Enter food name and price!"
            )
            return

        messagebox.showinfo(
            "Food",
            f"{name} added successfully!\nPrice: Rs. {price}"
        )

        window.destroy()

    tk.Button(
        window,
        text="ADD FOOD",
        width=20,
        command=save_food
    ).pack(pady=25)


# -----------------------------
# VIEW FOOD
# -----------------------------
def view_food_admin():

    window = tk.Toplevel()
    window.title("Food Menu")
    window.geometry("450x500")

    tk.Label(
        window,
        text="FOOD MENU",
        font=("Arial", 22, "bold")
    ).pack(pady=25)

    foods = [
        ("Chicken Biryani", 150),
        ("Chicken Fried Rice", 140),
        ("Pizza", 200),
        ("Burger", 120),
        ("Veg Meals", 100),
        ("Chicken Noodles", 130)
    ]

    for name, price in foods:

        tk.Label(
            window,
            text=f"{name} - Rs. {price}",
            font=("Arial", 13)
        ).pack(pady=7)


# -----------------------------
# ADD RESTAURANT
# -----------------------------
def add_restaurant():

    window = tk.Toplevel()
    window.title("Add Restaurant")
    window.geometry("400x300")

    tk.Label(
        window,
        text="ADD RESTAURANT",
        font=("Arial", 20, "bold")
    ).pack(pady=25)

    tk.Label(
        window,
        text="Restaurant Name"
    ).pack()

    restaurant_entry = tk.Entry(
        window,
        width=30
    )
    restaurant_entry.pack(pady=10)

    def save_restaurant():

        name = restaurant_entry.get()

        if name == "":
            messagebox.showwarning(
                "Restaurant",
                "Enter restaurant name!"
            )
            return

        messagebox.showinfo(
            "Restaurant",
            f"{name} added successfully!"
        )

        window.destroy()

    tk.Button(
        window,
        text="ADD RESTAURANT",
        width=20,
        command=save_restaurant
    ).pack(pady=20)


# -----------------------------
# VIEW ORDERS
# -----------------------------
def view_orders_admin():

    window = tk.Toplevel()

    window.title("ALL ORDERS")
    window.geometry("600x650")

    tk.Label(
        window,
        text="ALL ORDERS",
        font=("Arial", 22, "bold")
    ).pack(pady=25)

    if not orders:

        tk.Label(
            window,
            text="No orders available.",
            font=("Arial", 14)
        ).pack(pady=30)

        return

    for i, order in enumerate(orders, 1):

        tk.Label(
            window,
            text=f"ORDER {i}",
            font=("Arial", 16, "bold")
        ).pack(pady=8)

        for name, price in order["items"]:

            tk.Label(
                window,
                text=f"{name} - Rs. {price}"
            ).pack()

        tk.Label(
            window,
            text=f"Total: Rs. {order['total']}",
            font=("Arial", 13, "bold")
        ).pack(pady=5)

        tk.Label(
            window,
            text=f"Payment: {order.get('payment', 'Pending')}"
        ).pack()

        tk.Label(
            window,
            text=f"Status: {order.get('status', 'Pending')}"
        ).pack()

        tk.Label(
            window,
            text=f"Delivery: {order.get('delivery_status', 'Order Confirmed')}"
        ).pack(pady=10)


# -----------------------------
# UPDATE ORDER STATUS
# -----------------------------
def update_order_status():

    window = tk.Toplevel()

    window.title("Update Order Status")
    window.geometry("450x400")

    tk.Label(
        window,
        text="UPDATE ORDER STATUS",
        font=("Arial", 20, "bold")
    ).pack(pady=25)

    if not orders:

        tk.Label(
            window,
            text="No orders available."
        ).pack(pady=30)

        return

    tk.Label(
        window,
        text="Select Status"
    ).pack(pady=10)

    status = tk.StringVar()
    status.set("Preparing Food")

    tk.Radiobutton(
        window,
        text="Preparing Food",
        variable=status,
        value="Preparing Food"
    ).pack(pady=5)

    tk.Radiobutton(
        window,
        text="Out for Delivery",
        variable=status,
        value="Out for Delivery"
    ).pack(pady=5)

    tk.Radiobutton(
        window,
        text="Delivered",
        variable=status,
        value="Delivered"
    ).pack(pady=5)

    def update():

        orders[-1]["delivery_status"] = status.get()

        messagebox.showinfo(
            "Updated",
            f"Order status updated to:\n{status.get()}"
        )

        window.destroy()

    tk.Button(
        window,
        text="UPDATE",
        width=20,
        command=update
    ).pack(pady=20)


# -----------------------------
# ADMIN PAGE
# -----------------------------
def admin_page():

    admin_window = tk.Toplevel()

    admin_window.title("Admin Panel")
    admin_window.geometry("550x600")

    tk.Label(
        admin_window,
        text="ADMIN PANEL",
        font=("Arial", 24, "bold")
    ).pack(pady=30)

    tk.Button(
        admin_window,
        text="ADD FOOD",
        width=30,
        height=2,
        command=add_food
    ).pack(pady=8)

    tk.Button(
        admin_window,
        text="VIEW FOOD",
        width=30,
        height=2,
        command=view_food_admin
    ).pack(pady=8)

    tk.Button(
        admin_window,
        text="ADD RESTAURANT",
        width=30,
        height=2,
        command=add_restaurant
    ).pack(pady=8)

    tk.Button(
        admin_window,
        text="VIEW ORDERS",
        width=30,
        height=2,
        command=view_orders_admin
    ).pack(pady=8)

    tk.Button(
        admin_window,
        text="UPDATE ORDER STATUS",
        width=30,
        height=2,
        command=update_order_status
    ).pack(pady=8)

    tk.Button(
        admin_window,
        text="LOGOUT",
        width=30,
        height=2,
        command=admin_window.destroy
    ).pack(pady=20)