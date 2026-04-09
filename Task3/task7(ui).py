import tkinter as tk


class MainWindow:
    def __init__(self, logic):
        self.logic = logic  # передаємо логіку ззовні

        self.root = tk.Tk()
        self.root.title("Calculator")

        # Поля вводу
        self.entry1 = tk.Entry(self.root)
        self.entry1.pack()

        self.entry2 = tk.Entry(self.root)
        self.entry2.pack()

        # Кнопки
        tk.Button(self.root, text="Add", command=self.add).pack()
        tk.Button(self.root, text="Subtract", command=self.subtract).pack()
        tk.Button(self.root, text="Multiply", command=self.multiply).pack()
        tk.Button(self.root, text="Divide", command=self.divide).pack()

        # Вивід результату
        self.result = tk.Label(self.root, text="Result: ")
        self.result.pack()

    def get_values(self):
        try:
            a = float(self.entry1.get())
            b = float(self.entry2.get())
            return a, b
        except ValueError:
            self.result.config(text="Error: enter numbers")
            return None, None

    def add(self):
        a, b = self.get_values()
        if a is not None:
            res = self.logic.add(a, b)
            self.result.config(text=f"Result: {res}")

    def subtract(self):
        a, b = self.get_values()
        if a is not None:
            res = self.logic.subtract(a, b)
            self.result.config(text=f"Result: {res}")

    def multiply(self):
        a, b = self.get_values()
        if a is not None:
            res = self.logic.multiply(a, b)
            self.result.config(text=f"Result: {res}")

    def divide(self):
        a, b = self.get_values()
        if a is not None:
            res = self.logic.divide(a, b)
            self.result.config(text=f"Result: {res}")

    def run(self):
        self.root.mainloop()