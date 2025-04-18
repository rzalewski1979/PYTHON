
import tkinter as tk

def draw_chart(data):
    max_value = max(data)
    width = 400
    height = 300
    bar_width = width / len(data)

    root = tk.Tk()
    canvas = tk.Canvas(root, width=width, height=height, bg='white')
    canvas.pack()

    for i, value in enumerate(data):
        # Rysowanie prostokątów (słupków wykresu)
        x1 = i * bar_width
        y1 = height - (value / max_value * height)
        x2 = (i + 1) * bar_width
        y2 = height
        canvas.create_rectangle(x1, y1, x2, y2, fill='blue')

    root.mainloop()

# Przykładowe dane
data = [10, 20, 30, 25, 15]
draw_chart(data)
