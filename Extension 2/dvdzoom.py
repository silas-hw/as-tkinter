from tkinter import *
from PIL import ImageTk, Image

import random, math

root = Tk()
root.geometry("1280x720")
root.minsize(600, 600)
imgs = []

#load image files to list
for i in range(1, 5):
    img=ImageTk.PhotoImage(Image.open(f"dvd{i}.png"))
    imgs.append(img)

#set velocity for dvd logo to move at
baseVel = 10
baseResulant = math.sqrt(2 * baseVel**2)
x_vel = baseVel
y_vel = baseVel

#the current dvd image number
currentNum = 0

#resize the canvas to match the root window  size
def canvasResize():
    canvas.config(width=root.winfo_width(), height=root.winfo_height())
    root.after(1, canvasResize)

def randomImg(currentImgIndex):
    global currentNum
    num = random.randint(0, 2)   
    numList = [0, 1, 2, 3]
    numList.pop(currentImgIndex) #remove current image index from number list
    newImgIndex = numList[num] #set current image index to random number from number list
    img = imgs[newImgIndex] #set the canvas image to the new image based off the randomly generated image index number

    currentNum = newImgIndex

    return img

def move():
    global x_vel
    global y_vel

    coords = canvas.coords(dvdimg)
    x = coords[0]
    y = coords[1]

    old_x_vel = x_vel
    old_y_vel = y_vel

    width = canvas.winfo_width()
    height = canvas.winfo_height()

    if width<600 or height<600:
        root.after(33, move)
        return

    if y<height and y>112:
        y_vel = y_vel
    else: 
        randVel = random.randint(8, 12)
        y_vel = randVel if y<115 else -randVel


        newX = math.sqrt(baseResulant**2 - y_vel**2)
        x_vel = newX if x_vel>0 else -newX

    if x<width and x>230:
        x_vel = x_vel 
    else:
        randVel = random.randint(8, 12)
        x_vel = randVel if x<235 else -randVel

        newY = math.sqrt(baseResulant**2 - x_vel**2)
        y_vel = newY if y_vel>0 else -newY

    #if x or y velocity changes from positive to negative or vise versa
    if (old_x_vel<0 and x_vel>0) or (old_x_vel>0 and x_vel<0) or (old_y_vel<0 and y_vel>0) or (old_y_vel>0 and y_vel<0):
        newImg = randomImg(currentNum) #generate random image index
        canvas.itemconfig(dvdimg, image=newImg) #set new dvd image
        canvas.tag_raise(dvdimg) #raise the canvas image to top level (have it visible above everything else)

    canvas.move(dvdimg, x_vel, y_vel)

    root.after(33, move)

canvas = Canvas(root, width=1280, height=720, bg="black")
canvas.pack()

img = ImageTk.PhotoImage(Image.open("dvd1.png"))
dvdimg = canvas.create_image(400, 400, image=imgs[0], anchor=SE)

canvasResize()
move()

root.mainloop()