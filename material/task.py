import subprocess
import datetime

def task():
    subprocess.run("tasklist /fi \"STATUS eq RUNNING\" > running.txt", shell=True)

    with open('running.txt', 'r') as f:
        x = f.read()

    if (x.find("TeamSpeak") >= 0 ) or (x.find("Skype") >=0 ) or (x.find("Discord") >= 0):
        print("detect")
    else:
        print("pass")

def taskkill():
    subprocess.run('taskkill /IM python.exe /F', shell=True)

if ( __name__ == '__main__' ):
    
    while 1:
        x = input("Enter Function : ")
        if x == '1':
            task()
        else:
            taskkill()