import json, os
import tkinter as tk
from tkinter import ttk #has better looking widgets
from tkinter import messagebox

class Window(tk.Frame):
    '''
        A superclass to create windows from. Includes a change window function to change the content of the root window 
    '''
    FILE_PATH = os.path.dirname(os.path.realpath(__file__)) # gets the directory of the python file, so file operations can be done regardless of the current working directory

    TITLE_FONT = ("Arial", 30, "bold")

    PADX = 10
    PADY = 10
    PADY_ENTRY = 3

    def change_window(self, window):
        for widget in self.root.winfo_children():
            widget.destroy()

        window(self.root)

    @property
    def books(self):
        with open(f"{self.FILE_PATH}\\books.json", "r") as f:
            out = json.load(f)

        return out

    def save_to_file(self, books:dict) -> None:
        if not isinstance(books, dict):
            raise TypeError("Books argument should be a dictionary")

        with open(f"{self.FILE_PATH}\\books.json", "w") as f:
            json.dump(books, f, indent=4)

class BookSearch(Window):

    def __init__(self, root):
        self.root = root

        super().__init__()

        self.title = tk.Label(self.root, text="Search for a Book", font=self.TITLE_FONT)
        self.title.grid(row=0, column=0, columnspan=2)

        self.back_butt = ttk.Button(self.root, text="go back", command=lambda: self.change_window(MainApp))
        self.back_butt.grid(row=1, column=0, sticky=tk.NW, padx=self.PADX)

class BookAdd(Window):

    def __init__(self, root):
        self.root = root

        super().__init__()

        self.title = tk.Label(self.root, text="Add a Book", font=self.TITLE_FONT)
        self.title.grid(row=0, column=0, columnspan=2)

        self.back_butt = ttk.Button(self.root, text="go back", command=lambda:self.change_window(MainApp))
        self.back_butt.grid(row=1, column=0, sticky=tk.NW, padx=self.PADX)

        #========#
        ## form ##
        #========#

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
        self.entry_hardback = ttk.Checkbutton(self.form, text="hardback", variable=self.hardback_val)
        self.entry_hardback.grid(row=4, column=0, pady=self.PADY_ENTRY)

        self.paperback_val = tk.IntVar()
        self.entry_paperback = ttk.Checkbutton(self.form, text="paperback", variable=self.paperback_val)
        self.entry_paperback.grid(row=4, column=1, pady=self.PADY_ENTRY)

        self.label_amount = tk.Label(self.form, text="Amount of Books")
        self.label_amount.grid(row=5, column=0, sticky=tk.NW, pady=self.PADY_ENTRY)

        self.entry_amount = ttk.Spinbox(self.form, from_=1, to=100, wrap=True)
        self.entry_amount.grid(row=5, column=1, sticky=tk.NW, pady=self.PADY_ENTRY)

        self.form.grid(row=2, column=0, columnspan=2, pady=self.PADY, padx=self.PADX)

        #========#

        self.save_butt = ttk.Button(self.root, text="Save Book", command=self.save_book)
        self.save_butt.grid(row=3, column=0, sticky=tk.NW, pady=self.PADY, padx=self.PADX)

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

    def __init__(self, root):
        self.root = root
        super().__init__()

        self.title = tk.Label(self.root, text="Manage Library", font=self.TITLE_FONT)
        self.title.grid(row=0, column=0, columnspan=2)

        self.back_butt = ttk.Button(self.root, text="go back", command=lambda: self.change_window(MainApp))
        self.back_butt.grid(row=1, column=0, padx=self.PADX)

        self.combo_name = ttk.Combobox(self.root, values=[key for key in self.books.keys()])
        self.combo_name.grid(row=2, column=1, pady=self.PADY_ENTRY)  

class MainApp(Window):
    '''
        The main body of the app, being what everything else is built on top of
    '''

    def __init__(self, root):
        self.root = root

        self.title = tk.Label(self.root ,text="Library System", font=self.TITLE_FONT)
        self.title.grid(row=0, column=0, columnspan=2)

        self.main_menu = tk.Frame(self.root)

        self.search_butt = ttk.Button(self.root, text="Search For Book", command=lambda:self.change_window(BookSearch))
        self.search_butt.grid(row=1, column=0, sticky=tk.NW, pady=self.PADY, padx=self.PADX)

        self.add_butt = ttk.Button(self.root, text="Add Book", command=lambda:self.change_window(BookAdd))
        self.add_butt.grid(row=1, column=1, sticky=tk.NW, pady=self.PADY)

        self.mgmt_butt = ttk.Button(self.root, text="Manage Books", command=lambda:self.change_window(BookManage))
        self.mgmt_butt.grid(row=1, column=2, sticky=tk.NW, pady=self.PADY, padx=self.PADX)
        
    def mainloop(self):
        self.root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    #root.geometry("500x500")
    root.resizable(False, False)

    app = MainApp(root)
    app.mainloop()     