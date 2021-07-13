import subprocess
import pyautogui
import datetime

# capture 
def capture():
    x = str(datetime.datetime.now().strftime("%d %b %Y_%H%M00"))
    x += "_Time"
    #print(x)
    pyautogui.screenshot().save('Temp\\Capture\\'+ x +'.jpg')

def taskkill():
    subprocess.run('taskkill /IM python.exe /F', shell=True)

# def hide():


if ( __name__ == '__main__' ):
    
    while 1:
        x = input("Enter Function : ")
        if x == '1':
            capture()
        else:
            taskkill()