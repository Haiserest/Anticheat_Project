import pyautogui
import datetime

x = str(datetime.datetime.now().strftime("%d %b %Y_%H%M%S"))
#print(x)
pyautogui.screenshot().save('C:\\Projecttemp\\Temp\\Capture\\'+ x +'.jpg')