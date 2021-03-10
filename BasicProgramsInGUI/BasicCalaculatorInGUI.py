from tkinter import *
import tkinter as tk

window = tk.Tk(className = "calculator")

number1Frame=tk.Frame()
numLbl1 = tk.Label(text = "Number 1:", master = number1Frame)
numLbl1.pack(side=LEFT)
numTxt1 = tk.Entry(fg="blue",bg="#66FFCC", master = number1Frame)
numTxt1.pack(side=LEFT)
number1Frame.pack()

number2Frame=tk.Frame()
numLbl2 = tk.Label(text = "Number 2:", master = number2Frame)
numLbl2.pack(side=LEFT)
numTxt2 = tk.Entry(fg="blue",bg="#66FFCC", master = number2Frame)
numTxt2.pack(side=LEFT)
number2Frame.pack()


window.mainloop()
print("end")