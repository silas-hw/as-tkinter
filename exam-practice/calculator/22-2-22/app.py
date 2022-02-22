import tkinter as tk
import tkinter.ttk as ttk

class MainApp(tk.Frame):
    
    def __init__(self, root):
        self.root = root
        super().__init__(self.root)

        self.expression = "" #used to store the mathemetical expression the user enters

        self.display = ttk.Label(self.root, font=('Arial', 12))
        self.display.grid(row=0, column=0)

        self.button_frame = tk.Frame(self.root)

        self.numbers_frame = tk.Frame(self.button_frame)
        
        self.num_one = ttk.Button(self.numbers_frame, text="1", command=lambda: self.addToExpression("1"))
        self.num_two = ttk.Button(self.numbers_frame, text="2", command=lambda:self.addToExpression("2"))
        self.num_three = ttk.Button(self.numbers_frame, text="3", command=lambda:self.addToExpression("3"))
        self.num_four = ttk.Button(self.numbers_frame, text="4", command=lambda:self.addToExpression("4"))
        self.num_five = ttk.Button(self.numbers_frame, text="5", command=lambda:self.addToExpression("5"))
        self.num_six = ttk.Button(self.numbers_frame, text="6", command=lambda:self.addToExpression("6"))
        self.num_seven = ttk.Button(self.numbers_frame, text="7", command=lambda:self.addToExpression("7"))
        self.num_eight = ttk.Button(self.numbers_frame, text="8", command=lambda:self.addToExpression("8"))
        self.num_nine = ttk.Button(self.numbers_frame, text="9", command=lambda:self.addToExpression("9"))
        self.num_zero = ttk.Button(self.numbers_frame, text="0", command=lambda:self.addToExpression("0"))
        self.answer = ttk.Button(self.numbers_frame, text="ans", command=lambda:self.addToExpression(self.ans))

        self.num_one.grid(row=0, column=0)
        self.num_two.grid(row=0, column=1)
        self.num_three.grid(row=0, column=2)
        self.num_four.grid(row=1, column=0)
        self.num_five.grid(row=1, column=1)
        self.num_six.grid(row=1, column=2)
        self.num_seven.grid(row=2, column=0)
        self.num_eight.grid(row=2, column=1)
        self.num_nine.grid(row=2, column=2)
        self.num_zero.grid(row=3, column=0)
        self.answer.grid(row=3, column=1)

        self.equals = ttk.Button(self.numbers_frame, text="=", command=self.calc)
        self.equals.grid(row=3, column=2)

        self.numbers_frame.grid(row=1, column=0)

        self.operations_frame = tk.Frame(self.button_frame)

        self.add = ttk.Button(self.operations_frame, text="+", command=lambda:self.addToExpression("+"))
        self.min = ttk.Button(self.operations_frame, text="-", command=lambda:self.addToExpression("-"))
        self.mult = ttk.Button(self.operations_frame, text="x", command=lambda:self.addToExpression("*"))
        self.div = ttk.Button(self.operations_frame, text="/", command=lambda:self.addToExpression("/"))

        self.add.grid(row=0, column=0)
        self.min.grid(row=1, column=0)
        self.mult.grid(row=2, column=0)
        self.div.grid(row=3, column=0)

        self.clear = ttk.Button(self.operations_frame, text="cls", command=self.cls)
        self.clear.grid(row=0, column=1)

        self.operations_frame.grid(row=1, column=1)

        self.button_frame.grid(row=1, column=0, sticky=tk.NW)

    @property
    def ans(self):
        with open('answer.txt') as f:
            out = float(f.read())
        return out

    def addToExpression(self, value: str):
        self.expression += str(value)
        self.display.config(text=self.expression)
    
    def cls(self):
        self.expression = ""
        self.display.config(text="")

    def calc(self):
        try:
            answer = eval(self.expression)
            self.display.config(text=answer)
            self.expression = str(answer)

            with open('answer.txt', 'w') as f:
                f.write(str(answer))
                
        except Exception as e:
            print(e)
            self.display.config(text="SYNTAX ERROR")
            self.expression = ""

if __name__ == '__main__':
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()