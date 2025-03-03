from tkinter import *

wn = Tk("Address Book")
wn.geometry("600x600")

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

## BOTTOM FRAME
bframe = Frame(wn)
bframe.pack()

edit = Button(bframe, text="Edit")
edit.grid(row=1, column=1)
delete = Button(bframe, text="Delete")
delete.grid(row=1, column=2)

addupd = Button(bframe, text="Add / Update")
addupd.grid(row=1, column=4, columnspan=2)

wn.mainloop()