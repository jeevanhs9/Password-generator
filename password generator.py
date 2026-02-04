import tkinter as tk
import random
import string
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())

        chars = ""
        if upper_var.get():
            chars += string.ascii_uppercase
        if lower_var.get():
            chars += string.ascii_lowercase
        if number_var.get():
            chars += string.digits
        if symbol_var.get():
            chars += string.punctuation

        if not chars:
            messagebox.showwarning("Warning", "Select at least one option")
            return

        password = "".join(random.choice(chars) for _ in range(length))
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)

    except:
        messagebox.showerror("Error", "Enter a valid number")

# Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("380x460")
root.configure(bg="#0f172a")
root.resizable(False, False)

# Title
tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 20, "bold"),
    fg="#38bdf8",
    bg="#0f172a"
).pack(pady=15)

# Card frame
card = tk.Frame(root, bg="#1e293b")
card.pack(padx=20, pady=10, fill="both", expand=True)

# Length
tk.Label(card, text="Password Length", fg="white", bg="#1e293b").pack(pady=(15, 5))
length_entry = tk.Entry(card, justify="center", font=("Arial", 12))
length_entry.pack()
length_entry.insert(0, "12")

# Options
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=False)

options = [
    ("Uppercase (A-Z)", upper_var),
    ("Lowercase (a-z)", lower_var),
    ("Numbers (0-9)", number_var),
    ("Symbols (!@#$)", symbol_var)
]

for text, var in options:
    tk.Checkbutton(
        card,
        text=text,
        variable=var,
        fg="white",
        bg="#1e293b",
        activebackground="#1e293b",
        activeforeground="white",
        selectcolor="#0f172a"
    ).pack(anchor="w", padx=30)

# Generate button
tk.Button(
    card,
    text="Generate Password",
    font=("Arial", 13, "bold"),
    bg="#ef4444",
    fg="white",
    activebackground="#dc2626",
    command=generate_password
).pack(pady=15, ipadx=10, ipady=5)

# Result
tk.Label(card, text="Generated Password", fg="white", bg="#1e293b").pack(pady=5)
result_entry = tk.Entry(card, font=("Arial", 12), justify="center")
result_entry.pack(padx=20, fill="x", pady=(0, 15))

root.mainloop()
