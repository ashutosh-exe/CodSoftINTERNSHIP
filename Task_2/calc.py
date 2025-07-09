import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    handle_input(text)

def handle_input(key):
    if key == "=" or key == "\r":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif key == "C":
        entry.delete(0, tk.END)
    elif key == "\x08":  # Backspace
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current[:-1])
    else:
        entry.insert(tk.END, key)

def on_key_press(event):
    if event.keysym == "Return":
        handle_input("=")
        return "break"
    elif event.keysym == "BackSpace":
        handle_input("\x08")
        return "break"
    elif event.char in "0123456789+-*/().%":
        handle_input(event.char)
        return "break"

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, font="Arial 20", borderwidth=5, relief=tk.RIDGE, justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

entry.bind("<Key>", on_key_press)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["C", "(", ")", "%"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

for row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack(expand=True, fill="both")
    for btn_text in row:
        button = tk.Button(
            row_frame,
            text=btn_text,
            font="Arial 18",
            height=2,
            width=5
        )
        button.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        button.bind("<Button-1>", on_click)

root.mainloop()
