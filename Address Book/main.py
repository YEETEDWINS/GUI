from tkinter import *
from tkinter import messagebox

wn = Tk("Address Book")
wn.geometry("600x600")
wn.title("Address Book")

addressbook = {}

def addUpdate():
  personName = nameInput.get()
  personMobile = mobileInput.get()
  personAddress = addressInput.get()
  personEmail = emailInput.get()                                                                                              
  personDOF = dofInput.get()
  if personName != "":
    if personName not in addressbook:
      storage.insert(0, personName)
    addressbook[personName] = [personAddress, personMobile, personEmail, personDOF]
    print(addressbook)
  else:
    messagebox.showwarning("Error", "No name has been prodivded")

  clEntries()

def clEntries():
  nameInput.delete(0, END)
  mobileInput.delete(0, END)
  addressInput.delete(0, END)
  emailInput.delete(0, END)
  dofInput.delete(0, END)

def editEntries():
  clEntries()
  item = storage.curselection()
  if item:
    selectedName = storage.get(item) 
    nameInput.insert(0, selectedName)
    details = addressbook[selectedName]
    addressInput.insert(0, details[0])
    mobileInput.insert(0, details[1])
    emailInput.insert(0, details[2])
    dofInput.insert(0, details[3])
  else:
    messagebox.showwarning("Error 101", "Select a name!!!")

## TOP FRAME
tframe = Frame(wn)
tframe.pack()

filename = Label(tframe, text="Address Book")
filename.grid(row=1, column=1, padx=15)

open = Button(tframe, text="Open")
open.grid(row=1, column=2, padx=95, pady=20)

save = Button(tframe, text="Save")
save.grid(row=1, column=3)

## MIDDLE FRAME
mframe = Frame(wn)
mframe.pack()

# Left Frame
leftframe = Frame(mframe)
leftframe.pack(side=LEFT, padx=20)

storage = Listbox(leftframe, height=15, width=25)
storage.pack()

edit = Button(leftframe, text="Edit", command=editEntries)
edit.pack(side=LEFT, padx=30, ipadx=5)
delete = Button(leftframe, text="Delete")
delete.pack(side=LEFT)

# Right Frame
rightframe = Frame(mframe)
rightframe.pack(side=LEFT)

name = Label(rightframe, text="Name :")
name.grid(row=1, column=1, padx=10, pady=10)
nameInput = Entry(rightframe)
nameInput.grid(row=1, column=2, padx=10, pady=10)

address = Label(rightframe, text="Address :")
address.grid(row=2, column=1, padx=10, pady=10)
addressInput = Entry(rightframe)
addressInput.grid(row=2, column=2, padx=10, pady=10)

mobile = Label(rightframe, text="Mobile :")
mobile.grid(row=3, column=1, padx=10, pady=10)
mobileInput = Entry(rightframe)
mobileInput.grid(row=3, column=2, padx=10, pady=10)

email = Label(rightframe, text="E-mail :")
email.grid(row=4, column=1, padx=10, pady=10)
emailInput = Entry(rightframe)
emailInput.grid(row=4, column=2, padx=10, pady=10)

dof = Label(rightframe, text="Date of Birth :")
dof.grid(row=5, column=1, padx=10, pady=10)
dofInput = Entry(rightframe)
dofInput.grid(row=5, column=2, padx=10, pady=10)

hidden = Label(rightframe)
hidden.grid(row=6, column=2, padx=10)

addupd = Button(rightframe, text="Add / Update", command=addUpdate)
addupd.grid(row=7, column=1, columnspan=2, ipadx=30, pady=0)

wn.mainloop()