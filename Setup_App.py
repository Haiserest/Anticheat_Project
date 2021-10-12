import tkinter
from tkinter import *
from tkinter import filedialog,messagebox
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image, ImageTk
import subprocess
import os
import zipfile
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Hash import SHA512
from Crypto import Random
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

#=====================key==============================

def generateAESkey(subject):
    # key AES 256 bits
    key = get_random_bytes(32)

    # save Create AES key
    fileAES = subject+"/File_Generate/AESkey"
    os.makedirs(os.path.dirname(fileAES), exist_ok=True)
    with open(fileAES, 'wb') as f:
        f.write(key)
        f.close()

    # save key for std

    fileAES = subject + '/' + subject + "/GKey/AESkey"
    os.makedirs(os.path.dirname(fileAES), exist_ok=True)
    with open(fileAES, 'wb') as f:
        f.write(key)
        f.close()
        

def generateRSAkey(subject):
    # generate key 2048 bits
    key = RSA.generate(2048)

    Private_Key = key.exportKey('PEM')
    Public_Key = key.publickey().exportKey('PEM')

    # save key Create

    Private_key_file = subject+"/File_Generate/Private_Key.pem"
    os.makedirs(os.path.dirname(Private_key_file), exist_ok=True)
    with open(Private_key_file, 'wb') as f:
        f.write(Private_Key)
        f.close()

    Public_key_file = subject+"/File_Generate/Public_Key.pem"
    os.makedirs(os.path.dirname(Public_key_file), exist_ok=True)
    with open(Public_key_file, 'wb') as f:
        f.write(Public_Key)
        f.close()

    # save key for std

    Public_key_file = subject + '/' + subject +"/GKey/Public_Key.pem"
    os.makedirs(os.path.dirname(Public_key_file), exist_ok=True)
    with open(Public_key_file, 'wb') as f:
        f.write(Public_Key)
        f.close()

#====================================== function ==================================

def createApp(subject, time_start, time_stop):
#     AntiCheat = "\
# import tkinter\n\
# from tkinter import *\n\
# from tkinter import messagebox\n\
# import datetime\n\
# import pyautogui\n\
# import subprocess\n\
# import wmi\n\n\
# def monitor():\n\
#     obj = wmi.WMI().Win32_PnPEntity(ConfigManagerErrorCode=0)\n\
#     displays = [x for x in obj if 'DISPLAY' in str(x)]\n\
#     i = 0\n\
#     for item in displays:\n\
#         #print(item)\n\
#         i +=1\n\
#     i-=1\n\
#     if i == 1:\n\
#         display = 'single Monitor\\n'\n\
#     elif i > 1:\n\
#         display = 'Multi Monitor : [' + str(i) + ']\\n'\n\
#     task = 'Temp/exe.txt'\n\
#     with open(task, 'a') as f:\n\
#         f.write(display)\n\
# # capture \n\
# def capture():\n\
#     x = str(datetime.datetime.now().strftime(\"%d %b %Y_%H%M%S\"))\n\
#     pyautogui.screenshot().save('Temp\\\Capture\\\\'+ x +'.jpg')\n\n\
# def keylogger():\n\
#     subprocess.Popen(\"python " + subject + "\\Keyst.py\", shell=True)\n\
#     subprocess.Popen('python " + subject + "\\mc.py', shell=True)\n\
# def tasklist():\n\
#     subprocess.run(\"tasklist /fi \\\"STATUS eq RUNNING\\\" > Temp\\\\running.txt\", shell=True)\n\
#     with open(\"Temp/running.txt\", 'r') as r:\n\
#         x = r.read()\n\
#         detect = ''\n\
#     if (x.find('TeamSpeak') >= 0 ) or (x.find('Skype') >=0 ) or (x.find('Discord') >= 0):\n\
#         if (x.find('TeamSpeak') >= 0 ):\n\
#             detect += 'TeamSpeaker\\n'\n\
#         if (x.find('Skype') >=0 ):\n\
#             detect += 'Skype\\n'\n\
#         if (x.find('Discord') >= 0):\n\
#             detect += 'Discord\\n'\n\
#         else:\n\
#             print('pass')\n\
#         task = 'Temp/exe.txt'\n\
#         with open(task, 'a') as f:\n\
#             tasktime = str(datetime.datetime.now().strftime('Time >> %H : %M : %S\\n'))\n\
#             f.write(tasktime)\n\
#             f.write(detect)\n\
#             f.close()\n\n\
# def endApp():\n\
#     tasklist()\n\
#     subprocess.run(\"rename Temp \" + id, shell=True)\n\
#     subprocess.run(\"del \\\"\"+id+\"\\\\running.txt\\\"\", shell=True)\n\
#     subprocess.run('taskkill /IM python.exe /F', shell=True)\n\n\
# def student(): \n\
#     global id\n\
#     id = id_entry.get()\n\
#     if id :\n\
#         subprocess.run(\"mkdir Temp\\\\Capture\", shell=True)\n\
#         txt = \"Create : \" + id\n\
#         messagebox.showinfo(title=\"Success!!\", message=txt)\n\n\
#         Window = tkinter.Tk()\n\
#         Window.title(\"Window\")\n\
#         Window.geometry(\"300x150\")\n\n\
#         def clock():\n\
#             ####### set time to capture detect\n\
#             timestart_test = \""+time_start+"\"\n\
#             timeout_test = \""+time_stop+"\"\n\
#             hour = str(datetime.datetime.now().strftime(\"%H\"))\n\
#             minute = str(datetime.datetime.now().strftime(\"%M\"))\n\
#             second = str(datetime.datetime.now().strftime(\"%S\"))\n\
#             if hour+minute+second == timestart_test:\n\
#                 print(\"Start App\")\n\
#                 monitor()\n\
#                 tasklist()\n\
#                 capture()\n\
#                 keylogger()\n\
#             elif hour+minute+second == timeout_test:\n\
#                 print(\"Timeout\")\n\
#                 messagebox.showwarning(title=\"Time Out\", message=\"Time Out!!\")\n\
#                 endApp()\n\n\
#             timer = hour + \":\" + minute + \":\" + second\n\
#             clock_label.config(text=timer)\n\
#             clock_label.after(1000, clock)\n\
#         clock_label = Label(Window, text=\"\", font=(\"Raleway\", 20))\n\
#         clock_label.pack(padx=20, pady=20)\n\
#         clock()\n\
#         btn_end = Button(Window, text=\"Finish Test\", font=\"Raleway\", command=endApp)\n\
#         btn_end.pack(padx=20, pady=10)\n\
#         Window.mainloop()\n\
#     else:\n\
#         messagebox.showwarning(title=\"warning\", message=\"error valid\") \n\n\
# Application = tkinter.Tk()\n\
# Application.title(\"Anticheat\")\n\
# canvas = tkinter.Canvas(Application, width=300, height=150)\n\
# canvas.grid(columnspan=4, rowspan=3)\n\
# id_label = Label(Application, text = \"ID : \", font = \"Raleway\")\n\
# id_label.grid(column = 0, row = 1)\n\
# id_entry = Entry(Application, width=30)\n\
# id_entry.grid(column = 1, row = 1)\n\
# btn_submit = Button(Application, text=\"Submit\" , font=\"Raleway\", command=student)\n\
# btn_submit.grid(column = 1, row = 2)\n\
# Application.mainloop()\n\
#                        "
#     keystroke = "\
# from pynput.keyboard import Listener\n\
# import pyautogui\n\
# import datetime\n\n\
# # keyloger\n\
# def keystroke(key):\n\
#     key = str(key).replace(\"'\",\"\")\n\
#     if key == \"\\\\x03\":\n\
#         key = \"\\nshortcut Copy\\n\"\n\
#         capturekey(\"_Copy\")\n\
#     if key == \"\\\\x16\":\n\
#         key = \"\\nshortcut Paste\\n\"\n\
#         capturekey(\"_Paste\")\n\
#     if key == \"\\\\x06\":\n\
#         key = \"\\nshortcut search\\n\"\n\
#         capturekey(\"_Search\")\n\
#     if key == \"Key.print_screen \":\n\
#         key = \"\\nprint screen\\n\"\n\
#         capturekey(\"_capture\")\n\
#     if key == (\"Key.ctrl_l\") or key == (\"Key.right\") or key == (\"Key.left\") or key == (\"Key.up\") or key == (\"Key.down\") or key == (\"Key.backspace\") or key == (\"Key.space\") or key == (\"Key.enter\") or key == (\"\\\\x13\") or key == (\"\\\\x01\"):\n\
#         key = ''\n\
#     else:\n\
#         key += ' '\n\n\
#     with open(\"Temp\\\\Keylogger.txt\", 'a') as f:\n\
#         f.write(key)\n\n\
# # capture\n\
# def capturekey(k):\n\
#     x = str(datetime.datetime.now().strftime(\"%d %b %Y_%H%M%S\"))\n\
#     x += k\n\
#     pyautogui.screenshot().save('Temp\\\\Capture\\\\'+ x +'.jpg')\n\n\
# with Listener(on_press=keystroke) as l:\n\
#     l.join()\n\
#                     "
    
#     subprocess.run("mkdir "+subject, shell=True)

#     # print(keystroke)
#     file = subject+"/Main_App.py"
#     with open(file, 'w') as f:
#         f.write(AntiCheat)
#         print("create Main Complete")
    
#     file = subject+"/Keyst.py"
#     with open(file, 'w') as f:
#         f.write(keystroke)
#         print("create keylogger Complete")
    
    generateAESkey(subject)
    generateRSAkey(subject)

    messagebox.showinfo(title="Create Complete", message="Create : "+subject)

def more_APP():

    global keywords
    keywords = ['DISCORD','SKYPE','TEAMSPEAKER']

    ck = check.get()
    key = keyword_entry.get()

    if ck:
        k = key.split(',')
        for count in range(len(k)):
            keywords.append(k[count].upper())
    else:
        pass
    print(keywords)

def on_click():

    subject = subject_entry.get()
    timingstart = str(hour_startbox.get()) + str(min_startbox.get()) + "00"
    timingstop = str(hour_stopbox.get()) + str(min_stopbox.get()) + "00"
    print("Subject : ",subject)
    print("time start : ",timingstart)
    print("time out : ",timingstop)
    more_APP()

    print("-------------------------------------------")
    
    if subject :
        if int(timingstart) < int(timingstop):
            createApp(subject, timingstart, timingstop)
        else : 
            messagebox.showwarning(title="Create Error", message="Time Incorrect")
    else :
        messagebox.showwarning(title="Create Error", message="Subject Incorrect")

def set_path(entry_field, pathinput):

    global filter_path, suspect_path, key_path

    if pathinput == 'suspect':
        path = filedialog.askopenfilename(initialdir='C:')
        entry_field.delete(0, tkinter.END)
        entry_field.insert(0, path)
        
        suspect_path = path
        print("suspect path : " + suspect_path)

    if pathinput == 'filter':
        path = filedialog.askdirectory(initialdir='C:')
        entry_field.delete(0, tkinter.END)
        entry_field.insert(0, path)
        
        filter_path = path
        print("filter path : " + filter_path)
        
    if pathinput == 'key':
        path = filedialog.askdirectory(initialdir='C:')
        entry_field.delete(0, tkinter.END)
        entry_field.insert(0, path)
        
        key_path = path
        print("key path : " + key_path)

def findword(name):
    name = filter_path + '/' + name
    zip = zipfile.ZipFile(name)
    ziplist = zip.namelist()
    status = 0
    print(ziplist)
    for files in ziplist:
        if 'Packet' in files:
            print("detect Packet : " + files)
            status = 1
        elif 'Capture.txt' in files:
            print("detect Capture : " + files)
            if status != 1:
                status = 2
    return status

def dirsearch():

    file = os.listdir(filter_path)
    packet = ''
    scct = ''
    count = 0
    for name in file:
        print("Name : " + name + '\n')
        try :
            status = findword(name)
            if status == 1 :
                packet = packet + 'Detect Packet : ' + name + '\n'
                count+=1
            elif status == 2 :
                scct = scct + 'Detect Capture : ' + name + '\n'
                count+=1
        except:
            pass
    keep = 'Suspect : ' + str(count) + '\n' + packet + scct

    if count == 0:
        messagebox.showinfo(message="All Done!!!")
    else:
        messagebox.showinfo(message=keep)

def extract_decrypt():
    global dirs_path

    s_path = suspect_path.split('/')
    get_pop = s_path.pop()
    slade = 0
    dirs_path = ''
    for i in s_path:
        if slade :
            dirs_path = dirs_path + '/'    
        dirs_path = dirs_path + i
        slade = 1

    with zipfile.ZipFile(suspect_path, 'r') as f:
        f.extractall(dirs_path)
        messagebox.showinfo(message="Extract Complete!!!")
        f.close()
    
    get_pop = get_pop.replace(".zip",'')
    send = dirs_path +'/'+ get_pop
    decrypt(send)

def decrypt(fileextract):

    # decrypt textfile
    print("====================================================\n")
    print("\nDecrypt text\n")

    with open(key_path + '/AESkey', 'rb') as f:
        aes_k = f.read()

    with open(key_path + '/Private_Key.pem', 'rb') as f:
        pvt_k = f.read()
    print("fileextract : " + fileextract)
    file = os.listdir(fileextract)
    
    for name_file in file:
        if '.txt' in name_file:
            print("name_file : "+ str(name_file))
            send = fileextract + '/' + str(name_file)
            text_decrypt(send)
        elif 'Capture' in name_file:
            capture_file = os.listdir(fileextract + '/' + str(name_file))
            print("folder capture : "+ str(capture_file))
            # type list
            if capture_file:
                picture_decrypt(fileextract + '/' + str(name_file))
        elif 'Packet' in name_file:
            packet_file = os.listdir(fileextract + '/' + str(name_file))
            print("folder packet : "+ str(packet_file))
            # type list
            if packet_file:
                send = fileextract + '/' + str(name_file)
                file_decrypt(send)
        else:
            messagebox.showinfo(title="?????", message="????? : " + name_file)

def text_decrypt(file):

    with open('File_Generate/AESKey', 'rb') as f:
        aeskey = f.read()
        
    with open(file, 'rb') as f:
        lock = f.read(256)
        text = f.read()

    pvt = RSA.import_key(open('File_Generate/Private_Key.pem', 'rb').read())
    pvtkey = PKCS1_v1_5.new(pvt)
    obj = pvtkey.decrypt(lock, Random.new().read)

    digest = SHA512.new()
    digest.update(text)
    print("text : ",digest.digest())

    if obj == digest.digest() :
        print("true")

        with open(file, 'wb') as f:
            f.write(text)
        
        with open(file, 'rb') as f:
            iv = f.read(16)
            tag = f.read(16)
            textdata = f.read()

        # get AES key to decrypt text
        cipher = AES.new(aeskey, AES.MODE_EAX, nonce=iv)
        plaintext = cipher.decrypt_and_verify(textdata, tag).decode('UTF-8')

        with open(file, 'w') as f:
            f.write(plaintext)

    else :
        print("false")

def file_decrypt(files):

    with open('File_Generate/AESKey', 'rb') as f:
        aeskey = f.read()
    
    list_text = os.listdir(files)
    for eachfile in list_text:
        file = files + '/' + eachfile
        print("file decrypt : " + file)
        if '.txt' in eachfile:            
            text_decrypt(file)
        else :
            print("false")

def picture_decrypt(filedir_):

    print("decrypt\n")
    aes_key = 'File_Generate/AESkey'
    with open(aes_key, 'rb') as f:
        k = f.read()

    list_pic = os.listdir(filedir_)
    for eachfile in list_pic:
        file = filedir_ + '/' + eachfile
        print("decrypt picture : "+ file)
        if ('.jpg' in eachfile) or ('.png' in eachfile):             
            with open(file, 'rb') as f:
                lock = f.read(256)
                text = f.read()

            pvt = RSA.import_key(open('File_Generate/Private_Key.pem').read())
            pvtkey = PKCS1_v1_5.new(pvt)
            obj = pvtkey.decrypt(lock, Random.new().read)

            digest = SHA512.new()
            digest.update(text)
            print("text : ",digest.digest())

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

#========================================= UI =====================================
def main_frame():
    global page

    frame_main = Frame(App, height=400, width=100, background='#65728d')
    frame_main.place(x=0,y=0)

    btn_home = Button(frame_main, text="Home",font=BOLD,bd=0,foreground='#ffffff', background='#65728d',command=frame_home)
    btn_home.place(x=10,y=30)

    btn_config = Button(frame_main, text="Config",font=BOLD,bd=0,foreground='#ffffff', background='#65728d',command=frame_config)
    btn_config.place(x=10, y=70)

    btn_decreypt = Button(frame_main, text="Decrypt",font=BOLD,bd=0,foreground='#ffffff', background='#65728d',command=frame_decrypt)
    btn_decreypt.place(x=10, y=110)

    frame_home()

def frame_home():
    global framehome

    framehome = Frame(App, height=300, width=300)
    framehome.place(x=100, y=0)

    label_home = Label(framehome, text='Home Page', font=BOLD)
    label_home.place(x=100,y=100)
    
def frame_config():
    global framecon,subject_entry,hour_startbox,min_startbox,hour_stopbox,min_stopbox,check,keyword_entry

    framecon = Frame(App, height=300, width=300)
    framecon.place(x=100, y=0)

    min = []
    hour = []

    for i in range(61):
        if i < 10:
            i = "0" + str(i)
            min.append(i)
            hour.append(i)
        elif i <= 23:
            hour.append(i)
        if (type(i) == int)and(i >= 10) :
            min.append(i)

    subject_label = Label(framecon, text='Subject : ', font=BOLD)
    subject_label.place(x=20, y=30)

    subject_entry = Entry(framecon, width=25)
    subject_entry.place(x=100, y=33)

    time_label = Label(framecon, text='Time : ', font=BOLD)
    time_label.place(x=20, y=70)

    hour_startbox = tkinter.StringVar()
    hour_start = ttk.Combobox(framecon, width=3, textvariable = hour_startbox)
    hour_start['values'] = hour
    hour_start.place(x=70, y=72)

    min_startbox = tkinter.StringVar()
    min_start = ttk.Combobox(framecon, width=3, textvariable = min_startbox)
    min_start['values'] = min
    min_start.place(x=120, y=72)

    label_ = Label(framecon, text='-')
    label_.place(x=170, y=70)

    hour_stopbox = tkinter.StringVar()
    hour_stop = ttk.Combobox(framecon, width=3, textvariable = hour_stopbox)
    hour_stop['values'] = hour
    hour_stop.place(x=190, y=72)

    min_stopbox = tkinter.StringVar()
    min_stop = ttk.Combobox(framecon, width=3, textvariable = min_stopbox)
    min_stop['values'] = min
    min_stop.place(x=240, y=72)
    
    check_label = Label(framecon, text='Add more Application Ex. Discord,Skype')
    check_label.place(x=50, y=120)
    check = BooleanVar()
    check_box = Checkbutton(framecon, variable=check)
    check_box.place(x=20, y=120)

    keyword_entry = Entry(framecon, width=40)
    keyword_entry.place(x=20, y=150)
    
    submit_btn = Button(framecon, text="Build", font=BOLD, command=on_click)
    submit_btn.place(x=130, y=200)

def frame_decrypt():
    global framedecrypt

    framedecrypt = Frame(App, height=300, width=300)
    framedecrypt.place(x=100, y=0)

    framefolder = Frame(framedecrypt, height=40, width=300, background="#b9dfa9")
    framefolder.place(x=0, y=0)
    text1_label = Label(framefolder, text='Path folder to Filter', font=BOLD, background="#b9dfa9")
    text1_label.place(x=10, y=8) 

    pathdir_label = Label(framedecrypt, text='folder :',font=BOLD)
    pathdir_label.place(x=10, y=50)
    pathdir_entry = Entry(framedecrypt, width=30)
    pathdir_entry.place(x=85,y=52)
    pathdir_btn = Button(framedecrypt, text='...', font=BOLD, bd=1, command=lambda: set_path(pathdir_entry, "filter"))
    pathdir_btn.place(x=275, y=45)

    
    filter_btn = Button(framedecrypt, text='filter', font=BOLD, bd=1, command=dirsearch)
    filter_btn.place(x=20, y=80)

    label_findsol = Label(framedecrypt, text='================================', font=BOLD)
    label_findsol.place(x=0,y=110)

    framesuspect = Frame(framedecrypt, height=40, width=300, background="#ff7caf")
    framesuspect.place(x=0, y=130)
    text2_label = Label(framesuspect, text='Path folder suspect', font=BOLD, background="#ff7caf")
    text2_label.place(x=10, y=8) 

    pathsc_label = Label(framedecrypt, text='suspect :',font=BOLD)
    pathsc_label.place(x=10, y=180)
    pathsc_entry = Entry(framedecrypt, width=30)
    pathsc_entry.place(x=85,y=182)
    pathsc_btn = Button(framedecrypt, text='...', font=BOLD, bd=1, command=lambda: set_path(pathsc_entry, "suspect"))
    pathsc_btn.place(x=275, y=175)

    pathkey_label = Label(framedecrypt, text='key :',font=BOLD)
    pathkey_label.place(x=10, y=220)
    pathkey_entry = Entry(framedecrypt, width=30)
    pathkey_entry.place(x=85,y=222)
    pathkey_btn = Button(framedecrypt, text='...', font=BOLD, bd=1, command=lambda: set_path(pathkey_entry, "key"))
    pathkey_btn.place(x=275, y=215)

    decrypt_btn = Button(framedecrypt, text='Decrypt', font=BOLD, bd=1, command=extract_decrypt)
    decrypt_btn.place(x=20, y=260)

App = tkinter.Tk()
App.title("Anticheat Config")
App.geometry("400x300")
App.iconbitmap('material/icon2.ico')

main_frame()

App.mainloop()