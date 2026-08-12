import tkinter as tk
from tkinter import messagebox


def delivery_page(home_window, order):

    delivery_window = tk.Toplevel(home_window)

    delivery_window.title("Delivery Tracking")
    delivery_window.geometry("500x500")

    tk.Label(
        delivery_window,
        text="DELIVERY TRACKING",
        font=("Arial", 22, "bold")
    ).pack(pady=30)

    tk.Label(
        delivery_window,
        text="Order Status",
        font=("Arial", 16, "bold")
    ).pack(pady=15)

    status = tk.StringVar()
    status.set(
        order.get("delivery_status", "Order Confirmed")
    )

    tk.Label(
        delivery_window,
        textvariable=status,
        font=("Arial", 18)
    ).pack(pady=20)

    def preparing():

        status.set("Preparing Food")
        order["delivery_status"] = "Preparing Food"

    def out_for_delivery():

        status.set("Out for Delivery")
        order["delivery_status"] = "Out for Delivery"

    def delivered():

        status.set("Delivered")
        order["delivery_status"] = "Delivered"

        messagebox.showinfo(
            "Delivery",
            "Order Delivered Successfully!"
        )

    tk.Button(
        delivery_window,
        text="PREPARING FOOD",
        width=25,
        command=preparing
    ).pack(pady=8)

    tk.Button(
        delivery_window,
        text="OUT FOR DELIVERY",
        width=25,
        command=out_for_delivery
    ).pack(pady=8)

    tk.Button(
        delivery_window,
        text="DELIVERED",
        width=25,
        command=delivered
    ).pack(pady=8)

    tk.Button(
        delivery_window,
        text="CLOSE",
        width=25,
        command=delivery_window.destroy
    ).pack(pady=20)