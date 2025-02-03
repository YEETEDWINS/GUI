from tkinter import *
import tkinter.font as fn

wn = Tk("RPS")
wn.title("RPS")
wn.geometry("500x300")

baseF = fn.Font(family="Open Sans", size=20)

# Top Frame
tframe = Frame(wn)
tframe.pack()

title = Label(tframe, text="Rock Paper Scissors", font=("Lexend Giga", 30))
title.pack()

result = Label(tframe, text="GOAL!!", font=("Lexend Giga", 15), foreground="green")
result.pack(pady=10)

# Middle Frame
mframe = Frame(wn)
mframe.pack()

options = Label(mframe, text="Your Options:", font=baseF)
options.grid(row=0, column=0, padx=10, pady=5)

rock = Button(mframe, text="Rock", font=baseF)
rock.grid(row=1, column=1, padx=10, pady=5)

paper = Button(mframe, text="Paper", font=baseF)
paper.grid(row=1, column=2, padx=10, pady=5)

scissors = Button(mframe, text="Scissors", font=baseF)
scissors.grid(row=1, column=3, padx=10, pady=5)

score = Label(mframe, text="Score:", font=baseF)
score.grid(row=2,column=0, padx=10, pady=5)

# Bottom Frame
bframe = Frame()
bframe.pack()

pselect = Label(bframe, text="You Selected: ")
pselect.grid(row=0,column=0, padx=10)

cselect = Label(bframe, text="CPU Selected: ")
cselect.grid(row=1,column=0, padx=10)

pscore = Label(bframe, text="Your Score: ")
pscore.grid(row=0,column=1, padx=10)

cscore = Label(bframe, text="CPU Score: ")
cscore.grid(row=1,column=1, padx=10)

wn.mainloop()