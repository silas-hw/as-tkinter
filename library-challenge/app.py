'''
    This tkinter project makes use of a lot of classes and core oop concepts that we haven't yet been taught in class yet. If you're having trouble peer
    marking it because of this you can just ask me to explain some of it to you :)
'''

import json, os, inspect
import tkinter as tk
from tkinter import ttk #has better looking widgets
from tkinter import messagebox

class Window(tk.Frame):
    '''
        A superclass to create windows from. Includes a change window function to change the content of the root window 
    '''

    #constants that are used in every window
    FILE_PATH = os.path.dirname(os.path.realpath(__file__)) # gets the directory of the python file, so file operations can be done regardless of the current working directory

    TITLE_FONT = ("Arial", 30, "bold")

    PADX = 10
    PADY = 10
    PADY_ENTRY = 3

    themes = {
        "dark":{
            "bg":"#303030",
            "fg":"#ffffff",
            "butt-bg":"#6b6b6b",
            "butt-fg":"#ffffff"
        },
        "light":{
            "bg":"#ffffff",
            "fg":"#262626",
            "butt-bg":"#d9d9d9",
            "butt-fg":"#262626"

        }
    }

    current_theme = "light"

    def __init__(self, root):

        #set up styles for light and dark theme ttk widgets
        style = ttk.Style()

        style.theme_use('default')
        style.configure("TButton", relief='flat', bd=0)

        #####################################################################################################################################
        ## theres a lot of awkward things I have to do here in order to get the ttk widgets looking decent with the light and dark themes ###
        ## if you're at all interested at what the heck any of this means its likely best to rummage through what docs for ttk there are  ###
        #####################################################################################################################################

        style.configure("light.TButton", foreground=self.themes['light']['butt-fg'], background=self.themes['light']['butt-bg'], focuscolor=self.themes['light']['butt-bg'])
        style.map("light.TButton", background=[('active', self.themes['light']['butt-bg'])], foreground=[('active', self.themes['light']['butt-fg'])])
    
        style.configure("dark.TButton", foreground=self.themes['dark']['butt-fg'], background=self.themes['dark']['butt-bg'], focuscolor=self.themes['dark']['butt-bg'])
        style.map("dark.TButton", background=[('active', self.themes['dark']['butt-bg'])], foreground=[('active', self.themes['dark']['butt-fg'])])

    def change_window(self, window, theme='light'):
        for widget in self.root.winfo_children():
            widget.destroy()

        window(self.root, theme)

    @property
    def books(self):
        with open(f"{self.FILE_PATH}\\books.json", "r") as f:
            out = json.load(f)

        return out

    def save_to_file(self, books:dict) -> None:
        if not isinstance(books, dict):
            raise TypeError("Books argument should be a dictionary") #raises an exception if books arg doesnt have the type of a dict

        with open(f"{self.FILE_PATH}\\books.json", "w") as f:
            json.dump(books, f, indent=4)

    def tk_config(self, theme, widget, name):
        if name == 'Label':
            widget.config(bg=self.themes[theme]['bg'], fg=self.themes[theme]['fg'])
        elif name == 'Checkbutton': #checkbuttons will always be with ttk
            widget.config(background=self.themes[theme]['bg'], activebackground=self.themes[theme]['bg'], fg=self.themes[theme]['fg'], activeforeground=self.themes[theme]['fg'], selectcolor='#91d5f2')
        elif name == "Button":
            widget.config(style=f"{theme}.TButton")
        elif name == 'Frame':
            widget.config(bg=self.themes[theme]['bg'])

            for child in widget.winfo_children():
                child_name = child.__class__.__name__

                #this uses recursion, allowing for frames to be configured regardless of how many frames its already a child of
                self.tk_config(theme, child, child_name)
        

    def change_theme(self, theme:str):
        for widget in self.root.winfo_children():
            parent_module = inspect.getmodule(widget).__name__

            obj_name = widget.__class__.__name__

            self.root.config(bg=self.themes[theme]['bg'])

            if parent_module == 'tkinter':
                self.tk_config(theme, widget, obj_name)
            elif parent_module == 'tkinter.ttk':
                self.tk_config(theme, widget, obj_name)
                

class BookSearch(Window):

    def __init__(self, root, theme='light'):
        self.root = root
        self.current_theme = theme

        self.title = tk.Label(self.root, text="Search Books", font=self.TITLE_FONT)
        self.title.grid(row=0, column=0, columnspan=2)

        self.back_butt = ttk.Button(self.root, text="go back", command=lambda: self.change_window(MainApp, self.current_theme))
        self.back_butt.grid(row=1, column=0, sticky=tk.NW, padx=self.PADX)

        #==============#
        ## entry form ##
        #==============#

        self.form = tk.Frame(self.root)

        self.label_name = tk.Label(self.form, text="Book Name")
        self.label_name.grid(row=0, column=0, sticky=tk.NW, pady=self.PADY_ENTRY)
        
        self.entry_name = ttk.Entry(self.form)
        self.entry_name.grid(row=0, column=1, sticky=tk.NW, pady=self.PADY_ENTRY)

        self.label_author = tk.Label(self.form, text="Book Author")
        self.label_author.grid(row=1, column=0, sticky=tk.NW, pady=self.PADY_ENTRY)

        self.entry_author = ttk.Entry(self.form)
        self.entry_author.grid(row=1, column=1, sticky=tk.NW, pady=self.PADY_ENTRY)

        self.label_desc = tk.Label(self.form, text="Book Brief")
        self.label_desc.grid(row=2, column=0, sticky=tk.NW, pady=self.PADY_ENTRY)

        self.entry_desc = ttk.Entry(self.form)
        self.entry_desc.grid(row=2, column=1, sticky=tk.NW, pady=self.PADY_ENTRY)

        self.label_pages = tk.Label(self.form, text="Page Count")
        self.label_pages.grid(row=3, column=0, sticky=tk.NW, pady=self.PADY_ENTRY)

        self.entry_pages = ttk.Spinbox(self.form, from_=0, to=1000, wrap=True)
        self.entry_pages.grid(row=3, column=1, sticky=tk.NW, pady=self.PADY_ENTRY)

        self.hardback_val = tk.IntVar()
        self.entry_hardback = tk.Checkbutton(self.form, text="hardback", variable=self.hardback_val)
        self.entry_hardback.grid(row=4, column=0, pady=self.PADY_ENTRY)

        self.paperback_val = tk.IntVar()
        self.entry_paperback = tk.Checkbutton(self.form, text="paperback", variable=self.paperback_val)
        self.entry_paperback.grid(row=4, column=1, pady=self.PADY_ENTRY)

        self.label_amount = tk.Label(self.form, text="Amount of Books")
        self.label_amount.grid(row=5, column=0, sticky=tk.NW, pady=self.PADY_ENTRY)

        self.entry_amount = ttk.Spinbox(self.form, from_=1, to=100, wrap=True)
        self.entry_amount.grid(row=5, column=1, sticky=tk.NW, pady=self.PADY_ENTRY)

        self.form.grid(row=2, column=0, columnspan=2, pady=self.PADY, padx=self.PADX)

        #==============#

        self.search_butt = ttk.Button(self.root, text="Search", command=self.search)
        self.search_butt.grid(row=3, column=0, pady=self.PADY, padx=self.PADX)

        super().__init__(self.root)

        self.change_theme(self.current_theme)

    def search(self):
        name = self.entry_name.get()
        author = self.entry_author.get()
        desc = self.entry_desc.get()
        page_count = self.entry_pages.get()
        hardback = self.entry_hardback.get()
        paperback = self.entry_paperback.get()
        amount = self.entry_amount.get()

        try:
            assert int(page_count)>=0, "Page count must be a positive integer"
            assert not (hardback and paperback), "Book can only either be paperback or hardback, not both"
            assert int(amount)>=0, "Book amount must be a positive integer"
        except Exception as e:
            messagebox.showerror("Error", e)

class BookAdd(Window):

    def __init__(self, root, theme='light'):
        self.root = root
        self.current_theme = theme

        self.title = tk.Label(self.root, text="Add a Book", font=self.TITLE_FONT)
        self.title.grid(row=0, column=0, columnspan=2)

        self.back_butt = ttk.Button(self.root, text="go back", command=lambda:self.change_window(MainApp, self.current_theme))
        self.back_butt.grid(row=1, column=0, sticky=tk.NW, padx=self.PADX)

        #==============#
        ## entry form ##
        #==============#

        self.form = tk.Frame(self.root)

        self.label_name = tk.Label(self.form, text="Book Name")
        self.label_name.grid(row=0, column=0, sticky=tk.NW, pady=self.PADY_ENTRY)
        
        self.entry_name = ttk.Entry(self.form)
        self.entry_name.grid(row=0, column=1, sticky=tk.NW, pady=self.PADY_ENTRY)

        self.label_author = tk.Label(self.form, text="Book Author")
        self.label_author.grid(row=1, column=0, sticky=tk.NW, pady=self.PADY_ENTRY)

        self.entry_author = ttk.Entry(self.form)
        self.entry_author.grid(row=1, column=1, sticky=tk.NW, pady=self.PADY_ENTRY)

        self.label_desc = tk.Label(self.form, text="Book Brief")
        self.label_desc.grid(row=2, column=0, sticky=tk.NW, pady=self.PADY_ENTRY)

        self.entry_desc = ttk.Entry(self.form)
        self.entry_desc.grid(row=2, column=1, sticky=tk.NW, pady=self.PADY_ENTRY)

        self.label_pages = tk.Label(self.form, text="Page Count")
        self.label_pages.grid(row=3, column=0, sticky=tk.NW, pady=self.PADY_ENTRY)

        self.entry_pages = ttk.Spinbox(self.form, from_=0, to=1000, wrap=True)
        self.entry_pages.grid(row=3, column=1, sticky=tk.NW, pady=self.PADY_ENTRY)

        self.hardback_val = tk.IntVar()
        self.entry_hardback = tk.Checkbutton(self.form, text="hardback", variable=self.hardback_val)
        self.entry_hardback.grid(row=4, column=0, pady=self.PADY_ENTRY)

        self.paperback_val = tk.IntVar()
        self.entry_paperback = tk.Checkbutton(self.form, text="paperback", variable=self.paperback_val)
        self.entry_paperback.grid(row=4, column=1, pady=self.PADY_ENTRY)

        self.label_amount = tk.Label(self.form, text="Amount of Books")
        self.label_amount.grid(row=5, column=0, sticky=tk.NW, pady=self.PADY_ENTRY)

        self.entry_amount = ttk.Spinbox(self.form, from_=1, to=100, wrap=True)
        self.entry_amount.grid(row=5, column=1, sticky=tk.NW, pady=self.PADY_ENTRY)

        self.form.grid(row=2, column=0, columnspan=2, pady=self.PADY, padx=self.PADX)

        #==============#

        self.save_butt = ttk.Button(self.root, text="Save Book", command=self.save_book)
        self.save_butt.grid(row=3, column=0, sticky=tk.NW, pady=self.PADY, padx=self.PADX)

        super().__init__(self.root)

        self.change_theme(self.current_theme)

    def save_book(self):
    
        try:
            # validation checks
            assert self.entry_name.get() not in self.books.keys(), "book already exists in library"
            assert int(self.entry_pages.get()), "page count music be a positive integer"
            assert int(self.entry_amount.get()), "amount of books must be a positive interger"
            assert not(self.paperback_val.get() and self.hardback_val.get()), "books can only either be paperback or hardback, not both"
        except Exception as e:
            messagebox.showerror(title="Error", message=str(e))
            return #dont do anything else

        temp_books = self.books # wouldnt work with reference lol, lucky python doesnt do that

        book = {}
        book["name"] = self.entry_name.get()
        book["author"] = self.entry_author.get()
        book["brief"] = self.entry_desc.get()
        book["pages"] = int(self.entry_pages.get())
        book["hardback"] = bool(self.hardback_val.get())
        book["paperback"] = bool(self.paperback_val.get())
        book["in-stock"] = int(self.entry_amount.get())
        book["total"] = int(self.entry_amount.get())

        temp_books[self.entry_name.get()] = book
        
        self.save_to_file(temp_books)

class BookManage(Window):

    def __init__(self, root, theme='light'):
        self.root = root
        self.current_theme = theme

        self.title = tk.Label(self.root, text="Manage Library", font=self.TITLE_FONT)
        self.title.grid(row=0, column=0, columnspan=2)

        self.back_butt = ttk.Button(self.root, text="go back", command=lambda: self.change_window(MainApp, self.current_theme))
        self.back_butt.grid(row=1, column=0, padx=self.PADX, sticky=tk.NW)

        self.combo_var = tk.StringVar()
        self.combo_var.trace('w', self.on_combo_change) # call function when value of combobox changes

        self.combo_name = ttk.Combobox(self.root, values=[key for key in self.books.keys()], textvariable=self.combo_var)
        self.combo_name.grid(row=2, column=1, pady=self.PADY_ENTRY)  

        self.book_info = tk.Frame(self.root)
        self.book_taken_out = tk.Label(self.book_info, text="Num. Taken Out: ")
        self.book_taken_out.grid(row=0, column=0, sticky=tk.NW)

        self.book_in_stock = tk.Label(self.book_info, text="Num. In Stock: ")
        self.book_in_stock.grid(row=1, column=0, sticky=tk.NW)
        
        self.book_info.grid(row=3, column=1)

        self.takeout_butt = ttk.Button(self.root, text="Takeout Book", command=self.take_out_book)
        self.takeout_butt.grid(row=3, column=0, padx=self.PADX, pady=self.PADY_ENTRY, sticky=tk.NW)

        self.return_butt = ttk.Button(self.root, text="Return Book", command=self.return_book)
        self.return_butt.grid(row=4, column=0, padx=self.PADX, pady=self.PADY_ENTRY, sticky=tk.NW)

        super().__init__(self.root)

        self.change_theme(self.current_theme)
    
    def update_info(self):
        book = self.combo_name.get()
        if book:
            self.book_taken_out.config(text=f"Num. Taken Out: {self.books[book]['total'] - self.books[book]['in-stock']}")
            self.book_in_stock.config(text=f"Num. In Stock: {self.books[book]['in-stock']}")

    def on_combo_change(self, index, value, op):
        self.update_info()

    def take_out_book(self):
        book = self.combo_name.get()
        if self.books[book]['in-stock'] <= 0:
            messagebox.showerror("Error", "Not Enough Books In Stock")
            return

        temp = self.books
        temp[book]['in-stock'] -= 1
        self.save_to_file(temp)

        self.update_info()

    def return_book(self):
        book = self.combo_name.get()
        if self.books[book]['in-stock'] == self.books[book]['total']:
            messagebox.showerror("Error", "All of these books are already in stock")
            return

        temp = self.books
        temp[book]['in-stock'] += 1
        temp[book]['taken-out'] -= 1
        self.save_to_file(temp)

        self.update_info()
    
class MainApp(Window):
    '''
        The main body of the app, being what everything else is built on top of
    '''

    def __init__(self, root, theme='light'):
        self.root = root
        self.current_theme = theme

        self.title = tk.Label(self.root ,text="Library System", font=self.TITLE_FONT)
        self.title.grid(row=0, column=0, columnspan=2)

        self.main_menu = tk.Frame(self.root)

        self.search_butt = ttk.Button(self.root, text="Search For Book", command=lambda:self.change_window(BookSearch, self.current_theme))
        self.search_butt.grid(row=1, column=0, sticky=tk.NW, pady=self.PADY, padx=self.PADX)

        self.add_butt = ttk.Button(self.root, text="Add Book", command=lambda:self.change_window(BookAdd, self.current_theme))
        self.add_butt.grid(row=1, column=1, sticky=tk.NW, pady=self.PADY)

        self.mgmt_butt = ttk.Button(self.root, text="Manage Books", command=lambda:self.change_window(BookManage, self.current_theme))
        self.mgmt_butt.grid(row=1, column=2, sticky=tk.NW, pady=self.PADY, padx=self.PADX)

        self.theme_butt = ttk.Button(self.root, text="Toggle Theme", command=self.theme_butt)
        self.theme_butt.grid(row=2, column=1, sticky=tk.NW, pady=self.PADY)

        super().__init__(self.root)

        self.change_theme(self.current_theme)

    def theme_butt(self):
        if self.current_theme == 'light':
            self.current_theme = 'dark'
        else:
            self.current_theme = 'light'

        self.change_theme(self.current_theme)
        
    def mainloop(self):
        self.root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    #root.geometry("500x500")
    root.resizable(False, False)

    app = MainApp(root)
    app.mainloop()     