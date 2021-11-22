from tkinter import *

root = Tk()

x_vel = 10
y_vel = 10

def move():
    global x_vel
    global y_vel

    coords = canvas1.coords(circle1)
    x = coords[0]
    y = coords[1]

    print(x)

    y_vel = y_vel if y<105 and y!=0 else -y_vel
    x_vel = x_vel if x<300 and x>0 else -x_vel

    canvas1.move(circle1, x_vel, y_vel)
    root.after(33, move)

canvas1 = Canvas(root, height=200, width=400, bg="#50a0d9")
canvas1.pack()

#50, 50, 150, 150 follows x0, y0, x1, y1 where the difference between x0 and x1 is the width and the height for y0, y1
circle1 = canvas1.create_oval(50,50,150,150, outline="red", fill="pink")

coord = [120, 150, 250, 190]
rect1 = canvas1.create_rectangle(coord, outline="pink", fill="red")

move()

root.mainloop()