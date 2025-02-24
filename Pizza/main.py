from tkinter import *
from tkinter.ttk import *
from time import strftime

def placeOrder():
  completed.config(text=f"You ordered {amount.get()} {pizza.get()} pizzas. ETA: {strftime('%H: %M: %S')}")

wn = Tk("Dominos")
wn.geometry("500x300")

title = Label(wn, font=("Comic Sans", 20), text="Welcome to Dominos!")
title.pack(pady=30)

## TOP FRAME
TF = Frame(wn)
TF.pack()

# Main frame
mainframe = Frame(TF)
mainframe.pack(side=LEFT, padx=20)

pizzaLabel = Label(mainframe, text="Choose your Pizza: ")
pizzaLabel.grid(column=1, row=1)

pizzas = ["Margherita", "Pepperoni", "Hawai", "BBQ Chicken"]
pizza = StringVar()
pizza.set(pizzas[0])
pizzaSelector = OptionMenu(mainframe, pizza, *pizzas)
pizzaSelector.grid(column=2, row=1, pady=10)

quantityLabel = Label(mainframe, text="Choose the Amount: ")
quantityLabel.grid(column=1, row=2)
amount = IntVar()
amount.set(1)
quantitySelector = Combobox(mainframe, textvariable=amount, values=list(range(1,6)))
quantitySelector.grid(column=2, row=2)

# Radio Frame
radioframe = Frame(TF)
radioframe.pack(side=LEFT)

size = StringVar()
size.set("medium")
largeb = Radiobutton(radioframe, text="L", value="large", variable=size)
largeb.grid(column=0, row=0)
mediumb = Radiobutton(radioframe, text="M", value="medium", variable=size)
mediumb.grid(column=0, row=1, pady=5)
smallb = Radiobutton(radioframe, text="S", value="small", variable=size)
smallb.grid(column=0, row=2)

## BOTTOM FRAME
BF = Frame(wn)
BF.pack()


order = Button(BF, text="Order!", command=placeOrder)
order.pack(pady=20)

completed = Label(BF, text="")
completed.pack()

wn.mainloop()