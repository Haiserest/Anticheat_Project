import tkinter
from tkinter import *
from tkinter import messagebox
import datetime
import pyautogui
import subprocess
import wmi
import os
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

#=====================key==============================

#===================function===========================

def monitor():
    obj = wmi.WMI().Win32_PnPEntity(ConfigManagerErrorCode=0)

    displays = [x for x in obj if 'DISPLAY' in str(x)]
    i = 0
    for item in displays:
        #print(item)
        i +=1
    i-=1

    if i == 1:
        display = "single Monitor\n"
        print(display)      
    elif i > 1:
        display = "Multi Monitor : [" + str(i) + "]\n"
        print(display)  
    
    task = "Temp/exe.txt"
    with open(task, 'a') as f:
        f.write(display)

# capture 
def capture():
    x = str(datetime.datetime.now().strftime("%d %b %Y_%H%M%S"))
    pyautogui.screenshot().save('Temp\\Capture\\'+ x +'.jpg')

def keylogger():
    subprocess.Popen('python material\\Keylogger.py', shell=True)
    subprocess.Popen('python material\\mic.py', shell=True)

def tasklist():
    subprocess.run("tasklist /fi \"STATUS eq RUNNING\" > Temp\\running.txt", shell=True)

    with open("Temp/running.txt", 'r') as r:
        x = r.read()
        detect = ""

    if (x.find("TeamSpeak") >= 0 ) or (x.find("Skype") >=0 ) or (x.find("Discord") >= 0):
        if (x.find("TeamSpeak") >= 0 ):

            detect += "TeamSpeaker\n"
        if (x.find("Skype") >=0 ):

            detect += "Skype\n"
        if (x.find("Discord") >= 0):

            detect += "Discord\n"
        else:
            print("pass")

        task = "Temp/exe.txt"
        with open(task, 'a') as f:
            tasktime = str(datetime.datetime.now().strftime("Time >> %H : %M : %S\n"))
            f.write(tasktime)
            f.write(detect)
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
            fix = "200200"
            timeout = "165330"

            hour = str(datetime.datetime.now().strftime("%H"))
            minute = str(datetime.datetime.now().strftime("%M"))
            second = str(datetime.datetime.now().strftime("%S"))

            if hour+minute+second == fix:
                print("Start App")
                monitor()
                tasklist()
                #capture()
                keylogger()
            
            # elif hour+minute+second == timeout:
            #     print("timeout")
            #     messagebox.showwarning(title="Time Out", message="Time Out")
            #     endApp()


            timer = hour + ":" + minute + ":" + second
            clock_label.config(text=timer)
            clock_label.after(1000, clock)


        clock_label = Label(Window, text="", font=("Raleway", 20))
        clock_label.pack(pady=20)

        clock()
        
        btn_end = Button(Window, text="Finish Test", font="Raleway", command=endApp)
        btn_end.pack(pady=10)

        Window.mainloop()
    else:
        messagebox.showwarning(title="warning", message="error valid")
    

#========================== create folder =======================================
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
