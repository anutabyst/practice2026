import tkinter as tk

root = tk.Tk()
root.title("Перша програма")

root.geometry("1024x768")
root.resizable(False, False)  

label = tk.Label(root, text="Hello, world!", font=("Arial", 20))
label.pack(pady=50)

def close_app():
    root.destroy()

button = tk.Button(root, text="Закрити", command=close_app)
button.pack()

root.mainloop()