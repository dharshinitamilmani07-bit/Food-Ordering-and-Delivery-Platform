import tkinter as tk

root = tk.Tk()

root.title("Payment Test")
root.geometry("500x500")

label = tk.Label(
    root,
    text="PAYMENT PAGE",
    font=("Arial", 25, "bold")
)

label.pack(pady=50)

button = tk.Button(
    root,
    text="PAY NOW",
    width=20
)

button.pack(pady=30)

root.mainloop()