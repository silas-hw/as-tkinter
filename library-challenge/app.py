import json
import tkinter as tk
from tkinter import ttk #has better looking widgets

class Window(tk.Frame):
    '''
        A superclass to create windows from. Includes a change window function to change the content of the root window 
    '''
    TITLE_FONT = ("Arial", 30, "bold")

    def change_window(self, window):
        for widget in self.root.winfo_children():
            widget.destroy()

        window(self.root)

class BookSearch(Window):

    def __init__(self, root):
        self.root = root

        super().__init__()

        self.title = tk.Label(self.root, text="Search for a Book", font=self.TITLE_FONT)
        self.title.grid(row=0, column=0, columnspan=2)

        self.back_butt = ttk.Button(self.root, text="go back", command=lambda: self.change_window(MainApp))
        self.back_butt.grid(row=1, column=0, sticky=tk.NW)

class BookAdd(Window):

    def __init__(self, root):
        self.root = root

        super().__init__()

        self.title = tk.Label(self.root, text="Add a Book", font=self.TITLE_FONT)
        self.title.grid(row=0, column=0, columnspan=2)

        self.back_butt = ttk.Button(self.root, text="go back")

class MainApp(Window):
    '''
        The main body of the app, being what everything else is built on top of
    '''

    def __init__(self, root):
        self.root = root

        self.title = tk.Label(self.root ,text="Library System", font=self.TITLE_FONT)
        self.title.grid(row=0, column=0, columnspan=2)

        self.search_butt = ttk.Button(self.root, text="Search For Book", command=lambda:self.change_window(BookSearch))
        self.search_butt.grid(row=1, column=0, sticky=tk.NW)

        self.add_butt = ttk.Button(self.root, text="Add Book")
        self.add_butt.grid(row=1, column=1, sticky=tk.NW)
        
    def mainloop(self):
        self.root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("500x500")
    root.resizable(False, False)

    app = MainApp(root)
    app.mainloop()     