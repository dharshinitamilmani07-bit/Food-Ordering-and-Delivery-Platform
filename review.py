import tkinter as tk
from tkinter import messagebox


reviews = []


def review_page(home_window, order):

    review_window = tk.Toplevel(home_window)

    review_window.title("Review & Rating")
    review_window.geometry("500x550")

    tk.Label(
        review_window,
        text="REVIEW & RATING",
        font=("Arial", 22, "bold")
    ).pack(pady=30)

    tk.Label(
        review_window,
        text="How was your food?",
        font=("Arial", 15)
    ).pack(pady=15)

    rating = tk.IntVar(value=0)

    for i in range(1, 6):

        tk.Radiobutton(
            review_window,
            text=f"{i} Star",
            variable=rating,
            value=i
        ).pack(pady=5)

    tk.Label(
        review_window,
        text="Write your review"
    ).pack(pady=15)

    review_text = tk.Text(
        review_window,
        width=40,
        height=6
    )

    review_text.pack()

    def submit_review():

        if rating.get() == 0:

            messagebox.showwarning(
                "Review",
                "Please select a rating!"
            )

            return

        review = review_text.get("1.0", tk.END).strip()

        if review == "":

            messagebox.showwarning(
                "Review",
                "Please write a review!"
            )

            return

        reviews.append({
            "rating": rating.get(),
            "review": review
        })

        messagebox.showinfo(
            "Success",
            "Thank you for your review!"
        )

        review_window.destroy()

    tk.Button(
        review_window,
        text="SUBMIT REVIEW",
        width=25,
        command=submit_review
    ).pack(pady=25)