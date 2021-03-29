import pyautogui
import datetime

x = str(datetime.datetime.now().strftime("%d-%b-%Y %H-%M-%S"))
print(x)
pyautogui.screenshot().save('C:/Users/asus/Documents/Project file/Temp/attemp1/'+ x +'.jpg')