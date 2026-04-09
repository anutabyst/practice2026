import tkinter as tk
from tkinter import ttk, colorchooser
import json

root = tk.Tk()
root.title("Програма з вкладками")
root.geometry("400x300")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)
tab3 = tk.Frame(notebook)

notebook.add(tab1, text="Головна")
notebook.add(tab2, text="Налаштування")
notebook.add(tab3, text="Про програму")

name_var = tk.StringVar()

tk.Label(tab1, text="Введіть ім'я:").pack(pady=10)
tk.Entry(tab1, textvariable=name_var).pack(pady=5)

result_label = tk.Label(tab1, text="")
result_label.pack(pady=10)

def save_name():
    name = name_var.get()
    result_label.config(text=f"Привіт, {name}!")

tk.Button(tab1, text="Зберегти", command=save_name).pack()

# =========================
# 🔹 Вкладка 2 (Налаштування)
# =========================
COLOR_FILE = "settings.json"

def load_color():
    try:
        with open(COLOR_FILE, "r") as f:
            data = json.load(f)
            return data.get("bg_color", "white")
    except:
        return "white"

def save_color(color):
    with open(COLOR_FILE, "w") as f:
        json.dump({"bg_color": color}, f)

def choose_color():
    color = colorchooser.askcolor()[1]
    if color:
        root.configure(bg=color)
        tab1.configure(bg=color)
        tab2.configure(bg=color)
        tab3.configure(bg=color)
        save_color(color)

tk.Button(tab2, text="Обрати колір", command=choose_color).pack(pady=20)

tk.Label(tab3, text="Автор: Анна\nВерсія: 1.0", font=("Arial", 12)).pack(pady=50)

bg_color = load_color()
root.configure(bg=bg_color)
tab1.configure(bg=bg_color)
tab2.configure(bg=bg_color)
tab3.configure(bg=bg_color)

root.mainloop()