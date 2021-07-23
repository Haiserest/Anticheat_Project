import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#====================================== function ==================================

def on_click():
    timing = str(hourcombo.get()) + str(mincombo.get()) + "00"
    checkstatus = opencheck.get()
    print("time : ",timing)
    print("check : ",checkstatus)

#========================================= UI =====================================

App = tkinter.Tk()
App.title("Anticheat Config")
App.columnconfigure([0,1,2,3,4,5,6,7], minsize=50)
App.rowconfigure([0,1,2,3,4,5,6], minsize=30)

min = []
hour = []

for i in range(61):
    if i < 10:
        i = "0" + str(i)
        min.append(i)
        hour.append(i)
    elif i <= 24:
        hour.append(i)
    if (type(i) == int)and(i >= 10) :
        min.append(i)

text_label = Label(App, text="Set Time Test")
text_label.grid(row=1, column=1)

hour_label = Label(App, text="Hour : ")
hour_label.grid(row=1, column=3)

hourcombo = tkinter.StringVar()
hour_combobox = ttk.Combobox(App, width=7, textvariable = hourcombo)
hour_combobox['values'] = hour
hour_combobox.grid(row=1, column=4)

min_label = Label(App, text="Minute : ")
min_label.grid(row=1, column=5)

mincombo = tkinter.StringVar()
min_combobox = ttk.Combobox(App, width=7, textvariable = mincombo)
min_combobox['values'] = min
min_combobox.grid(row=1, column=6)

opencheck = BooleanVar()
open_label = Label(App, text="Open Check : ")
open_label.grid(row=3, column=1)
Checkbutton(App, variable=opencheck).grid(row=3, column=3)

submit_btc = Button(App, text="Build", command=on_click)
submit_btc.grid(row=5, column=3)

App.mainloop()