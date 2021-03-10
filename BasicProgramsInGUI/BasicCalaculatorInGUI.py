from tkinter import *
import tkinter as tk

def multiplacation_Handler(event):
    n1 = int(numTxt1.get())
    n2 = int(numTxt2.get())
    tmp = resultLbl["text"]
    resultLbl["text"] += f"{n1} * {n2} = {n1 * n2}\n"

def division_Handler(event):
    n1 = int(numTxt1.get())
    n2 = int(numTxt2.get())
    tmp = resultLbl["text"]
    if n2 == 0:
        resultLbl["text"] += "You cannot divide a number by 0."
    else:
        resultLbl["text"] += f"""
        {n1} / {n2} = {n1 / n2:.3f}
        Quotent = {n1 // n2}
        """
        if n1 % n2 == 0:
            resultLbl["text"] += f"Remainder = {n1%n2}"

def addition_Handler(event):
    n1 = int(numTxt1.get())
    n2 = int(numTxt2.get())
    tmp = resultLbl["text"]
    resultLbl["text"] += f"{n1} + {n2} = {n1 + n2}\n"

def subtraction_Handler(event):
    n1 = int(numTxt1.get())
    n2 = int(numTxt2.get())
    tmp = resultLbl["text"]
    resultLbl["text"] += f"{n2} - {n2} = {n1 - n2}\n"

window = tk.Tk(className = "calculator")

number1Frame=tk.Frame()

numLbl1 = tk.Label(text = "Number 1:", master = number1Frame)
numLbl1.pack(side=LEFT)

numTxt1 = tk.Entry(fg="#000000",bg="#FFFFFF", master = number1Frame)
numTxt1.pack(side=LEFT)

number1Frame.pack()

number2Frame=tk.Frame()

numLbl2 = tk.Label(text = "Number 2:", master = number2Frame)
numLbl2.pack(side=LEFT)

numTxt2 = tk.Entry(fg="#000000",bg="#FFFFFF", master = number2Frame)
numTxt2.pack(side=LEFT)

number2Frame.pack()

operatorsFrame = tk.Frame()

multiplacation = tk.Button(text="*", master = operatorsFrame)
multiplacation.bind("<Button-1>", multiplacation_Handler)
multiplacation.pack(side = LEFT)

addition = tk.Button(text="+", master = operatorsFrame)
addition.bind("<Button-2>", addition_Handler)
addition.pack(side = LEFT)

division = tk.Button(text="/", master = operatorsFrame)
division.bind("<Button-3>", division_Handler)
division.pack(side = LEFT)

subtraction = tk.Button(text="-", master = operatorsFrame)
subtraction.bind("<Button-4>", subtraction_Handler)
subtraction.pack(side = LEFT)

operatorsFrame.pack()

resultFrame = tk.Frame()

resultTitleLbl = tk.Label(text = "Result", master = resultFrame)
resultTitleLbl.pack()

resultLbl = tk.Label(master = resultFrame)
resultLbl.pack()

resultFrame.pack()

window.mainloop()
print("end")