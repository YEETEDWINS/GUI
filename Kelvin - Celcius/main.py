from tkinter import *

def conversion():
  print("hello")
  celcius = cinput.get()
  kelvin = kinput.get()
  print(celcius+" word")
  print(kelvin+" word")
  if celcius != "" and kelvin == "":
    print("celcius")
    celcius = int(celcius)
    value = round(celcius+273.15, 2)
    kinput.insert(0, value)
  elif celcius == "" and kelvin != "":
    print("kelvin")
    kelvin = int(kelvin)
    value = round(kelvin-273.15, 2)
    cinput.insert(0, value)

wn = Tk()
wn.title("Temp Converter")
wn.config(background="white")
wn.geometry("500x500")

title = Label(wn, text="Temperature Converter (C and K)")
title.grid(row=0, column=0, columnspan=2, pady=75)

ctitle = Label(wn, text="Celcius")
ctitle.grid(row=1, column=0)
ktitle = Label(wn, text="Kelvin")
ktitle.grid(row=1, column=1)

cinput = Entry(wn)
cinput.grid(row=2, column=0, padx=25)
kinput = Entry(wn)
kinput.grid(row=2, column=1, padx=25)

converter = Button(wn, text="Convert!", font=("Bradley Hand", 30), command=conversion)
converter.grid(row=3, column=0, columnspan=2, pady=100)

wn.mainloop()