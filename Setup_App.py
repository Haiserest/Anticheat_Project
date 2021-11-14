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
    fileAES = subject+"/File_Generate/AESkey.pem"
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

    Public_key_file = subject + '/' + subject +"/material/Public_Key.pem"
    os.makedirs(os.path.dirname(Public_key_file), exist_ok=True)
    with open(Public_key_file, 'wb') as f:
        f.write(Public_Key)
        f.close()

#====================================== function ==================================

def createApp(subject, time_start, time_stop):
    
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
    main_app = main_app.replace("TIMER_START", time1)
    main_app = main_app.replace("TIMER_STOP", time2)

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
    subject = subject.replace(' ','_')
    # print(subject)
    time_list = [str(hour_startbox.get()), str(min_startbox.get()), str(hour_stopbox.get()), str(min_stopbox.get())]
    err = 0
    i = 0
    while i != len(time_list):
        if (len(time_list[i]) == 0):
            time_list[i] = "00"
        elif (len(time_list[i]) == 1):
            time_list[i] = "0" + time_list[i]
        elif (len(time_list[i]) > 2):
            err = 1
        i+=1
    if err:
        messagebox.showerror(title="Invalid", message="Time Invalid!!")
    else:
        timingstart = str(time_list[0]) + str(time_list[1]) + "00"
        timingstop = str(time_list[2]) + str(time_list[3]) + "00"
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

    btn_decreypt = Button(frame_main, text="Option",font=BOLD,bd=0,foreground='#ffffff', background='#65728d',command=frame_decrypt)
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