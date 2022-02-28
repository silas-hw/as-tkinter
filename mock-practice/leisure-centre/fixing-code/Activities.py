# Only works in Python 3 (Created in 3.4.2)
# tkinter comes as part of the standard install - messagebox has to be imported explicitly

from tkinter import *
from tkinter import messagebox

def saveSession() :
    # for each field get the value from the screen and pad with spaces or chop if necessary
    typeSave = typeVar.get()
    typeSave = typeSave.ljust(30)
    sessionSave = sessionVar.get()
    sessionSave = sessionSave.ljust(5)
    daySave = dayVar.get()
    daySave = daySave.ljust(10)
    locationSave = locationVar.get()
    locationSave = locationSave.ljust(30)
    levelSave = levelVar.get()
    levelSave = levelSave.ljust(15)
    
    #open the file to append - if it's not there it'll be created
    fileObject = open("Leisure.txt","a")
    # write to the file with a newline character at the end
    fileObject.write(typeSave + sessionSave + daySave + locationSave + levelSave + "\n")
    fileObject.close()
    
    return

def countSession() :
    SessionCount=0
    CountNeeded=0

    #get the fields off the screen and validate them
    typeSave = typeVar.get()
    if len(typeSave) > 30 :
        messagebox.showerror("Error","Too many characters in Type")
        return
    # . . .=sessionVar.get()
    if len(sessionSave) > 5 :
        messagebox.showerror("Error","Too many characters in Session")
        return
    # . . . = dayVar.get()
    if len(daySave) > 10 :
        messagebox.showerror("Error","Too many characters in Day")
        return
    # . . . = locationVar.get()
    if len(locationSave) > 30 :
        messagebox.showerror("Error","Too many characters in Location")
        return
    # . . . = levelVar.get()
    if len(levelSave) > 15 :
        messagebox.showerror("Error","Too many characters in Level")
        return
 
    if not typeSave == "" :
        CountNeeded +=1
    if not sessionSave == "" :
        CountNeeded +=1
    if not daySave == "" :
        CountNeeded +=1
    if not locationSave == "" :
        CountNeeded +=1
    if not levelSave == "" :
        CountNeeded +=1

    if CountNeeded == 0 :
        messagebox.showerror("Error","Please enter something to count!")
        return
    # try opening the file for reading
    try:
        fileObject=open("Leisure.txt","r")
        
    # if it's not there then say
    except IOError:
        messagebox.showerror("Error","No file to read")

    # if we did open it then let's carry on!
    else:
        while True:
            CountGot=0
            recordVar=fileObject.readline()
            # Python keeps reading till EOF then returns a blank
            if recordVar=="":
                fileObject.close()
                break
         
            if typeSave in recordVar[0:30] and not typeSave=="" :
                CountGot +=1
            if sessionSave in recordVar[30:35] and not sessionSave=="" :
                CountGot +=1
            if daySave in recordVar[35:45] and not daySave=="":
                CountGot +=1
            if locationSave in recordVar[45:75] and not locationSave =="":
                CountGot +=1
            if levelSave in recordVar[75:90] and not levelSave=="":
                CountGot +=1
            if CountGot == CountNeeded:
                SessionCount +=1
                
        messagebox.showinfo("Information", str(SessionCount) + " Sessions have been found! Contact the centre for more information.")    
    
    return


def makeWindow():
    #declared my globals here as this is the 1st routine called
    # the other routines have to be in front of this one as they get called by it
    # and the parser would get upset if they weren't there
    
    global typeVar, sessionVar, dayVar, locationVar, levelVar

    #here's my window
    win = Tk()
    win.wm_title("FitnessCentre")
    #split into two sections then further split into a grid
    frame1=Frame(win)
    frame1.pack()

    Label(frame1, text="Fitness Leisure Centre", font=("Helvetica 12 bold")).grid(row=0, column=0)
    
    Label(frame1, text="Type").grid(row=1, column=0, sticky=W)
    typeVar=StringVar()
    title= Entry(frame1, textvariable=typeVar)
    title.grid(row=1,column=1,sticky=W)

    Label(frame1, text="Session").grid(row=2, column=0, sticky=W)
    sessionVar=StringVar()
    genre= Entry(frame1, textvariable=sessionVar)
    genre.grid(row=2,column=1,sticky=W)

    Label(frame1, text="Day").grid(row=3, column=0, sticky=W)
    dayVar=StringVar()
    director= Entry(frame1, textvariable=dayVar)
    director.grid(row=3,column=1,sticky=W)
    
    Label(frame1, text="Location").grid(row=4, column=0, sticky=W)
    locationVar=StringVar()
    leadactor= Entry(frame1, textvariable=locationVar)
    leadactor.grid(row=4,column=1,sticky=W)
    
    Label(frame1, text="Level").grid(row=5, column=0, sticky=W)
    levelVar=StringVar()
    duration= Entry(frame1, textvariable=levelVar)
    duration.grid(row=5,column=1,sticky=W)

    frame2 = Frame(win)
    frame2.pack()

    # build my buttons in the other frame then pack them side by side
    b1= Button(frame2, text=" Save ", command=saveSession)
    b2= Button(frame2, text=" Count ", command=countSession)
    b1.pack(side=LEFT); b2.pack(side=LEFT)
    
    return win


#this is the main program!
win = makeWindow()
win.mainloop()
