import tkinter as tk
from tkinter import colorchooser, filedialog

class GraphicsApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Графіка")

        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="white")
        self.canvas.pack()

        self.color = "black"
        self.tool = "line" 

        toolbar = tk.Frame(self.root)
        toolbar.pack(pady=5)

        tk.Button(toolbar, text="Лінія", command=lambda: self.select_tool("line")).pack(side="left", padx=5)
        tk.Button(toolbar, text="Коло", command=lambda: self.select_tool("circle")).pack(side="left", padx=5)
        tk.Button(toolbar, text="Колір", command=self.choose_color).pack(side="left", padx=5)
        tk.Button(toolbar, text="Очистити", command=self.clear_canvas).pack(side="left", padx=5)
        tk.Button(toolbar, text="Зберегти", command=self.save_canvas).pack(side="left", padx=5)

        self.start_x = None
        self.start_y = None
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        self.temp_shape = None  

    
    def select_tool(self, tool):
        self.tool = tool

    def choose_color(self):
        color = colorchooser.askcolor(title="Виберіть колір")
        if color[1]:
            self.color = color[1]

    def clear_canvas(self):
        self.canvas.delete("all")

    def on_click(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_drag(self, event):
        if self.temp_shape:
            self.canvas.delete(self.temp_shape)
        if self.tool == "line":
            self.temp_shape = self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill=self.color)
        elif self.tool == "circle":
            x0, y0 = self.start_x, self.start_y
            x1, y1 = event.x, event.y
            self.temp_shape = self.canvas.create_oval(x0, y0, x1, y1, outline=self.color)

    def on_release(self, event):
        if self.temp_shape:
            self.canvas.delete(self.temp_shape)
        if self.tool == "line":
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill=self.color)
        elif self.tool == "circle":
            self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y, outline=self.color)
        self.temp_shape = None

    def save_canvas(self):
        filename = filedialog.asksaveasfilename(defaultextension=".ps",
                                                filetypes=[("PostScript files", "*.ps")])
        if filename:
            self.canvas.postscript(file=filename)
            tk.messagebox.showinfo("Готово", f"Збережено у {filename}")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = GraphicsApp()
    app.run()