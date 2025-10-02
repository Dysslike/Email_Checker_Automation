from tkinter import *
from tkinter import ttk




def Showname(args):
    name_show.set(name())
    

root = Tk()
root.title("Did you get hired?")


mainframe = ttk.Frame(root, padding =(3, 3, 12 , 12))
mainframe.grid(column=0, row=0, sticky = (N, W, E, S))

name = StringVar()
name_entry = ttk.Entry(mainframe, width=7, textvariable=name)
name_entry.grid(column=2, row=1,sticky=(W,E))

ttk.Label(mainframe,text="Enter Name").grid(column=1,row=1,sticky=(W, E))

ttk.Button(mainframe,text="printname",).grid(column=2,row=2,sticky=(W, E))

name_show = StringVar()
ttk.Label(mainframe,textvariable=name_show).grid(column=2,row=3,sticky=(W, E))

root.mainloop()