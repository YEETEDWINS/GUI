from tkinter import *

wn = Tk("Background")
wn.title("List")
wn.geometry("500x500")

def changeBG():
  colindex = colours.curselection()
  col = colours.get(colindex)
  wn.config(background=col)

seperate = Frame(wn)
seperate.place(x=125, y=300)

scroll = Scrollbar(seperate)

colours = Listbox(seperate, width=30, height=10, yscrollcommand=scroll.set)
colours.pack(side=LEFT, anchor="center", )
colours.insert(END, "red", "blue", "green", "yellow", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",)

scroll.pack(fill=Y)
scroll.config(command=colours.yview)

action = Button(wn, text="Change Colour", command=changeBG)
action.place(x=250,y=200,anchor="center")

wn.mainloop()