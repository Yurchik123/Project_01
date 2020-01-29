import math
import tkinter as tk
import keyboard

import os
import sys

window = tk.Tk()
window.overrideredirect(1)
window.state('zoomed')
textFont = ("Arial Bold", 15)
window.geometry("200x200")
window.title("Project_08")


def button1Clicked():
    try:

        if editText2.get() == "pi":
            num = math.pi
        elif editText2.get() == "e":
            num = math.e
        if editText1.get() == "pi":
            z = math.pi
        elif editText1.get() == "e":
            z = math.e
        else:
            num = float(editText2.get())
            z = float(editText1.get())
        outp = round(num ** (1 / z), 2)
    except ValueError:
        outp = 0
    textView2.configure(text=outp)


textView1 = tk.Label(window, text="Корень n-ой степени", font=textFont, fg="#000000")
textView1.place(relx=0, rely=0, relwidth=1, relheight=0.25)

editText1 = tk.Entry(window, font=textFont)
editText1.place(relx=0.02, rely=0.25, relwidth=0.28, relheight=0.1)
editText2 = tk.Entry(window, font=textFont)
editText2.place(relx=0.3, rely=0.35, relwidth=0.68, relheight=0.15)

button1 = tk.Button(window, text="Вычислить", font=textFont, command=button1Clicked)
button1.place(relx=0, rely=0.52, relwidth=1, relheight=0.2)

textView2 = tk.Label(window, text="", font=textFont, fg="#000000")
textView2.place(relx=0, rely=0.78, relwidth=1, relheight=0.22)



window.mainloop()
