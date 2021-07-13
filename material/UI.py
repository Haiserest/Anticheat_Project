import tkinter
from tkinter import *

def hello():
    id = id_entry.get()
    print("id : " + id)

Application = tkinter.Tk()
Application.title("Anticheat")
canvas = tkinter.Canvas(Application, width=300, height=150)
canvas.grid(columnspan=4, rowspan=3)

id_label = Label(Application, text = "ID : ", font = "Raleway")
id_label.grid(column = 0, row = 1)

id_entry = Entry(Application, width=30)
id_entry.grid(column = 1, row = 1)

btn = Button(Application, text="Submit" , font="Raleway", command=hello)
btn.grid(column = 1, row = 2)

Application.mainloop()