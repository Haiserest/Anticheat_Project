import tkinter
from tkinter import *
import datetime
import pyautogui
import subprocess

#===================function===========================

def time(s):
    min = int(datetime.datetime.now().strftime("%M"))
    if (min %2 == 0) and (s == 0) :
        capture()
    return min

# capture 
def capture():
    x = str(datetime.datetime.now().strftime("%d %b %Y_%H%M00"))
    x += "_Time"
    #print(x)
    pyautogui.screenshot().save('Temp\\Capture\\'+ x +'.jpg')

def cmd():
    subprocess.run("mkdir Temp\\Capture", shell=True)
    subprocess.Popen('python material\\Keylogger.py', shell=True)
    subprocess.run("tasklist /fi \"STATUS eq RUNNING\" > Temp\\running.txt", shell=True)


def endApp():
    subprocess.run('taskkill /IM python.exe /F', shell=True)

#=====================main=============================

if (__name__ == '__main__'):

    cmd()
    check = int(input("Min to capture check : "))
    end = int(input("Min to end : "))
    i = 1
    spam = 0
    while i == 1 :
        min = time(spam)
        if (min %check == 0) and (spam == 0) :
            print(datetime.datetime.now().strftime("%H : %M : %S"))
            # print(min)
            spam = 1
        elif min % end == 0:
            print(datetime.datetime.now().strftime("%H : %M : %S"))
            print ("End")
            i = 0
        elif (min %check != 0):
            spam = 0
    
    endApp()

#=======================UI==============================

