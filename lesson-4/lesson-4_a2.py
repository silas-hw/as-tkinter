'''
a tkinter programme displaying various types of *a d v a n c e d* widgets
with saving
'''
import tkinter as tk
from typing import Text
from typing_extensions import IntVar #is better for resource management, only loads what you need and not everything
import json
import os

cwd = os.getcwd()

#variables

displayIndex = 0 #used to display next and previous saved entries

#button commands

def save_click():
    name = nameVar.get()
    age = ageVar.get()
    gender = genderVar.get()

    hobby1 = hobbyVar1.get()
    hobby2 = hobbyVar2.get()

    saveDict = {}

    saveDict["name"] = name
    saveDict["age"] = age
    saveDict["gender"] = gender
    saveDict["hobby1"] = "Skateboarding" if hobby1 else "n/a" #tenary operator
    saveDict["hobby2"] = "Music" if hobby1 else "n/a"

    
    with open(f"{cwd}\\saved-entries.txt", "r") as f:
        currentSave = [json.loads(line) for line in f] #a weird way to do it, but much safer than using eval(f.read()), refer to readme for more info

    currentSave.append(saveDict)

    with open(f"{cwd}\\saved-entries.txt", "w") as f:
        for save in currentSave:
            f.write(f"{json.dumps(save)}\n") #saves each dict in the list of dicts to txt file, with each dict being on a newline

def display_click():
    name = nameVar.get()
    age = ageVar.get()
    gender = genderVar.get()

    out = f"{name}\n{age}\n{gender}\nHobbies:\n"

    if hobbyVar1.get():
        out+="Skateboarding\n"

    if hobbyVar2.get():
        out+="Music\n"

    if not hobbyVar1.get() and not hobbyVar2.get():
        out+="none"

    outText.delete(0.0, tk.END)
    outText.insert(tk.END, out)

def get_entry(displacement):
    global displayIndex

    maxCheck = displayIndex+displacement #used to check if displacement will remain within the bounds of the savedEntries list

    if  maxCheck < len(savedEntries) and maxCheck >= 0: #if displacement stays within the length of the list, increase the displayIndex
        displayIndex += displacement

    entry = savedEntries[displayIndex] #get entry from list

    out = ""

    #organise the answers in the entry into a string to be displayed
    for term in entry:
        out += f"{entry[term]}\n"

    outText.delete(0.0, tk.END)
    outText.insert(tk.END, out)

#gui

root = tk.Tk()
root.title("Widgets Galore")

label1 = tk.Label(root, text="Questionnaire")
label1.grid(row=0, column=0, columnspan=2, sticky=tk.N)

label2 = tk.Label(root, text="Name: ")
label2.grid(row=1, column=0)

label3 = tk.Label(root, text="Age: ")
label3.grid(row=2, column=0)

label4 = tk.Label(root, text="How do you identify?")
label4.grid(row=3, column=0)

label5 = tk.Label(root, text="Hobbies: ")
label5.grid(row=8, column=0)

nameVar = tk.StringVar()
entryName = tk.Entry(root, textvariable=nameVar, width=20)
entryName.grid(row=1, column=1, sticky=tk.W)

ageVar = tk.IntVar()
spinAge = tk.Spinbox(root, textvariable=ageVar, from_=1, to=150, width=20)
spinAge.grid(row=2, column=1, sticky=tk.W)

genderVar = tk.StringVar()
genderRb = tk.Radiobutton(root, text="Other", variable=genderVar, value="other")
genderRb.grid(row=4, column=0, sticky=tk.W)
genderRb = tk.Radiobutton(root, text="Male", variable=genderVar, value="male")
genderRb.grid(row=5, column=0, sticky=tk.W)
genderRb = tk.Radiobutton(root, text="Female", variable=genderVar, value="female")
genderRb.grid(row=6, column=0, sticky=tk.W)
genderRb = tk.Radiobutton(root, text="Non-binary", variable=genderVar, value="non-binary")
genderRb.grid(row=7, column=0, sticky=tk.W)

hobbyVar1 = tk.IntVar()
hobbyCheck1 = tk.Checkbutton(root, text="Skateboarding", variable=hobbyVar1)
hobbyCheck1.grid(row=9, column=0)

hobbyVar2 = tk.IntVar()
hobbyCheck2 = tk.Checkbutton(root, text="Music", variable=hobbyVar2)
hobbyCheck2.grid(row=10, column=0)

outText = tk.Text(root, width=30, height=10, wrap=tk.WORD)
outText.grid(row=11, column=0)

displayButt = tk.Button(root, text="SUBMIT", command=display_click)
displayButt.grid(row=12, column=0)

saveButt = tk.Button(root, text="SAVE", command=save_click)
saveButt.grid(row=13, column=0, sticky=tk.W)

nextButt = tk.Button(root, text="Next", command=lambda: get_entry(1))
nextButt.grid(row=14, column=1)

prevButt = tk.Button(root, text="Previous", command=lambda: get_entry(-1))
prevButt.grid(row=14, column=0)

#load saved data

try:
    with open(f"{cwd}\\saved-entries.txt", "r") as f:
        savedEntries = [json.loads(line) for line in f] #a weird way to do it, but much safer than using eval(f.read()), refer to readme for more info

    outText.delete(0.0, tk.END)
    outText.insert(tk.END, "Previously saved data loaded")
except:
    outText.delete(0.0, tk.END)
    outText.insert(0.0, "No previously saved data found")

root.mainloop()