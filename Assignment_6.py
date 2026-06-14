from tkinter import *
from tkinter import ttk 
import tkinter.font as tFont

window = Tk()
window.title("Calculator")
window.geometry("500x500")

custom_font = tFont.Font(family="Times New Roman", size=15, weight = 'bold')
label= ttk.Label(text = "Welcome to Calculator.",font=custom_font,padding=15)
label.pack()

e = Entry(window, width = 50, borderwidth = 6)

e.place(x=10, y=60)

def Click(n):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(n))

button =Button(window, text = "1", width = 12, command = lambda : Click(1))
button.place(x=0, y=120)

button =Button(window, text = "2", width = 12, command = lambda : Click(2))
button.place(x=80, y=120)

button =Button(window, text = "3", width = 12, command = lambda : Click(3))
button.place(x=170, y=120)

button =Button(window, text = "4", width = 12, command = lambda : Click(4))
button.place(x=0, y=180)

button =Button(window, text = "5", width = 12, command = lambda : Click(5))
button.place(x=80, y=180)

button =Button(window, text = "6", width = 12, command = lambda : Click(6))
button.place(x=170, y=180)

button =Button(window, text = "7", width = 12, command = lambda : Click(7))
button.place(x=0, y=240)

button =Button(window, text = "8", width = 12, command = lambda : Click(8))
button.place(x=80, y=240)

button =Button(window, text = "9", width = 12, command = lambda : Click(9))
button.place(x=170, y=240)

button =Button(window, text = "0", width = 12, command = lambda : Click(0))
button.place(x=0, y=300)

def add():
      n1= e.get()
      global math
      math = "addition"
      global i
      i = int(n1)
      e.delete(0, END)

button =Button(window, text = "+", width = 12, command = add)
button.place(x=80, y=300)

def sub():
      n1= e.get()
      global math
      math = "subtraction"
      global i
      i = int(n1)
      e.delete(0, END)

button =Button(window, text = "-", width = 12, command = sub)
button.place(x=170, y=300)

def mul():
      n1= e.get()
      global math
      math = "multiplication"
      global i
      i = int(n1)
      e.delete(0, END)

button =Button(window, text = "*", width = 12, command = mul)
button.place(x=0, y=350)

def div():
      n1= e.get()
      global math
      math = "division"
      global i
      i = int(n1)
      e.delete(0, END)

button =Button(window, text = "/", width = 12, command = div)
button.place(x=80, y=350)

def equal():
      n2 = e.get()
      e.delete(0, END)
      if math == "addition":
            e.insert(0, i + int(n2))
      elif math == "subtraction":
            e.insert(0, i - int(n2))
      elif math == "multiplication":
            e.insert(0, i * int(n2))
      elif math == "division":
            e.insert(0, i / int(n2))

button =Button(window, text = "=", width = 12, command = equal)
button.place(x=170, y=350)

def clear():
      e.delete(0, END)

button =Button(window, text = "clear", width = 12, command = clear)
button.place(x=10, y=400)


window.mainloop()