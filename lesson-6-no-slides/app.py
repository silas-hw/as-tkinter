import tkinter as tk
import tkinter.ttk as ttk

class MainApp(tk.Frame):

    def __init__(self, root):
        self.root = root

        self.label_title = tk.Label(self.root, text="Plumbers", font=("Arial", "20", "bold"))
        self.label_title.grid(row=0, column=0, sticky=tk.NSEW)

        self.label_id = tk.Label(self.root, text="Plumber ID")
        self.label_id.grid(row=1, column=0, sticky=tk.W)

        self.entry_id = ttk.Entry(self.root)
        self.entry_id.grid(row=1, column=1, sticky=tk.E)

        self.label_fn = tk.Label(self.root, text="Firstname")
        self.label_fn.grid(row=2, column=0, sticky=tk.W)

        self.entry_fn = ttk.Entry(self.root)
        self.entry_fn.grid(row=2, column=1, sticky=tk.E)

        self.label_sn = tk.Label(self.root, text="Surname")
        self.label_sn.grid(row=3, column=0, sticky=tk.W)

        self.entry_sn = ttk.Entry(self.root)
        self.entry_sn.grid(row=3, column=1, sticky=tk.E)

        self.label_gas = tk.Label(self.root, text="Gas Safe?")
        self.label_gas.grid(row=4, column=0, sticky=tk.W)

        self.gas_value = tk.BooleanVar()

        self.radio_frame = tk.Frame(self.root)

        self.radio_gas_y = ttk.Radiobutton(self.radio_frame, text="yes", value=True, variable=self.gas_value)
        self.radio_gas_n = ttk.Radiobutton(self.radio_frame, text="no", value=False, variable=self.gas_value)

        self.radio_gas_y.grid(row=0, column=0, sticky=tk.E)
        self.radio_gas_n.grid(row=0, column=1, sticky=tk.W)
        self.radio_frame.grid(row=4, column=1)

        self.label_rate = tk.Label(self.root, text="Hourly Rate")
        self.label_rate.grid(row=5, column=0, sticky=tk.W)

        self.spin_rate = ttk.Spinbox(self.root, from_=0, to=10000, increment=0.5)
        self.spin_rate.grid(row=5, column=1, sticky=tk.E)

        self.label_callout = tk.Label(self.root, text="Callout Price")
        self.label_callout.grid(row=6, column=0, sticky=tk.W)

        self.spin_callout = ttk.Spinbox(self.root, from_=0, to=10000, increment=0.5)
        self.spin_callout.grid(row=6, column=1, sticky=tk.E)

        self.label_exp = tk.Label(self.root, text="Years Experience")
        self.label_exp.grid(row=7, column=0, sticky=tk.W)

        self.spin_exp = ttk.Spinbox(self.root, from_=1, to=100, increment=1)
        self.spin_exp.grid(row=7, column=1, sticky=tk.E)

        self.label_spec = tk.Label(self.root, text="Specialism")
        self.label_spec.grid(row=8, column=0, sticky=tk.W)

        self.combo_spec = ttk.Combobox(self.root, values=("bath", "kitchen", "outside"))
        self.combo_spec.grid(row=8, column=1, sticky=tk.E)

        super().__init__(self.root)
    
    def mainloop(self):
        self.root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()

    app = MainApp(root)
    app.mainloop()