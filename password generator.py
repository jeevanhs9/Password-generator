import tkinter as tk
import random
import string

# -------- PASSWORD GENERATE --------
def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            result_label.config(text="Length must be ≥ 4", fg="red")
            return

        characters = ""

        if letters_var.get():
            characters += string.ascii_letters
        if numbers_var.get():
            characters += string.digits
        if symbols_var.get():
            characters += string.punctuation

        if characters == "":
            result_label.config(text="Select at least one option!", fg="red")
            return

        # strong password (at least one of each selected)
        password = []

        if letters_var.get():
            password.append(random.choice(string.ascii_letters))
        if numbers_var.get():
            password.append(random.choice(string.digits))
        if symbols_var.get():
            password.append(random.choice(string.punctuation))

        while len(password) < length:
            password.append(random.choice(characters))

        random.shuffle(password)
        final_password = "".join(password)

        password_entry.delete(0, tk.END)
        password_entry.insert(0, final_password)
        result_label.config(text="Password Generated!", fg="lightgreen")

    except:
        result_label.config(text="Invalid length!", fg="red")

# -------- COPY PASSWORD --------
def copy_password():
    pwd = password_entry.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        result_label.config(text="Copied to clipboard!", fg="cyan")

# -------- WINDOW --------
root = tk.Tk()
root.title("Advanced Password Generator - IBM Project")
root.geometry("400x420")
root.configure(bg="#111827")
root.resizable(False, False)

# Title
tk.Label(root, text="Random Password Generator",
         font=("Arial", 18, "bold"),
         fg="#00ffcc", bg="#111827").pack(pady=15)

# Length
tk.Label(root, text="Password Length",
         fg="white", bg="#111827").pack()

length_entry = tk.Entry(root, font=("Arial", 12), justify="center")
length_entry.pack(pady=5)
length_entry.insert(0, "12")

# Options
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters (A-Z, a-z)",
               variable=letters_var, bg="#111827", fg="white",
               selectcolor="#222").pack(anchor="w", padx=80)

tk.Checkbutton(root, text="Include Numbers (0-9)",
               variable=numbers_var, bg="#111827", fg="white",
               selectcolor="#222").pack(anchor="w", padx=80)

tk.Checkbutton(root, text="Include Symbols (!@#)",
               variable=symbols_var, bg="#111827", fg="white",
               selectcolor="#222").pack(anchor="w", padx=80)

# Generate button
tk.Button(root, text="Generate Password",
          font=("Arial", 13, "bold"),
          bg="#ff2d55", fg="white",
          command=generate_password).pack(pady=15)

# Password display
password_entry = tk.Entry(root, font=("Arial", 14), justify="center", width=25)
password_entry.pack(pady=10)

# Copy button
tk.Button(root, text="Copy Password",
          font=("Arial", 12, "bold"),
          bg="#00adb5", fg="white",
          command=copy_password).pack(pady=5)

# Result label
result_label = tk.Label(root, text="", fg="white", bg="#111827", font=("Arial", 11))
result_label.pack(pady=10)

root.mainloop()
