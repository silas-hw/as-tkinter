'''
basic tkinter menu bar program
'''
from tkinter import *

def func1():
    textarea.delete(0.0, END)
    textarea.insert(END, "Lmao imagine selecting option 1, how pathetic")

def func2():
    textarea.delete(0.0, END)
    textarea.insert(END, "Wow how amazing, you selected option 2")

def buttClick(text):
    menubar.entryconfigure(2, label=text) #config the second menu in menubar

root = Tk()

menubar = Menu(root)

firstmenu = Menu(menubar, tearoff=0)
firstmenu.add_command(label="Option 1", command=func1)
firstmenu.add_command(label="Quit", command=root.destroy)

secondmenu = Menu(menubar, tearoff=0)
secondmenu.add_command(label="Option 2", command=func2)
secondmenu.add_command(label="Quit, pt.2", command=root.destroy)

menubar.add_cascade(label="Menu1", menu=firstmenu)
menubar.add_cascade(label="menu2", menu=secondmenu)

root.config(menu=menubar)

#textbox
textarea = Text(root, width=35, height=10, wrap=WORD, bg="lightblue")
textarea.pack()

#buttons
butt1 = Button(root, text="Click me ;)", command=lambda: buttClick("thank u <3"))
butt2 = Button(root, text="pls leave me alone :/", command=lambda: buttClick(">:( i said leave me alone"))

butt1.pack()
butt2.pack()
root.mainloop()