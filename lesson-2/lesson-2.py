'''
basic python tkinter gui dictionary with support for aliases and use of json files

The alias dict contains all the terms a user would actually search, linking them each to the id.
Each definition only has one id, allowing multiple terms to be linked to one definition.

This is useful for synonyms, words with multiple spellings or abreviations (e.g chs for cardiff high school)
'''
from tkinter import *
import json
import os

cwd = os.getcwd()

#importing alias and definitions
with open(f"{cwd}\\alias.json", 'r') as f:
    alias = json.load(f)

with open('definitions.json', 'r') as f:
    definitions = json.load(f)


#commands

def butt_search():
    term=entry1.get() #gets what is entered into the entry box

    out_text.delete(0.0, END) #deletes current text in the out_text

    try:
        out = definitions[alias[term]] #gets the relevant definition for what the user is searching for
        
    except:
        out = 'that word does not currently have a definition' #if the definition does not exist, it output an error message

    out_text.insert(END, out) #inserts the definition into out_text

def add_dict():
    key = entry_key.get() #gets key entered by user
    term = entry_term.get() #gets term entered by user

    idNum = len(definitions)+1
    id = f"id{idNum}"

    out_text.delete(0.0, END)

    if not term or not key:
        msg = 'ERROR: term or key entry box empty'
    elif key in alias or term in definitions:
        msg = 'ERROR: term or key already exists'
    else:
        msg = 'SUCCESS: term and key added!'

        alias[key] = id
        definitions[id] = term

        with open(f'{cwd}\\alias.json', 'w') as f:
            json.dump(alias, f)

        with open(f'{cwd}\\definitions.json', 'w') as f:
            json.dump(definitions, f)

    out_text.insert(END, msg)


#gui

root = Tk()
root.title("Dictionary GUI")

entry1 = Entry(root, width=30, bg='light green')
entry1.grid(row=0, column=0, columnspan=2)

but1 = Button(root, text="SEARCH", command=butt_search)
but1.grid(row=1, column=0, columnspan=2)

out_text = Text(root, width=30, height=10, wrap=WORD, background="light blue")
out_text.grid(row=2, column=0, columnspan=2)


entry_key = Entry(root, textvariable="Enter Key", bg="light gray")
entry_key.grid(row=3, column=0, sticky=W)

entry_term = Entry(root, textvariable="Enter term", bg="light gray")
entry_term.grid(row=3, column=1)

butt_add = Button(root, text="ADD", command=add_dict)
butt_add.grid(row=4, column=0, columnspan=2)

entry_key.insert(END, 'Enter key')
entry_term.insert(END, 'Enter term')

root.mainloop()