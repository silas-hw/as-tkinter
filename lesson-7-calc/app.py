import tkinter as tk
import tkinter.ttk as ttk

from tkinter import messagebox

class Calc(tk.Frame):

    def __init__(self, root):
        super().__init__(root)

        self.root = root

        self.expression = '' #stores the mathematical expression that the user enters
        self.last_result = None #stores the last result if the user chooses to save it

        self.display = ttk.Label(text='')
        self.display.grid(row=0, column=0, sticky=tk.NW)

        self.num_frame = tk.Frame(self.root)

        #automatically organise number buttons in grid
        r = 0
        c = 0
        for i in range(0, 9):
            butt_num = ttk.Button(self.num_frame, text=str(i), command=lambda num=i: self.add_to_expression(str(num)))
            butt_num.grid(row=r, column=c)

            if c>2:
                r+=1
                c=0
            else:
                c+=1

        self.operand_frame = tk.Frame(self.root)

        self.butt_add = ttk.Button(self.operand_frame, text='+', command=lambda: self.add_to_expression('+'))
        self.butt_add.grid(row=0, column=0, sticky=tk.NW)

        self.butt_sub = ttk.Button(self.operand_frame, text='-', command=lambda: self.add_to_expression('-'))
        self.butt_sub.grid(row=1, column=0, sticky=tk.NW)

        self.butt_mult = ttk.Button(self.operand_frame, text='x', command=lambda: self.add_to_expression('*'))
        self.butt_mult.grid(row=2, column=0, sticky=tk.NW)

        self.butt_div = ttk.Button(self.operand_frame, text='-', command=lambda: self.add_to_expression('/'))
        self.butt_div.grid(row=3, column=0, sticky=tk.NW)
        
        self.butt_equals = ttk.Button(self.operand_frame, text='=', command=self.calculate)
        self.butt_equals.grid(row=4, column=0, sticky=tk.NW)

        self.butt_save_result = ttk.Button(self.operand_frame, text='MS', command=self.store_result)
        self.butt_save_result.grid(row=0, column=1, sticky=tk.NW)

        self.butt_get_result = ttk.Button(self.operand_frame, text='MR', command=lambda: self.add_to_expression(str(self.saved_result)))
        self.butt_get_result.grid(row=1, column=1)

        self.butt_clear = ttk.Button(self.operand_frame, text='CLS', command=self.clear)
        self.butt_clear.grid(row=2, column=1, sticky=tk.NW)

        self.operand_frame.grid(row=1, column=1)

        self.num_frame.grid(row=1, column=0, sticky=tk.NW)

    @property
    def saved_result(self):
        try:
            with open('calcResult.txt', 'r') as f:
                result = int(f.read())

            return result
        except IOError:
            messagebox.showerror('Error', 'File Not Found')
        except ValueError:
            messagebox.showerror('Error', 'calcResult.txt stores none-number value')

        return 0

    def add_to_expression(self, value):
        self.expression += value
        self.display.config(text=self.expression)

    def clear(self):
        self.expression = ''
        self.display.config(text='')

    def calculate(self):
        try:
            result = eval(self.expression)
            self.last_result = result
        except:
            result = 'Syntax Error'
        
        self.expression = ''
        self.display.config(text=result)

    def store_result(self):
        if self.last_result != None:
            try:
                with open('calcResult.txt', 'w') as f:
                    f.write(str(self.last_result))
            except IOError:
                messagebox.showerror('Error',  'File Not Found')
        
if __name__ == '__main__':
    root = tk.Tk()
    calc = Calc(root)

    calc.root.mainloop()