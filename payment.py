import tkinter as tk
from tkinter import messagebox


def payment_page(home_window, order, cart_window=None):

    payment_window = tk.Toplevel(home_window)

    payment_window.title("Payment")
    payment_window.geometry("500x500")

    tk.Label(
        payment_window,
        text="PAYMENT PAGE",
        font=("Arial", 24, "bold")
    ).pack(pady=30)

    tk.Label(
        payment_window,
        text=f"Total Amount: Rs. {order['total']}",
        font=("Arial", 16, "bold")
    ).pack(pady=15)

    tk.Label(
        payment_window,
        text="Select Payment Method",
        font=("Arial", 14)
    ).pack(pady=15)

    payment_method = tk.StringVar()

    tk.Radiobutton(
        payment_window,
        text="UPI",
        variable=payment_method,
        value="UPI"
    ).pack(pady=8)

    tk.Radiobutton(
        payment_window,
        text="Credit / Debit Card",
        variable=payment_method,
        value="Card"
    ).pack(pady=8)

    tk.Radiobutton(
        payment_window,
        text="Cash on Delivery",
        variable=payment_method,
        value="COD"
    ).pack(pady=8)

    def make_payment():

        method = payment_method.get()

        if method == "":
            messagebox.showwarning(
                "Payment",
                "Please select a payment method!"
            )
            return

        # Update the same order
        order["payment"] = method
        order["status"] = "Payment Successful"

        messagebox.showinfo(
            "Payment Successful",
            f"Payment Successful!\n\n"
            f"Amount: Rs. {order['total']}\n"
            f"Method: {method}"
        )

        payment_window.destroy()

        if cart_window:
            cart_window.destroy()

    tk.Button(
        payment_window,
        text="PAY NOW",
        width=25,
        command=make_payment
    ).pack(pady=30)