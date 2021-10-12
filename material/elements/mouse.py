from pynput.mouse import Listener
import time

def on_move(x, y):
    # time.sleep(10)
    print("moved ({0}, {1})".format(x, y))

def on_click(x, y, button, presses):
    # time.sleep(10)
    if presses:
        print("click ({0}, {1}) [{2}]".format(x, y, button))
    
    if button == "Button.right":
        print("Click right")
        
        # with open('click.txt', 'a') as f:
        #     f.write(x)
    if button == "Button.left":
        print("Click left")

with Listener(on_move=on_move, on_click=on_click) as listener:
    
    listener.join()