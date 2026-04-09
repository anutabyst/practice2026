import tkinter as tk

root = tk.Tk()
root.title("Програма з кнопками")
root.geometry("400x300")

label = tk.Label(root, text="", font=("Arial", 16))
label.pack(pady=20)

def greet():
    label.config(text="Вітаю, користувач!")

def clear():
    label.config(text="")

def exit_app():
    root.destroy()

btn_greet = tk.Button(root, text="Привітати", command=greet)
btn_greet.pack(pady=5)

btn_clear = tk.Button(root, text="Очистити", command=clear)
btn_clear.pack(pady=5)

btn_exit = tk.Button(root, text="Вийти", command=exit_app)
btn_exit.pack(pady=5)

root.mainloop()