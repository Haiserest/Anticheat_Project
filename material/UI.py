import tkinter
from tkinter import *
from tkinter import messagebox
import time

def id():
    id = id_entry.get()
    if id :
        txt = "Create : " + id
        messagebox.showinfo(title="Success!!", message=txt)
    else:
        messagebox.showwarning(title="warning", message="error valid")


Application = tkinter.Tk()
Application.title("Anticheat")
canvas = tkinter.Canvas(Application, width=300, height=150)
canvas.grid(columnspan=4, rowspan=3)

id_label = Label(Application, text = "ID : ", font = "Raleway")
id_label.grid(column = 0, row = 1)

id_entry = Entry(Application, width=30)
id_entry.grid(column = 1, row = 1)

btn = Button(Application, text="Submit" , font="Raleway", command=id)
btn.grid(column = 1, row = 2)

Application.mainloop()


Window = tkinter.Tk()
Window.title("Window")
Window.geometry("300x150")

def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    timer = hour + ":" + minute + ":" + second
    clock_label.config(text=timer)
    clock_label.after(1000, clock)

clock_label = Label(Window, text="", font=("Helvetica", 20))
clock_label.pack(padx=20, pady=20)

clock()

Window.mainloop()