from tkinter import *

x = 10
y = 10
a = 100
b = 100

window = Tk()
window.geometry("400x200")

canvas1 = Canvas (window, bg = "Light blue", height = 200, width = 400)
canvas1.grid(row = 0, column = 0, sticky = W)

circle = canvas1.create_oval(50,50,150,150, outline="Blue", fill = "Blue")

coord = [x, y, a, b]
rect = canvas1.create_rectangle(coord, outline = "Red", fill = "Red")

window.mainloop()
