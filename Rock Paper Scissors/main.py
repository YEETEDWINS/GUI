from tkinter import *
import tkinter.font as fn
import random

scp = 0
scc = 0

def Game(player):
  global scp, scc
  choices = ["Rock", "Paper", "Scissors"]
  cpu = random.choice(choices)
  pselect.config(text="You Selected: "+player)
  cselect.config(text="CPU Selected: "+cpu)

  if cpu == player:
    result.config(text="Tie...")
  elif (player == "Rock" and cpu == "Scissors") or (player == "Paper" and cpu == "Rock") or (player == "Scissors" and cpu == "Paper"):
    result.config(text="WINNNNNNN")
    scp += 1
  else:
    result.config(text="What a loss")
    scc += 1

  percentage = round(scp/(scp+scc)*100, 2)
  pscore.config(text="Your Score: "+str(scp))
  cscore.config(text="CPU Score: "+str(scc))
  ratio.config(text="Ratio: "+str(percentage))


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

rock = Button(mframe, text="Rock", font=baseF, command=lambda:Game("Rock"))
rock.grid(row=1, column=1, padx=10, pady=5)

paper = Button(mframe, text="Paper", font=baseF, command=lambda:Game("Paper"))
paper.grid(row=1, column=2, padx=10, pady=5)

scissors = Button(mframe, text="Scissors", font=baseF, command=lambda:Game("Scissors"))
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

# Ratio
ratio = Label(wn, font=("", 20), text="Win Ratio: ")
ratio.pack()

wn.mainloop()