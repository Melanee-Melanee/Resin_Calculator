
from functools import partial 
from tkinter import *
import math

import tkinter as tk

root = Tk()

root.geometry('500x600')
root.title('Resin Calculator')

background_image = tk.PhotoImage(file="back5.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)


def resincal(p1, p2):#heigthh,lengthh,widthh):
    print(p1, p2)
    heigthh = int(heigthEntry.get())
    lengthh = int(lengthValue.get())
    widthh = int(widthValue.get())

    result = heigthh*lengthh*widthh 

    Label(text =  "your resin is {} gr".format(result)).grid(row=8, column=1)
    return result
    
Label(text = 'Heigth').grid(row=1, column=0, padx=90)
Label(text='Length').grid(row=2, column=0)
Label(text='Width').grid(row=3, column=0)


heigthValue = StringVar()
lengthValue = StringVar()
widthValue = StringVar()
heigthEntry = Entry(root, textvariable=heigthValue)
lengthEntry = Entry(root, textvariable=lengthValue)
widthEntry = Entry(root, textvariable=widthValue)
heigthEntry.grid(row=1, column=1, pady=5)
lengthEntry.grid(row=2, column=1, pady= 10)
widthEntry.grid(row=3, column=1, pady=10)


Button(text='Calculate Resin', command=partial(resincal, 10, 30)).grid(row=5, column= 1, pady=10)

root.mainloop()
