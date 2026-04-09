import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Простий Блокнот")
root.geometry("500x400")

text_area = tk.Text(root)
text_area.pack(fill="both", expand=True)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt")])
    if file_path:
        content = text_area.get(1.0, tk.END)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

def exit_app():
    if messagebox.askyesno("Вихід", "Ви хочете вийти без збереження?"):
        root.destroy()

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Відкрити", command=open_file)
file_menu.add_command(label="Зберегти", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Вийти", command=exit_app)
menu_bar.add_cascade(label="Файл", menu=file_menu)
root.config(menu=menu_bar)

root.mainloop()