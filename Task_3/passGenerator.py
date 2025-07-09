import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    length = length_var.get()
    if length <= 0:
        messagebox.showwarning("Invalid", "Password length must be greater than 0")
        return

    characters = ""
    if use_letters.get():
        characters += string.ascii_letters
    if use_numbers.get():
        characters += string.digits
    if use_symbols.get():
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("Warning", "Please select at least one character set")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

def copy_password():
    password = password_var.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard")
    else:
        messagebox.showwarning("Empty", "No password to copy")

# GUI setup
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x350")
root.config(bg="#eef2f3")

tk.Label(root, text="Password Generator", font=("Arial", 18, "bold"), bg="#eef2f3", fg="#333").pack(pady=10)

frame = tk.Frame(root, bg="#eef2f3")
frame.pack(pady=5)

tk.Label(frame, text="Password Length:", font=("Arial", 12), bg="#eef2f3").grid(row=0, column=0, sticky="w")
length_var = tk.IntVar(value=12)
tk.Spinbox(frame, from_=4, to=64, textvariable=length_var, width=5, font=("Arial", 12)).grid(row=0, column=1, padx=10)

# Options
use_letters = tk.BooleanVar(value=True)
use_numbers = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Include Letters (A-Z, a-z)", variable=use_letters, bg="#eef2f3", font=("Arial", 11)).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Include Numbers (0-9)", variable=use_numbers, bg="#eef2f3", font=("Arial", 11)).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Include Symbols (!@#$)", variable=use_symbols, bg="#eef2f3", font=("Arial", 11)).pack(anchor="w", padx=40)

# Output field
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, font=("Arial", 14), width=30, justify="center").pack(pady=15)

# Buttons
btn_frame = tk.Frame(root, bg="#eef2f3")
btn_frame.pack()

tk.Button(btn_frame, text="🔁 Generate", command=generate_password, bg="#4CAF50", fg="white", font=("Arial", 12), width=12).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="📋 Copy", command=copy_password, bg="#2196F3", fg="white", font=("Arial", 12), width=12).grid(row=0, column=1, padx=5)

root.mainloop()
