import tkinter
from tkinter import *
from tkinter import messagebox
import datetime
import pyautogui
import subprocess

# capture 
def capture():
    x = str(datetime.datetime.now().strftime("%d %b %Y_%H%M00"))
    x += "_Time"
    pyautogui.screenshot().save('Temp\\Capture\\'+ x +'.jpg')

def keylogger():

    ####### fix mean set time to capture detect
    fix = "090000"

    t = str(datetime.datetime.now().strftime("%H")) + str(datetime.datetime.now().strftime("%M")) +  str(datetime.datetime.now().strftime("%S"))
    if t >= fix:
        subprocess.Popen('python Keyst.py', shell=True)

def tasklist():
    subprocess.run("tasklist /fi \"STATUS eq RUNNING\" > Temp\\running.txt", shell=True)
    with open("Temp/running.txt", 'r') as r:
        running = r.read()

    task = "Temp/exe.txt"
    with open(task, 'a') as f:
        tasktime = str(datetime.datetime.now().strftime("Detect Time >> %H : %M : %S\n"))
        f.write(tasktime)
        f.write(running)
        f.close()

def endApp():
    tasklist()
    subprocess.run("rename Temp " + id, shell=True)
    subprocess.run("del \""+id+"\\running.txt\"", shell=True)
    subprocess.run('taskkill /IM python.exe /F', shell=True)

def student(): 
    global id
    id = id_entry.get()
    if id :
        subprocess.run("mkdir Temp\\Capture", shell=True)
        txt = "Create : " + id
        messagebox.showinfo(title="Success!!", message=txt)

        Window = tkinter.Tk()
        Window.title("Window")
        Window.geometry("300x150")

        def clock():
            ####### fix mean set time to capture detect
            fix = "090000"
            hour = str(datetime.datetime.now().strftime("%H"))
            minute = str(datetime.datetime.now().strftime("%M"))
            second = str(datetime.datetime.now().strftime("%S"))
            if hour+minute+second == fix:
                print("detect")
                tasklist()
                capture()
            timer = hour + ":" + minute + ":" + second
            clock_label.config(text=timer)
            clock_label.after(1000, clock)
        clock_label = Label(Window, text="", font=("Raleway", 20))
        clock_label.pack(padx=20, pady=20)
        clock()
        keylogger()
        btn_end = Button(Window, text="Finish Test", font="Raleway", command=endApp)
        btn_end.pack(padx=20, pady=10)
        Window.mainloop()
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
btn_submit = Button(Application, text="Submit" , font="Raleway", command=student)
btn_submit.grid(column = 1, row = 2)
Application.mainloop()
                       