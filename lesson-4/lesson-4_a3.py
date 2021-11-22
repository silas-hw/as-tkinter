'''
a tkinter programme displaying various types of *a d v a n c e d* widgets
with saving
'''
import tkinter as tk
from typing import Text
from typing_extensions import IntVar #is better for resource management, only loads what you need and not everything

#button commands

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

    out_text.delete(0.0, tk.END)
    out_text.insert(tk.END, out)

def save_click():
    name = entryName.get()
    age = spinAge.get()
    gender = genderVar.get()

    hobby1 = hobbyVar1.get()
    hobby2 = hobbyVar2.get()
    
    hobbyOut1 = "Skateboarding".ljust(50) if hobby1 else "" #tenary operator (one line if statement for assignment)
    hobbyOut2 = "Music".ljust(50) if hobby2 else ""

    out = f"{name.ljust(50)}{str(age).ljust(50)}{gender.ljust(50)}{hobbyOut1}{hobbyOut2}\n"

    with open("saved-entries-table.txt", "a") as f:
        f.write(out)

    out_text.delete(0.0, tk.END)
    out_text.insert(tk.END, "Data saved to file")

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

out_text = tk.Text(root, width=30, height=10, wrap=tk.WORD)
out_text.grid(row=11, column=0)

displayButt = tk.Button(root, text="SUBMIT", command=display_click)
displayButt.grid(row=12, column=0)

saveButt = tk.Button(root, text="SAVE", command=save_click)
saveButt.grid(row=13, column=0, sticky=tk.W)

root.mainloop()