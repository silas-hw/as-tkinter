from tkinter import ttk
from PIL import ImageTk, Image

import random, math
import tkinter as tk

class MainApp(tk.Frame):

    def __init__(self, imgList, initialVel, master=None):
        self.currentImgIndex = 0
        self.dvdImgList = imgList

        #set velocity for dvd logo to move at
        self.initialVel = initialVel
        self.initialResulant = math.sqrt(2 * self.initialVel**2) #to ensure the object moves at the same speed, whilst having random angles
        self.x_vel = self.initialVel
        self.y_vel = self.initialVel

        super().__init__(master)
        self.master = master
        self.pack()

        self.layout()
        
        self.expandToWinSize()
        self.moveImg()

    @property
    def x_coord(self):
        coords = self.canvas.coords(self.dvdimg)
        out = coords[0]
        return out

    @property
    def y_coord(self):
        coords = self.canvas.coords(self.dvdimg)
        out = coords[1]
        return out

    @property
    def WinSize(self):
        return [self.master.winfo_width(), self.master.winfo_height()]

    @property
    def ImgIndexRange(self):
        out = []
        indexRange = len(self.dvdImgList)
        for i in range(0, indexRange):
            out.append(i)
        
        return out

    @property
    def DvdImgFileIndex(self):
        randImgIndexRange = self.ImgIndexRange #get current img index range and set it to local variable
        print(randImgIndexRange)
        print(self.currentImgIndex)
        randImgIndexRange.pop(self.currentImgIndex) #remove current image index from index range (prevents same image from being chosen again)
        print(randImgIndexRange)
        print(len(self.dvdImgList))

        randImgIndexNum = random.randint(0 , len(self.dvdImgList)-2) #generate a random number to choose a new random index with
        self.currentImgIndex = randImgIndexRange[randImgIndexNum] #get random image index from list that doesn't include current image index

        return self.currentImgIndex

    def layout(self):
        self.canvas = tk.Canvas(self.master, width=1280, height=720, bg='black')
        self.canvas.pack()

        self.dvdimg = self.canvas.create_image(400, 400, image=self.dvdImgList[0], anchor=tk.SE)

    def changeColour(self):
        imgIndex = self.DvdImgFileIndex
        outImg = self.dvdImgList[imgIndex]

        self.canvas.itemconfig(self.dvdimg, image=outImg)

    def moveImg(self):
        changeColour = False

        #bounce
        if self.x_coord>=self.WinSize[0] or self.x_coord<=230:
            randVel = random.randint(8, 12)
            self.x_vel = randVel if self.x_coord<235 else -randVel

            newY = math.sqrt(self.initialResulant**2 - self.x_vel**2)
            self.y_vel = newY if self.y_vel>0 else -newY

            changeColour = True

        if self.y_coord>=self.WinSize[1] or self.y_coord<=112:
            randVel = random.randint(8, 12)
            self.y_vel = randVel if self.y_coord<115 else -randVel

            newX = math.sqrt(self.initialResulant**2 - self.y_vel**2)
            self.x_vel = newX if self.x_vel>0 else -newX

            changeColour=True

        if changeColour:
            self.changeColour()
        
        self.canvas.move(self.dvdimg, self.x_vel, self.y_vel)
        self.master.after(33, self.moveImg)


    def expandToWinSize(self):
        width = self.WinSize[0]
        height = self.WinSize[1]

        self.canvas.config(width=width, height=height)

        self.master.after(1, self.expandToWinSize)



if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("1280x720")
    root.minsize(600, 600)

    imgs = []

    #load image files to list, you need to open images here as to not have them garbage collected
    for i in range(1, 5):
        img=ImageTk.PhotoImage(Image.open(f"dvd{i}.png"))
        imgs.append(img)

    app = MainApp(imgs, 10, master=root)
    app.mainloop()