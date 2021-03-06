from tkinter import *
import tkinter as tk
from tkinter import font

def operation_Handler(operator):
    n1 = int(numTxt1.get())
    n2 = int(numTxt2.get())
    tmp = resultLbl["text"]
    res = 0
    if(operator == "+"):
        res = n1 + n2
    elif(operator == "-"):
        res = n1 - n2
    elif(operator == "*"):
        res = n1 * n2
    resultLbl["text"] += f"{n1} {operator} {n2} = {res}\n"

def addition_Handler(event):
    operation_Handler("+")  

def subtraction_Handler(event):
    operation_Handler("-") 

def multiplacation_Handler(event):
    operation_Handler("*") 

def division_Handler(event):
    n1 = int(numTxt1.get())
    n2 = int(numTxt2.get())
    tmp = resultLbl["text"]
    if n2 == 0:
        resultLbl["text"] += "You cannot divide a number by 0.\n"
    else:
        resultLbl["text"] += f"""
        {n1} / {n2} = {n1 / n2:.3f}
        Quotent = {n1 // n2}
        """
        if n1 % n2 == 0:
            resultLbl["text"] += f"Remainder = {n1%n2}\n"

def create_button(caption,handler):
    btn = tk.Button(text=caption, master = operatorsFrame, fg = "#FF80FF", font = "Verdana 36")
    btn.bind("<Button-1>", handler)
    btn.pack(side = LEFT,padx=5, pady=10, ipadx=20, ipady=10)

window = tk.Tk(className = "calculator")

number1Frame=tk.Frame()

numLbl1 = tk.Label(text = "Number 1:", master = number1Frame, fg = "#FF80FF", font = "Verdana 36")
numLbl1.pack(side=LEFT,padx=5, pady=10, ipadx=20, ipady=10)

numTxt1 = tk.Entry(bg="#FFFFFF", master = number1Frame, fg = "#FF80FF", font = "Verdana 36")
numTxt1.pack(side=LEFT,padx=5, pady=10, ipadx=20, ipady=10)

number1Frame.pack()

number2Frame=tk.Frame()

numLbl2 = tk.Label(text = "Number 2:", master = number2Frame, fg = "#FF80FF", font = "Verdana 36")
numLbl2.pack(side=LEFT,padx=5, pady=10, ipadx=20, ipady=10)

numTxt2 = tk.Entry(bg="#FFFFFF", master = number2Frame, fg = "#FF80FF", font = "Verdana 36")
numTxt2.pack(side=LEFT,padx=5, pady=10, ipadx=20, ipady=10)

number2Frame.pack()

operatorsFrame = tk.Frame()

create_button("*", multiplacation_Handler)
create_button("/", division_Handler)
create_button("+", addition_Handler)
create_button("-", subtraction_Handler)

operatorsFrame.pack()

resultFrame = tk.Frame()

resultTitleLbl = tk.Label(text = "Result", master = resultFrame, font = "Verdana 36")
resultTitleLbl.pack()

resultLbl = tk.Label(master = resultFrame)
resultLbl.pack()

resultFrame.pack()

window.mainloop()
print("end")