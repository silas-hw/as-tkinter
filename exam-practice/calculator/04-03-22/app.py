import tkinter as tk
import tkinter.ttk as ttk

class MainApp(tk.Frame):

    def __init__(self, root):
        self.root = root
        super().__init__(self.root)

        self.expression = "" # used to store the mathematical expresion that the user enters

        self.display = ttk.Label(self.root)
        self.display.grid(row=0, column=0, sticky=tk.NW)

        self.butt_frame = tk.Frame(self.root) # frame to store buttons in

        self.num_frame = tk.Frame(self.butt_frame) # frame to store the number buttons in

        r = 0
        c = 0
        for num in range(0, 9):
            self.butt = ttk.Button(self.num_frame, text=str(num), command=lambda n=num: self.add_to_expr(str(n)))
            self.butt.grid(row=r, column=c)
            
            # automatically change the row and column of each number
            if c == 2:
                r += 1
                c = 0
            else:
                c += 1


        self.num_frame.grid(row=0, column=0)

        self.op_frame = tk.Frame(self.butt_frame) # frame to store the operation buttons in

        self.butt_add = ttk.Button(self.op_frame, text="+", command=lambda: self.add_to_expr("+"))
        self.butt_add.grid(row=0, column=0)

        self.butt_min = ttk.Button(self.op_frame, text="-", command=lambda: self.add_to_expr("-"))
        self.butt_min.grid(row=1, column=0)

        self.butt_mult = ttk.Button(self.op_frame, text="x", command=lambda: self.add_to_expr("*"))
        self.butt_mult.grid(row=2, column=0)

        self.butt_div = ttk.Button(self.op_frame, text="/", command=lambda: self.add_to_expr("/"))
        self.butt_div.grid(row=3, column=0)

        self.butt_ans = ttk.Button(self.op_frame, text="ans", command=lambda: self.add_to_expr(self.answer))
        self.butt_ans.grid(row=0, column=1)

        self.butt_eq = ttk.Button(self.op_frame, text="=", command=self.calculate)
        self.butt_eq.grid(row=1, column=1)

        self.butt_cls = ttk.Button(self.op_frame, text="cls", command=self.cls)
        self.butt_cls.grid(row=0, column=2)

        self.op_frame.grid(row=0, column=1, sticky=tk.NW)

        self.butt_frame.grid(row=1, column=0, sticky=tk.NW)

    # property method to return answer stored in answer.txt
    @property
    def answer(self):
        with open('answer.txt', 'r') as f:
            out = f.read()

        return out

    # add passed string to expression
    def add_to_expr(self, val:str) -> None:
        self.expression += val
        self.display.config(text=self.expression)

    #calculate expression and update display
    def calculate(self):
        try:
            answer = eval(self.expression)
            self.expression = ""

            with open('answer.txt', 'w') as f:
                f.write(str(answer))

            self.display.config(text=str(answer))
        except Exception as e:
            self.display.config(text="ERROR: Snytax Eror")
            self.expression = ""

    #clear expression and update display
    def cls(self):
        self.expression = ""
        self.display.config(text=self.expression)

# create the tkinter & app instance and begin the mainloop
if __name__ == '__main__': #only run if the file is being executed as the main python file
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()