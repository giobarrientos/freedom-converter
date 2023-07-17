import tkinter as tk
from tkinter import *
from tkinter import ttk
import sv_ttk
root = tk.Tk()
root.geometry("500x500")
root.title("Freedom Converter")
sv_ttk.set_theme("dark")

label = ttk.Label(root, text="Freedom converter!")
label.pack(pady=10)

impLabel = ttk.Label(root, text="U.S. Measurement:")
impLabel.pack(pady=10)


imperialEntry = ttk.Entry(root)
imperialEntry.pack()
var = tk.StringVar()

def pressed():
    metInput = imperialEntry.get()
    metInput = float(metInput)
    answer = float
    metMes = str
    unit = clicked.get()
    fullAnswer = str
    match unit:
        case "Inches":
            answer = metInput *2.5
            metMes = "cm"
        case "Feet":
            answer = metInput *30.48
            if answer > 100:
                answer = answer/10
                metMes = "meters"
            else:
                metMes = "cm"
        case "Ounces":
            answer = metInput *28.34
            metMes = "g"
        case "Pounds":
            answer = metInput *0.453
            metMes = "kg"
        case "Gallons":
            answer = metInput *3.78
            metMes = "litres"
        case "Yards":
            answer = metInput *0.9144
            metMes = "meters"
        case "Cups":
            answer = metInput *0.236
            metMes = "litres"
        case "Fl Oz":
            answer = metInput *29.57
            metMes = "ml"
        case _:
            answer = str(answer)
            answer = "error, "
            metMes = "please enter a valid number"
    fullAnswer = (answer,metMes)
    var.set(fullAnswer)

        
    


option = [
    "Inches",
    "Feet",
    "Yards",
    "Ounces",
    "Pounds",
    "Gallons",
    "Cups",
    "Fl Oz"
]

clicked = StringVar()
clicked.set(option[0])

drop = ttk.OptionMenu(root, clicked, *option)
drop.pack(pady=20)

convert = ttk.Button(root, text="Convert!", command=pressed)
convert.pack(pady=30)

metLabel = ttk.Label(root, text="Metric Measurement:")
metLabel.pack(pady=30)

ansLabel = ttk.Label(root, textvariable = var).pack()

root.mainloop()