import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import subprocess

#====================================== function ==================================

def createApp(subject, timing):
    AntiCheat = "\
import tkinter\n\
from tkinter import *\n\
from tkinter import messagebox\n\
import datetime\n\
import pyautogui\n\
import subprocess\n\n\
# capture \n\
def capture():\n\
    x = str(datetime.datetime.now().strftime(\"%d %b %Y_%H%M00\"))\n\
    x += \"_Time\"\n\
    pyautogui.screenshot().save('Temp\\\Capture\\\\'+ x +'.jpg')\n\n\
def keylogger():\n\n\
    ####### fix mean set time to capture detect\n\
    fix = \""+timing+"\"\n\n\
    t = str(datetime.datetime.now().strftime(\"%H\")) + str(datetime.datetime.now().strftime(\"%M\")) +  str(datetime.datetime.now().strftime(\"%S\"))\n\
    if t >= fix:\n\
        subprocess.Popen(\"python " + subject + "\\Keyst.py\", shell=True)\n\n\
def tasklist():\n\
    subprocess.run(\"tasklist /fi \\\"STATUS eq RUNNING\\\" > Temp\\\\running.txt\", shell=True)\n\
    with open(\"Temp/running.txt\", 'r') as r:\n\
        running = r.read()\n\n\
    task = \"Temp/exe.txt\"\n\
    with open(task, 'a') as f:\n\
        tasktime = str(datetime.datetime.now().strftime(\"Detect Time >> %H : %M : %S\\n\"))\n\
        f.write(tasktime)\n\
        f.write(running)\n\
        f.close()\n\n\
def endApp():\n\
    tasklist()\n\
    subprocess.run(\"rename Temp \" + id, shell=True)\n\
    subprocess.run(\"del \\\"\"+id+\"\\\\running.txt\\\"\", shell=True)\n\
    subprocess.run('taskkill /IM python.exe /F', shell=True)\n\n\
def student(): \n\
    global id\n\
    id = id_entry.get()\n\
    if id :\n\
        subprocess.run(\"mkdir Temp\\\\Capture\", shell=True)\n\
        txt = \"Create : \" + id\n\
        messagebox.showinfo(title=\"Success!!\", message=txt)\n\n\
        Window = tkinter.Tk()\n\
        Window.title(\"Window\")\n\
        Window.geometry(\"300x150\")\n\n\
        def clock():\n\
            ####### fix mean set time to capture detect\n\
            fix = \""+timing+"\"\n\
            hour = str(datetime.datetime.now().strftime(\"%H\"))\n\
            minute = str(datetime.datetime.now().strftime(\"%M\"))\n\
            second = str(datetime.datetime.now().strftime(\"%S\"))\n\
            if hour+minute+second == fix:\n\
                print(\"detect\")\n\
                tasklist()\n\
                capture()\n\
            timer = hour + \":\" + minute + \":\" + second\n\
            clock_label.config(text=timer)\n\
            clock_label.after(1000, clock)\n\
        clock_label = Label(Window, text=\"\", font=(\"Raleway\", 20))\n\
        clock_label.pack(padx=20, pady=20)\n\
        clock()\n\
        keylogger()\n\
        btn_end = Button(Window, text=\"Finish Test\", font=\"Raleway\", command=endApp)\n\
        btn_end.pack(padx=20, pady=10)\n\
        Window.mainloop()\n\
    else:\n\
        messagebox.showwarning(title=\"warning\", message=\"error valid\") \n\n\
Application = tkinter.Tk()\n\
Application.title(\"Anticheat\")\n\
canvas = tkinter.Canvas(Application, width=300, height=150)\n\
canvas.grid(columnspan=4, rowspan=3)\n\
id_label = Label(Application, text = \"ID : \", font = \"Raleway\")\n\
id_label.grid(column = 0, row = 1)\n\
id_entry = Entry(Application, width=30)\n\
id_entry.grid(column = 1, row = 1)\n\
btn_submit = Button(Application, text=\"Submit\" , font=\"Raleway\", command=student)\n\
btn_submit.grid(column = 1, row = 2)\n\
Application.mainloop()\n\
                       "
    keystroke = "\
from pynput.keyboard import Listener\n\
import pyautogui\n\
import datetime\n\n\
# keyloger\n\
def keystroke(key):\n\
    key = str(key).replace(\"'\",\"\")\n\
    if key == \"\\\\x03\":\n\
        key = \"\\nshortcut Copy\\n\"\n\
        capturekey(\"_Copy\")\n\
    if key == \"\\\\x16\":\n\
        key = \"\\nshortcut Paste\\n\"\n\
        capturekey(\"_Paste\")\n\
    if key == \"Key.print_screen \":\n\
        key = \"\\nprint screen\\n\"\n\
        capturekey(\"_capture\")\n\
    if key == (\"Key.ctrl_l\") or key == (\"Key.right\") or key == (\"Key.left\") or key == (\"Key.up\") or key == (\"Key.down\") or key == (\"Key.backspace\") or key == (\"Key.space\") or key == (\"Key.enter\") or key == (\"\\\\x13\") or key == (\"\\\\x01\"):\n\
        key = ''\n\
    else:\n\
        key += ' '\n\n\
    with open(\"Temp\\\\Keylogger.txt\", 'a') as f:\n\
        f.write(key)\n\n\
# capture\n\
def capturekey(k):\n\
    x = str(datetime.datetime.now().strftime(\"%d %b %Y_%H%M%S\"))\n\
    x += k\n\
    pyautogui.screenshot().save('Temp\\\\Capture\\\\'+ x +'.jpg')\n\n\
with Listener(on_press=keystroke) as l:\n\
    l.join()\n\
                    "
    subprocess.run("mkdir "+subject, shell=True)

    # print(keystroke)
    file = subject+"/Main_App.py"
    with open(file, 'w') as f:
        f.write(AntiCheat)
        print("create Main Complete")
    
    file = subject+"/Keyst.py"
    with open(file, 'w') as f:
        f.write(keystroke)
        print("create keylogger Complete")

def on_click():
    timing = str(hourcombo.get()) + str(mincombo.get()) + "00"
    checkstatus = opencheck.get()
    subject = subject_entry.get()
    print("Subject : ",subject)
    print("time : ",timing)
    print("check : ",checkstatus)

    if checkstatus:
        timecheck = checkcombo.get()
        print("Time Check : ",timecheck)
    
    createApp(subject, timing)

#========================================= UI =====================================

App = tkinter.Tk()
App.title("Anticheat Config")
App.columnconfigure([0,1,2,3,4,5,6,7], minsize=50)
App.rowconfigure([0,1,2,3,4,5,6,7,8], minsize=30)

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

subject_label = Label(App, text="Subject : ", font="Raleway")

subject_entry = Entry(App, width=30)

subject_label.grid(row=1, column=1)
subject_entry.grid(row=1, column=3)


text_label = Label(App, text="Set Time Test", font="Raleway")

hour_label = Label(App, text=">> ", font="Raleway")
hourcombo = tkinter.StringVar()
hour_combobox = ttk.Combobox(App, width=7, textvariable = hourcombo)
hour_combobox['values'] = hour

min_label = Label(App, text=" : ", font="Raleway")
mincombo = tkinter.StringVar()
min_combobox = ttk.Combobox(App, width=7, textvariable = mincombo)
min_combobox['values'] = min

text_label.grid(row=3, column=1)
hour_label.grid(row=3, column=3)
hour_combobox.grid(row=3, column=4)
hour_combobox.current(0)
min_label.grid(row=3, column=5)
min_combobox.grid(row=3, column=6)
min_combobox.current(0)


opencheck = BooleanVar()
open_label = Label(App, text="Open Check : ", font="Raleway")

Checkbutton(App, variable=opencheck).grid(row=5, column=3)
check_label = Label(App, text="Time check : ", font="Raleway").grid(row=5, column=4)
checkcombo = tkinter.StringVar()
check_combobox = ttk.Combobox(App, width=7, textvariable= checkcombo)
check_combobox['values'] = (5,10,15,20,30,60)

a1 = Label(App, text="Minute", font="Raleway").grid(row=5, column=6)

check_combobox.grid(row=5, column=5)
check_combobox.current(0)
open_label.grid(row=5, column=1)

submit_btc = Button(App, text="Build", font="Raleway",  command=on_click)
submit_btc.grid(row=7, column=3)

App.mainloop()