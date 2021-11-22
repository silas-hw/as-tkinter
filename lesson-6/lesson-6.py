'''
tkinter input validation
'''
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox

ENTRY_WIDTH = 50 #set constant to be used for the width of entry boxes to keep the gui uniform
BG_COLOR = "lightblue" #set constant to be used for background colours


def save_click():

    plumberID = idEntry.get() #get the plumberID from the idEntry widget
    firstname = fnEntry.get()
    surname = snEntry.get()
    gasSafe = gasVar.get()
    rate = rateVar.get()
    callout = calloutVar.get()
    experience = expVar.get()
    specialism = specVar.get()

    try:
        #assert raises an error if a condition is not met, also allowing us to add a custom excpetion message
        #this means we dont have to do an if statement for each validation check, instead we can wrap
        #several assert statements in side a try and accept
        #this also mean we wont have to write "messagebox.showerror" for each individual error message :)


        assert plumberID, "must enter plumber ID" #check if plumberID is present, if not raise excpetion with message "must enter plumber ID"
        assert len(plumberID) == 4, "plumber ID must be 4 digits"

        assert firstname, "must enter first name"
        assert len(firstname) < 50, "Forename entered too long, must be less than 50 characters"

        assert rate, "must enter hourly rate"
        float(rate) #try converting rate to a float, if an error raises then it is not a float
        assert float(rate)<100 and float(rate)>0, "Hourly rate must be between 0 and 100"

        assert callout, "must enter callout price"

        assert experience, "must enter years of experience"

        assert specialism, "must enter specialism"
        assert specialism.lower() in ["kitchen", "bathroom", "misc"], "specialism must be out of: 'kitchen', 'bathroom', 'misc'"


    except Exception as error:
        messagebox.showerror("ERROR", error) #if an error occurs,  create a messagebox with the text of the error message
        return

    plumberID = plumberID.ljust(50) #justify the variable to the left by 50 characters
    firstname = firstname.ljust(50)
    surname = surname.ljust(50)
    gasSafe = gasSafe.ljust(50)
    rate = rate.ljust(50)
    callout = callout.ljust(50)
    experience = experience.ljust(50)
    specialism = specialism.ljust(50)

    #open text file to appen to with a context manager
    with open("plumbers.txt", "a") as f:
        f.write(f"{plumberID}{firstname}{surname}{gasSafe}{rate}{callout}{experience}{specialism}\n") #write the variables on one line, leaving a newline for the next save

    messagebox.showinfo("Message", "Save successful")
    
    return

def count_click():
    countNeeded = 0 #used to measure how many variables need to be counted
    EntryCount = 0 #used to count how many entries that match the users criteria have been found 

    plumberID = idEntry.get()
    firstname = fnEntry.get()
    surname = snEntry.get()
    gasSafe = gasVar.get()
    rate = rateVar.get()
    callout = calloutVar.get()
    experience = expVar.get()
    specialism = specVar.get()

    if plumberID:
        countNeeded+=1
    if firstname:
        countNeeded+=1
    if surname:
        countNeeded+=1
    if gasSafe:
        countNeeded+=1
    if rate:
        countNeeded+=1
    if callout:
        countNeeded+=1
    if experience:
        countNeeded+=1
    if specialism:
        countNeeded+=1

    if countNeeded==0:
        messagebox.showerror("ERROR", "You have not included anything to search for")
    
    try:
        #open text file to read from
        with open("plumbers.txt", "r") as f:
            while True:
                CountGot = 0 #used to measure how many matching variabls have been found
                recordVar = f.readline() #read one line of the file at a time

                if not recordVar: #if no text on line
                    break #stop reading the file

                #check through each variable to see if it is in the part of the line where it should be saved to
                if plumberID in recordVar[0:50] and plumberID:
                    CountGot += 1
                if firstname in recordVar[50:100] and firstname:
                    CountGot += 1
                if surname in recordVar[100:150] and surname:
                    CountGot += 1
                if gasSafe in recordVar[150:200] and gasSafe:
                    CountGot += 1
                if rate in recordVar[200:250] and rate:
                    CountGot += 1
                if callout in recordVar[250:300] and callout:
                    CountGot += 1
                if experience in recordVar[300:350] and experience:
                    CountGot += 1
                if specialism in recordVar[350:400] and specialism:
                    CountGot += 1

                if CountGot == countNeeded: #if the amount of matching criteria matches the amount needed
                    EntryCount += 1 #increase the entries that match by 1

    except IOError: #if an IOError is raised, meaning an error in writing (input) or reading (output) to/from a file
        messagebox.showerror("ERROR", "error in opening save file :(") #create an error messagebox

    except Exception as error: #if some other error occurs, create a messagebox and display the error message. Prevents the programme from suddenly closing and confusing the user, even if they dont understand the error message
        messagebox.showerror("ERROR", error)

    messagebox.showinfo("Found:", EntryCount) #display the amount of matching entries found in a messagebox


root = Tk() #create a blank window
root.config(bg=BG_COLOR)

#create widgets and place them on the window using the .grid method, creating approptiate variables for entry widgets along the way

titleLabel = Label(root, text="Plumbers", font=("Helvetica", 32), bg=BG_COLOR)
titleLabel.grid(row=0, column=0, columnspan=2, sticky=N)

idLabel = Label(root, text="PlumberID", bg=BG_COLOR)
idLabel.grid(row=1, column=0, sticky=W)

idVar = StringVar()

idEntry = ttk.Entry(root, width=ENTRY_WIDTH, textvariable=idVar)
idEntry.grid(row=1, column=1,  columnspan=2, sticky=W)

fnLabel = Label(root, text="Firstname", bg=BG_COLOR)
fnLabel.grid(row=2, column=0, sticky=W)

fnVar = StringVar()

fnEntry = ttk.Entry(root, width=ENTRY_WIDTH, textvariable=fnVar)
fnEntry.grid(row=2, column=1, columnspan=2, sticky=W)

snLabel = Label(root, text="Surname", bg=BG_COLOR)
snLabel.grid(row=3, column=0, sticky=W)

snVar = StringVar()

snEntry = ttk.Entry(root, width=ENTRY_WIDTH, textvariable=snVar)
snEntry.grid(row=3, column=1,  columnspan=2, sticky=W)

gasLabel = Label(root, text="Gas safe", bg=BG_COLOR)
gasLabel.grid(row=4, column=0, sticky=W)

gasVar = StringVar()

#ttk loves to be unique so its radiobutton doesn't take a bg parameter, instead you have to create
#a style instance and configure a new radiobutton style to have a background
#and then set the style of any new radiobutton to the new style you just configured

style = ttk.Style()
style.configure("S.TRadiobutton", background=BG_COLOR) #it also uses the naming convention of '<name>.T<widget name>', even tho this isnt stated anywhere in the docs, it just does

gasRb = ttk.Radiobutton(root, text="yes", variable=gasVar, value="yes", style="S.TRadiobutton")
gasRb.grid(row=5, column=1, sticky=W)
gasRb = ttk.Radiobutton(root, text="no", variable=gasVar, value="no", style="S.TRadiobutton")
gasRb.grid(row=5, column=2, sticky=W)

rateLabel = Label(root, text="Hourly rate", bg=BG_COLOR)
rateLabel.grid(row=6, column=0, sticky=W)

rateVar = StringVar()

rateEntry = ttk.Entry(root, textvariable=rateVar)
rateEntry.grid(row=6, column=1, columnspan=2, sticky=W)

calloutLabel = Label(root, text="Call out price", bg=BG_COLOR)
calloutLabel.grid(row=7, column=0, sticky=W)

calloutVar = StringVar()

calloutEntry = ttk.Entry(root, textvariable=calloutVar)
calloutEntry.grid(row=7, column=1, columnspan=2, sticky=W)

expLabel = Label(root, text="Years experience", bg=BG_COLOR)
expLabel.grid(row=8, column=0, sticky=W)

expVar = StringVar()

expEntry = ttk.Entry(root, textvariable=expVar)
expEntry.grid(row=8, column=1, columnspan=2)

specLabel = Label(root, text="Specialism", bg=BG_COLOR)
specLabel.grid(row=9, column=0, sticky=W)

specVar = StringVar()

specEntry = ttk.Entry(root, textvariable=specVar)
specEntry.grid(row=9, column=1, columnspan=2)

saveButt = ttk.Button(root, text="SAVE", command=save_click)
saveButt.grid(row=10, column=0, sticky=W)

countButt = ttk.Button(root, text="COUNT", command=count_click)
countButt.grid(row=10, column=1, sticky=W)

#run the windows mainloop, opening the GUI and allowing the program to wait for input
root.mainloop()