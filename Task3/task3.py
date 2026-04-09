import tkinter as tk

root = tk.Tk()
root.title("Анкета користувача")
root.geometry("400x300")

name_var = tk.StringVar()
gender_var = tk.StringVar()
agree_var = tk.BooleanVar()

tk.Label(root, text="Ім'я:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
tk.Entry(root, textvariable=name_var).grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Стать:").grid(row=1, column=0, sticky="w", padx=10, pady=5)

tk.Radiobutton(root, text="Чоловіча", variable=gender_var, value="Чоловіча")\
    .grid(row=1, column=1, sticky="w")

tk.Radiobutton(root, text="Жіноча", variable=gender_var, value="Жіноча")\
    .grid(row=2, column=1, sticky="w")

tk.Checkbutton(root, text="Погоджуюсь із умовами", variable=agree_var)\
    .grid(row=3, column=0, columnspan=2, pady=5)

result_label = tk.Label(root, text="", fg="blue")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

def save():
    name = name_var.get()
    gender = gender_var.get()
    agree = agree_var.get()

    text = f"Ім'я: {name}\nСтать: {gender}\nПогодження: {agree}"
    result_label.config(text=text)
 
tk.Button(root, text="Зберегти", command=save)\
    .grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()