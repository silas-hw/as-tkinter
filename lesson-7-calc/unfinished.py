# Only works in Python 3 (Created in 3.4.2)
# tkinter comes as part of the standard install - messagebox has to be imported explicitly


# . . . Means missing or incomplete code. Complete these lines
# Note: There is no requirement to deal with a decimal point or negative numbers.
# Note: There is no requirement to deal with data type conversions or contiunuing to use the values stored on disk (simply store and recall them).


from tkinter import *
from tkinter import messagebox


class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False

        
    def saveResult(self, value):
        CalcMemSave = str(value)
        
     
        fileObject = open("calcResult.txt","w")
        fileObject.write(CalcMemSave)
        fileObject.close()
    

    def getResult(self, resultbox):


        try:
            fileObject=open("calcResult.txt","r")
        
        except IOError:
            messagebox.showerror("Error","No file to read")

        else:
            recordVar=fileObject.readline()
            fileObject.close()
            value = recordVar
            self.current = value
            text_box.delete(0, END)
            text_box.insert(0, value)
     

    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)      
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)

    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(text_box.get())

    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "minus":
            self.total -= self.current
        if self.op == "times":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    def operation(self, op): 
        self.current = float(self.current)
        if self.op_pending:
            self.do_sum()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def cancel(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True
        self.total = 0
        


sum1 = Calc()
root = Tk()
calc = Frame(root)
calc.grid()

root.title("Calc")
text_box = Entry(calc, justify=RIGHT)
text_box.grid(row = 0, column = 0, columnspan = 3, pady = 5)
text_box.insert(0, "0")

numbers = "789456123"
i = 0
bttn = []
for j in range(1,4):
    for k in range(3):
        bttn.append(Button(calc, text = numbers[i]))
        bttn[i].grid(row = j, column = k, pady = 5)
        bttn[i]["command"] = lambda x = numbers[i]: sum1.num_press(x)
        i += 1

bttn_0 = Button(calc, text = "0")
bttn_0["command"] = lambda: sum1.num_press(0)
bttn_0.grid(row = 4, column = 0, pady = 5)

bttn_MS = Button(calc, text = "MS")
bttn_MS["command"] = lambda: sum1.saveResult(text_box.get())
bttn_MS.grid(row = 4, column = 1, pady = 5)

bttn_MR = Button(calc, text = "MR")
bttn_MR["command"] = lambda: sum1.getResult(text_box)
bttn_MR.grid(row = 4, column = 2, pady = 5)

bttn_div = Button(calc, text = "/")
bttn_div["command"] = lambda: sum1.operation("divide")
bttn_div.grid(row = 4, column = 3, pady = 5)

bttn_mult = Button(calc, text = "*")
bttn_mult["command"] = lambda: sum1.operation("times")
bttn_mult.grid(row = 3, column = 3, pady = 5)

minus = Button(calc, text = "-")
minus["command"] = lambda: sum1.operation("minus")
minus.grid(row = 2, column = 3, pady = 5)


add = Button(calc, text = "+")
add["command"] = lambda: sum1.operation("add")
add.grid(row = 1, column = 3, pady = 5)


clear = Button(calc, text = "Clear")
clear["command"] = sum1.cancel
clear.grid(row = 5, column = 1, pady = 5)


equals = Button(calc, text = "  =   ")
equals["command"] = sum1.calc_total
equals.grid(row = 5, column = 2, pady = 5)

root.mainloop()