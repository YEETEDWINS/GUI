from tkinter import *

def printSomething():
  statement = response.get()
  new.config(text=statement)
  new.pack()

wn = Tk()
wn.geometry("512x512")
wn.title("The Screen")
wn.config(background="white")

text = Label(wn, text="Username :", background="white", foreground="black", font=("Apple Chancery", 30))
text.pack(side=LEFT)

response = Entry(wn)
response.pack(side=RIGHT)

new = Label(wn)

cancel = Button(wn, text="Cancel", foreground="black", command=wn.destroy)
cancel.pack(side=BOTTOM)
login = Button(wn, text="Login", foreground="black", command=printSomething)
login.pack(side=BOTTOM)

wn.mainloop()