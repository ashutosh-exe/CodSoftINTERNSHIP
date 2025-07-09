import tkinter as tk
from tkinter import messagebox

# List to store tasks: [("task", completed_bool), ...]
tasks = []

def update_listbox():
    listbox.delete(0, tk.END)
    for task, done in tasks:
        prefix = "✔ " if done else "✖ "
        listbox.insert(tk.END, prefix + task)

def add_task():
    task = entry.get().strip()
    if task:
        tasks.append((task, False))
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        update_listbox()
    else:
        messagebox.showwarning("Warning", "No task selected.")

def toggle_complete():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        task, done = tasks[index]
        tasks[index] = (task, not done)
        update_listbox()
    else:
        messagebox.showwarning("Warning", "No task selected.")

def clear_all():
    if messagebox.askyesno("Confirm", "Delete all tasks?"):
        tasks.clear()
        update_listbox()

# GUI setup
window = tk.Tk()
window.title("To-Do List App")
window.geometry("450x500")
window.config(bg="#f0f0f0")

title = tk.Label(window, text="📝 To-Do List", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333")
title.pack(pady=10)

frame = tk.Frame(window)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=40, height=10, font=("Arial", 14), selectbackground="#a3c9a8", activestyle='none')
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(window, font=("Arial", 14), width=30)
entry.pack(pady=10)

btn_frame = tk.Frame(window, bg="#f0f0f0")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="➕ Add Task", width=15, font=("Arial", 12), bg="#4CAF50", fg="white", command=add_task).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="❌ Delete Task", width=15, font=("Arial", 12), bg="#f44336", fg="white", command=delete_task).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="✅ Mark as Done", width=15, font=("Arial", 12), bg="#2196F3", fg="white", command=toggle_complete).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="🗑 Clear All", width=15, font=("Arial", 12), bg="#9C27B0", fg="white", command=clear_all).grid(row=1, column=1, padx=5, pady=5)

window.mainloop()
