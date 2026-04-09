import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x250")

num1_var = tk.StringVar()
num2_var = tk.StringVar()

tk.Label(root, text="Число 1:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
tk.Entry(root, textvariable=num1_var).grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Число 2:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
tk.Entry(root, textvariable=num2_var).grid(row=1, column=1, padx=10, pady=5)

result_label = tk.Label(root, text="", fg="blue")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

def calculate(op):
    try:
        num1 = float(num1_var.get())
        num2 = float(num2_var.get())
        
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                messagebox.showerror("Помилка", "Ділення на нуль неможливе!")
                return
            result = num1 / num2
        else:
            result = "???"
        
        result_label.config(text=f"Результат: {result}")
    
    except ValueError:
        messagebox.showerror("Помилка", "Введіть числові значення!")

tk.Button(root, text="+", width=5, command=lambda: calculate("+")).grid(row=3, column=0, padx=5, pady=5)
tk.Button(root, text="-", width=5, command=lambda: calculate("-")).grid(row=3, column=1, padx=5, pady=5)
tk.Button(root, text="*", width=5, command=lambda: calculate("*")).grid(row=4, column=0, padx=5, pady=5)
tk.Button(root, text="/", width=5, command=lambda: calculate("/")).grid(row=4, column=1, padx=5, pady=5)

root.mainloop()