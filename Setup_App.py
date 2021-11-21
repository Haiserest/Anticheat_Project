import tkinter
from tkinter import *
from tkinter import filedialog,messagebox
from tkinter import ttk
from tkinter.font import BOLD
import subprocess
import socket
import os
import zipfile
import shutil
import datetime
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Hash import SHA512
from Crypto import Random
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

#=====================key==============================

def ipv4_host():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))

    host = str(s.getsockname()[0])
    return host

def generateAESkey(subject):
    # key AES 256 bits
    key = get_random_bytes(32)

    # save Create AES key
    fileAES = subject+"/KEY/AESkey.pem"
    os.makedirs(os.path.dirname(fileAES), exist_ok=True)
    with open(fileAES, 'wb') as f:
        f.write(key)
        f.close()

    # save key for std

    fileAES = subject + '/' + subject + "/material/AESkey.pem"
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

    Private_key_file = subject+"/KEY/Private_Key.pem"
    os.makedirs(os.path.dirname(Private_key_file), exist_ok=True)
    with open(Private_key_file, 'wb') as f:
        f.write(Private_Key)
        f.close()

    Public_key_file = subject+"/KEY/Public_Key.pem"
    os.makedirs(os.path.dirname(Public_key_file), exist_ok=True)
    with open(Public_key_file, 'wb') as f:
        f.write(Public_Key)
        f.close()

    # save key for std

    Public_key_file = subject + '/' + subject +"/material/Public_Key.pem"
    os.makedirs(os.path.dirname(Public_key_file), exist_ok=True)
    with open(Public_key_file, 'wb') as f:
        f.write(Public_Key)
        f.close()

#====================================== function ==================================

def createApp(subject, time_start, time_stop, ts, tf, keyword, daytime):
    
    subprocess.run("mkdir "+subject, shell=True)

    with open('material/file_main', 'r') as f:
        main_app = f.read()

    with open('material/file_key', 'r') as f:
        key_app = f.read()

    with open('material/file_net', 'r') as f:
        net_app = f.read()

    with open('material/file_adapter', 'r') as f:
        adapt_app = f.read()

    with open('material/file_process', 'r') as f:
        process_app = f.read()

    with open('material/install_setup', 'r') as f:
        install = f.read()

    with open('material/client' ,'r') as f:
        client = f.read()

    with open('material/server', 'r') as f:
        server = f.read()
        
    time1 =str(time_start)
    time2 =str(time_stop)
    tt = f"{ts} - {tf}"
    main_app = main_app.replace("TIMER_START", time1)
    main_app = main_app.replace("TIMER_STOP", time2)
    main_app = main_app.replace("DAYTIME", daytime)
    main_app = main_app.replace("Name_Subject", subject)
    main_app = main_app.replace("TIMETOTEST", tt)
    app_exe = ''
    for k in range(len(keyword)):
        app_exe = f"{app_exe}'{keyword[k]}'"
        if k+1 != len(keyword):
            app_exe = app_exe+','        
    main_app = main_app.replace('"application_outside"', app_exe)
    process_app = process_app.replace('"application_outside"', app_exe)

    app_exe = app_exe.lower()
    
    net_app = net_app.replace('"application_outside"', app_exe)
    
    host = ipv4_host()
    client = client.replace("HOST_IP_SERVER", host)
    server = server.replace("HOST_IP_SERVER", host)

    generateAESkey(subject)
    generateRSAkey(subject)

    file = subject+"/Recieved/"
    os.makedirs(os.path.dirname(file))
    file = file + "Recieved.py"
    with open(file, 'w') as f:
        f.write(server)
        print("create Receiver..")

    dirfile= []
    file = subject+"/"+subject+"/Main_App.py"
    with open(file, 'w') as f:
        f.write(main_app)
        print("create Main Complete")
    dirfile.append(file)

    file = subject+"/"+subject+"/material/Keylogger.py"
    with open(file, 'w') as f:
        f.write(key_app)
        print("create keylogger Complete")
    dirfile.append(file)

    file = subject+"/"+subject+"/material/networkscan.py"
    with open(file, 'w') as f:
        f.write(net_app)
        print("create Networkscan Complete")
    dirfile.append(file)

    file = subject+"/"+subject+"/material/getadapter.py"
    with open(file, 'w') as f:
        f.write(adapt_app)
        print("create Networkadapter Complete")
    dirfile.append(file)

    file = subject+"/"+subject+"/material/processmonitor.py"
    with open(file, 'w') as f:
        f.write(process_app)
        print("create processmonitor Complete")
    dirfile.append(file)

    file = subject+"/"+subject+"/client.py"
    with open(file, 'w') as f:
        f.write(client)
        print("create client Complete")
    dirfile.append(file)

    file = subject+"/"+subject+"/setup.py"
    with open(file, 'w') as f:
        f.write(install)
    
    file_icon = ['material/icon2.ico']
    for icon in file_icon:
        shutil.copy(icon, subject+'/'+ subject +'/material/icon2.ico')
    
    for name_file in dirfile:
        subprocess.run('attrib +r +h ' + name_file, shell=True)

    print("Commplete!!")
    print("=================================================")
    messagebox.showinfo(title="Create Complete", message="Create : "+subject)

    # quit()

def more_APP():

    global keywords
    keywords = ['DISCORD','SKYPE', 'SKYPEAPP','TS3']

    ck = check.get()
    key = keyword_entry.get()

    if ck:
        k = key.split(',')
        for count in range(len(k)):
            keywords.append(k[count].upper())
            k_app = k[count]+"app"
            keywords.append(k_app.upper())
    else:
        pass
    return keywords

def on_click():

    subject = subject_entry.get()
    subject = subject.replace(' ','_')
    # print(subject)
    
    day_list = [str(day_box.get()), str(month_box.get()), str(year_box.get())]
    time_list = [str(hour_startbox.get()), str(min_startbox.get()), str(hour_stopbox.get()), str(min_stopbox.get())]
    err = 0
    i = 0
    m = 0
    month_now = str(datetime.datetime.now().strftime("%B"))
    day_now = str(datetime.datetime.now().strftime("%d"))
    zero = [4, 6, 9, 11]

    for i in range(len(month)):
        if month[i] == day_list[1]:
            m = i+1
        if month[i] == str(month_now):
            month_now = i+1
    if int(year_now) == int(day_list[2]):
        if int(m) < int(month_now):
            err = 1
        elif int(m) == int(month_now):
            if int(day_list[0]) < int(day_now):
                err = 1
    
    

    if int(day_list[0]) < 0:
        err = 1
    if int(day_list[0]) > 32:
        err = 1
    if int(day_list[2]) < int(year_now):
        err = 1
    else:
        if m in zero:
            if int(day_list[0]) == 31:
                err = 1
        elif m == 2:
            if int(day_list[0]) > 30:
                err = 1
            else:
                y_n = int(year_now)%4
                if (y_n != 0) and (int(day_list[0]) == 29):
                    err = 1
    if err == 1:
        messagebox.showerror(title="Invalid", message="Date Invalid!!")
    else:
        i = 0
        err = 0

        while i != len(time_list):
            if (len(time_list[i]) == 0):
                time_list[i] = "00"
            elif (len(time_list[i]) == 1):
                time_list[i] = "0" + time_list[i]
            elif (len(time_list[i]) > 2):
                err = 1
            if int(time_list[i]) < 0:
                err = 1
            if i%2 == 0:
                if int(time_list[i]) > 23:
                    err = 1
            elif i%2 == 1:
                if int(time_list[i]) > 59:
                    err = 1
            i+=1
        if err:
            messagebox.showerror(title="Invalid", message="Time Invalid!!")
        else:
            timingstart = str(time_list[0]) + str(time_list[1]) + "00"
            timingstop = str(time_list[2]) + str(time_list[3]) + "00"
            daytime = f"{day_list[0]} {day_list[1]} {day_list[2]}"
            ts = f"{time_list[0]}:{time_list[1]}"
            tf = f"{time_list[2]}:{time_list[3]}"
            print(f"Subject : {subject}")
            print(f"Date : {daytime}")
            print(f"time start : {ts}")
            print(f"time out : {tf}")
            keyword = more_APP()

            print("-------------------------------------------")
        
            if subject :
                if int(timingstart) < int(timingstop):
                    createApp(subject, timingstart, timingstop, ts, tf, keyword, daytime)
                    # print("create_App")
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

    with open(key_path + '/AESkey.pem', 'rb') as f:
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
                print('\n'+ fileextract + '/' + str(name_file)+'\n')
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

    with open(key_path+'/AESKey.pem', 'rb') as f:
        aeskey = f.read()
        
    with open(file, 'rb') as f:
        lock = f.read(256)
        text = f.read()

    namepathpvt = key_path + '/Private_Key.pem'
    pvt = RSA.import_key(open(namepathpvt, 'rb').read())
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

    with open(key_path+'/AESKey.pem', 'rb') as f:
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
    aes_key = key_path + '/AESkey.pem'
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

            namepathpvt = key_path + '/Private_Key.pem'
            pvt = RSA.import_key(open(namepathpvt).read())
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

    btn_config = Button(frame_main, text="Create",font=BOLD,bd=0,foreground='#ffffff', background='#65728d',command=frame_config)
    btn_config.place(x=10, y=70)

    btn_decreypt = Button(frame_main, text="Result",font=BOLD,bd=0,foreground='#ffffff', background='#65728d',command=frame_decrypt)
    btn_decreypt.place(x=10, y=110)

    frame_home()

def frame_home():
    global framehome

    text_home = "\n  \tAnticheat Application \n\n\
    Create : \n\n หน้าสำหรับการสร้างโปรแกรมให้ผู้สอบ\n\n\
    Result : \n\n หน้าสำหรับการตรวจสอบไฟล์ของผู้สอบ"

    framehome = Frame(App, height=300, width=300)
    framehome.place(x=100, y=0)

    label_home = Label(framehome, text=text_home, font=BOLD, anchor="e", justify=LEFT)
    label_home.place(x=10,y=0)
    
def frame_config():
    global framecon, subject_entry, day_box, month_box, month, year_box, year_now, hour_startbox, min_startbox, hour_stopbox, min_stopbox, check, keyword_entry

    framecon = Frame(App, height=300, width=300)
    framecon.place(x=100, y=0)

    min = []
    hour = []
    day = []
    month = []
    year_now = int(datetime.datetime.now().strftime("%Y"))
    year = [str(year_now), str(year_now+1)]
    for i in range(60): 
        if i > 9 and i <= 31:
            day.append(i)
        if i > 0 and i < 13:
            t = str(datetime.date(1900, i, 1).strftime('%B'))
            month.append(t)
        if i < 10:
            i = "0" + str(i)
            min.append(i)
            hour.append(i)
            if i != "00":
                day.append(i)
        elif i <= 23:
            hour.append(i)
        
        if (type(i) == int)and(i >= 10) :
            min.append(i)

    subject_label = Label(framecon, text='Subject : ', font=BOLD)
    subject_label.place(x=20, y=30)

    subject_entry = Entry(framecon, width=25)
    subject_entry.place(x=100, y=33)

    day_label = Label(framecon, text='Date : ', font=BOLD)
    day_label.place(x=20, y=70)

    day_box = tkinter.StringVar()
    day_combobox = ttk.Combobox(framecon, width=3, textvariable= day_box)
    day_combobox['values'] = day
    day_combobox.place(x=70, y=72)

    month_box = tkinter.StringVar()
    month_combobox = ttk.Combobox(framecon, width=11, textvariable= month_box)
    month_combobox['values'] = month
    month_combobox.place(x=120, y=72)

    year_box = tkinter.StringVar()
    year_combobox = ttk.Combobox(framecon, width=4, textvariable= year_box)
    year_combobox['values'] = year
    year_combobox.place(x=220, y=72)

    time_label = Label(framecon, text='Time : ', font=BOLD)
    time_label.place(x=20, y=110)

    hour_startbox = tkinter.StringVar()
    hour_start = ttk.Combobox(framecon, width=3, textvariable = hour_startbox)
    hour_start['values'] = hour
    hour_start.place(x=70, y=112)

    min_startbox = tkinter.StringVar()
    min_start = ttk.Combobox(framecon, width=3, textvariable = min_startbox)
    min_start['values'] = min
    min_start.place(x=120, y=112)

    label_ = Label(framecon, text='-')
    label_.place(x=170, y=110)

    hour_stopbox = tkinter.StringVar()
    hour_stop = ttk.Combobox(framecon, width=3, textvariable = hour_stopbox)
    hour_stop['values'] = hour
    hour_stop.place(x=190, y=112)

    min_stopbox = tkinter.StringVar()
    min_stop = ttk.Combobox(framecon, width=3, textvariable = min_stopbox)
    min_stop['values'] = min
    min_stop.place(x=240, y=112)
    
    check_label = Label(framecon, text='Add more Application Ex. Discord,Skype')
    check_label.place(x=50, y=160)
    check = BooleanVar()
    check_box = Checkbutton(framecon, variable=check)
    check_box.place(x=20, y=160)

    keyword_entry = Entry(framecon, width=40)
    keyword_entry.place(x=20, y=190)
    
    submit_btn = Button(framecon, text="Build", font=BOLD, command=on_click)
    submit_btn.place(x=130, y=220)

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
App.title("Anticheat")
App.geometry("400x300")
App.iconbitmap('material/icon2.ico')

main_frame()

App.mainloop()