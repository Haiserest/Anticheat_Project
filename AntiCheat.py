import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
import datetime
import pyautogui
import subprocess
import wmi
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

#=====================key==============================

#===================function===========================

                                                                    # detect find monitor used
def monitor():
    obj = wmi.WMI().Win32_PnPEntity(ConfigManagerErrorCode=0)

    displays = [x for x in obj if 'DISPLAY' in str(x)]
    i = 0
    for item in displays:
        #print(item)
        i +=1
    i-=1

    display = "Found Monitor : [" + str(i) + "]\n"
    print(display)  
                                                                    # write monitor used to exe.txt
    task = 'Temp/exe.txt'
    with open(task, 'a') as f:
        f.write(display+'\n')

                                                                    # screenshot (primary monitor) 
def capture():
    x = str(datetime.datetime.now().strftime('%d %b %Y_%H%M%S'))
    pyautogui.screenshot().save('Temp\\Capture\\'+ x +'.jpg')

                                                                    # call function interrupt
def Call_function():
                                                                    # keyboard interrupt
    subprocess.Popen('python material\\Keylogger.py', shell=True)
                                                                    # mic interrupt
    #more interrupt
    #subprocess.Popen('python material\\mic.py', shell=True)
                                                                    # scapy scan and find adapter wireless
    subprocess.Popen('python material\\getadapter.py', shell=True)
    subprocess.Popen('python material\\networkscan.py', shell=True)

                                                                    # process monitor detect keyword 
def tasklist():
    subprocess.run('tasklist /fi \"STATUS eq RUNNING\" > Temp\\running.txt', shell=True)

    with open('Temp/running.txt', 'r') as r:
        x = r.read()
        detect = ''
                                                                    # filter keyword application voice chat
    if (x.find('TeamSpeak') >= 0 ) or (x.find('Skype') >=0 ) or (x.find('Discord') >= 0):
        if (x.find('TeamSpeak') >= 0 ):
            detect += 'TeamSpeaker\n'
        if (x.find('Skype') >=0 ):
            detect += 'Skype\n'
        if (x.find('Discord') >= 0):
            detect += 'Discord\n'
        else:
            print("pass")
                                                                    # get process detected to exe.txt
        task = 'Temp/exe.txt'
        with open(task, 'a') as f:
            tasktime = str(datetime.datetime.now().strftime('Time >> %H : %M : %S\n'))
            f.write(tasktime)
            f.write(detect)
            f.close()

                                                                    # end Application and rename file keep source
def endApp():
    tasklist()
    subprocess.run('del "Temp\\running.txt"', shell=True)
    subprocess.run('rename Temp ' + id, shell=True)
    subprocess.run('taskkill /IM python.exe /F', shell=True)

    
def sumbit():
    global id

    id = id_std.get()
    entry_id.delete(0,END)
    return frame_clock()

def frame_id():
    global id_std,frametest,entry_id

    frametest = Frame(Application, height=150, width=300)
    frametest.place(x=0, y=0)
    
    label_id = Label(frametest, text="ID : ")
    label_id.place(x=30, y=40)

    id_std = StringVar()

    entry_id = Entry(frametest, width=30, textvariable= id_std)
    entry_id.place(x=60, y=43)

    btn_submit = Button(frametest, text="Submit", command=sumbit)
    btn_submit.place(x=120, y=100)

def frame_clock():
    global frameclock

    if id:
        subprocess.run('mkdir Temp\\Capture', shell=True)
        txt = 'Create : ' + id
        messagebox.showinfo(title='Success!!', message=txt)
        frameclock = Frame(Application, height=150, width=300)
        frameclock.place(x=0, y=0)
        try :
            framename = Frame(frameclock,height=40,width=300,background="#a9c8dd")
            framename.place(x=0,y=0)

            std_label = Label(framename, text="Student ID: "+id , font=BOLD, background="#a9c8dd")
            std_label.place(x=10,y=10)

        except:
            pass

        def clock():

            fix = "234600"

            hour = str(datetime.datetime.now().strftime("%H"))
            minute = str(datetime.datetime.now().strftime("%M"))
            second = str(datetime.datetime.now().strftime("%S"))

            if hour+minute+second == fix:
                monitor()
                tasklist()
                Call_function()

            timer = hour + ":" + minute + ":" + second
            clock_label.config(text=timer)
            clock_label.after(1000, clock)

        clock_label = Label(frameclock, text="", font=("Raleway", 20))
        clock_label.place(x=90, y=50)

        clock()

        btn_back = Button(frameclock, text="Finish", command=endApp)
        btn_back.place(x=120, y=100)

    else:
        messagebox.showwarning(title="warning", message="error valid")


Application = tkinter.Tk()
Application.title("Anticheat")
Application.geometry('300x150')
Application.iconbitmap('material/icon2.ico')

frame_id()

Application.mainloop()