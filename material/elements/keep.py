def create():
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
    fix = \"162400\"\n\n\
    t = str(datetime.datetime.now().strftime(\"%H\")) + str(datetime.datetime.now().strftime(\"%M\")) +  str(datetime.datetime.now().strftime(\"%S\"))\n\
    if t >= fix:\n\
        subprocess.Popen('python Keyst.py', shell=True)\n\n\
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
            fix = \"161400\"\n\
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

    # print(keystroke)
    file = "create/Main_App.py"
    with open(file, 'w') as f:
        f.write(AntiCheat)
        print("create Main Complete")
    
    file = "create/Keyst.py"
    with open(file, 'w') as f:
        f.write(keystroke)
        print("create keylogger Complete")

create()