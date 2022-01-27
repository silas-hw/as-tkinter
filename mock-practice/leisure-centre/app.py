import datetime
import json
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

class Window(tk.Frame):

    def __init__(self, root):
        self.root = root
        super().__init__(self.root)

    @property
    def users(self):
        with open("users.json") as f:
            out = json.load(f)
        return out

    @property
    def logs(self):
        with open("logs.json") as f:
            out = json.load(f)
        return out

    def change_window(self, window):
        for widget in self.root.winfo_children():
            widget.destroy()

        window(self.root)

class ClientHome(Window):

    def __init__(self, root):
        self.root = root

        self.title_label = ttk.Label(self.root, text="Client Home")
        self.title_label.grid(row=0, column=0, sticky=tk.NW)

        super().__init__(self.root)   

class AdminHome(Window):

    def __init__(self, root):
        self.root = root

        self.title_label = ttk.Label(self.root, text="Admin Home")
        self.title_label.grid(row=0, column=0, sticky=tk.NW)

        self.logout_butt = ttk.Button(self.root, text="logout", commnad=lambda: self.change_window(Login))
        self.logout_butt.grid(row=0, column=1, sticky=tk.NE)

        super().__init__(self.root)

class Login(Window):

    def __init__(self, root):
        self.root = root

        self.title_label = ttk.Label(text="Login")
        self.title_label.grid(row=0, column=0, sticky=tk.NSEW)

        self.id_entry = ttk.Entry(self.root)
        self.id_entry.grid(row=1, column=0, sticky=tk.NSEW)

        self.password_entry = ttk.Entry(self.root)
        self.password_entry.grid(row=2, column=0, sticky=tk.NSEW)

        self.login_butt = ttk.Button(self.root, text="Enter", command=self.login)
        self.login_butt.grid(row=3, column=0, sticky=tk.NE)

        super().__init__(self.root)

    def login(self):
        id = self.id_entry.get()
        password = self.password_entry.get()
        # validation
        try:
            assert id, "please enter an id"
            assert id in self.users.keys(), "id and password do not match"
            int(id)
            assert len(id)==4, "id must be 4 digits long"

            assert password, "please enter a password"

        except Exception as e:
            messagebox.showerror("Error with login!", e)
            return

        if password == self.users[id]["password"]:
            if self.users[id]["access"] == 0:
                self.change_window(ClientHome)
            else:
                self.change_window(AdminHome)
        else:
            messagebox.showerror("Error with login!", "id and password do not match")

if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()
