from tkinter import *
from tkinter import messagebox

wn = Tk()
wn.title("Game")
wn.geometry("200x200")

messagebox.showinfo(message="Some message")
messagebox.showwarning(title="Guess the Number!", message="AHHHJHHH!")
messagebox.showerror(title="Guess the Number!", message="you messed up")
print(messagebox.askquestion("Tieeks", message="Yes or No?"))
print(messagebox.askokcancel("Tieeks", message="just choose"))
print(messagebox.askyesno("Tieeks", message="just choose"))
print(messagebox.askretrycancel("Tieeks", message="retryorcanclke"))