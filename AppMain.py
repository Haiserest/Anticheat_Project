import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
import datetime
import pyautogui
import subprocess
import zipfile
import wmi
import os
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA512

#===================function===========================

def listfilezip():
                                                                    # list files in directory in file var.
    file = os.listdir(id)
    file_list = []
    keep = ''
    count = 1
                                                                    # loop file to find if name '.txt'
    for name in file:
        if '.txt' in name :
            keep = keep + str(count) + ' : ' + name + '\n'
            file_list.append(id+'/'+name)
            count+=1
        else:
            dir_list = os.listdir(id+'/'+name)
            for subfile in dir_list:
                keep = keep + str(count) + ' : ' + subfile + '\n'
                file_list.append(id+'/'+name+'/'+subfile)
                count+=1
    count = count - 1
    keep = 'Found : ' + str(count) + '\n' + keep
    print(file_list)
    file_compress(file_list)
    
                                                                    # compress list files to .zip
def file_compress(file_list):
    compression = zipfile.ZIP_DEFLATED
    out_zp = id+".zip"
    zf = zipfile.ZipFile(out_zp, mode="w")
    try:
        for files in file_list:
            print(f'zip : {files}')
            zf.write(files, files, compress_type=compression)
    except FileNotFoundError as e:
        print(f'Exception {e}')
     
    zf.close  

                                                                    # detect find monitor used
def monitor():
    obj = wmi.WMI().Win32_PnPEntity(ConfigManagerErrorCode=0)

    displays = [x for x in obj if 'DISPLAY' in str(x)]
    i = 0
    for item in displays:
        #print(item)
        i +=1
    i-=1

    display = "Found Monitor : [" + str(i) + "]\n"
    print(display)  
                                                                    # write monitor used to exe.txt
    task = 'Temp/log_data.txt'
    with open(task, 'a') as f:
        f.write(display+'\n')

                                                                    # call function interrupt
def Call_function():
                                                                    # keyboard interrupt
    subprocess.Popen('python material\\Keylogger.py', shell=True)
                                                                    # scapy scan and find adapter wireless
    subprocess.Popen('python material\\getadapter.py', shell=True)
    subprocess.Popen('python material\\networkscan.py', shell=True)
                                                                    # process monitor detect keyword 
def tasklist():
    subprocess.Popen('python material\\processmonitor.py', shell=True)

                                                                    # end Application and rename file keep source
def endApp():
    tasklist()
    ans = messagebox.askyesno(title='Finish test', message='Are You Finish Test?')
    if ans:
        messagebox.showinfo(message='test compete!!')
        subprocess.run('del "Temp\\Name_adapter.txt"', shell=True)
        subprocess.run('del "Temp\\running.txt"', shell=True)
        encryptfiletext()
        subprocess.run('rename Temp ' + id, shell=True)
        try:
            listfilezip()
            subprocess.run('taskkill /IM python.exe /F', shell=True)
        except:
            messagebox.showerror(message="error!!!")
    else:
        messagebox.showerror(message='Invalid!!')

def encryptfiletext():

    with open('File_Generate/AESKey', 'rb') as f:
        aeskey = f.read()
    
    list_text = os.listdir('Temp')
    for eachfile in list_text:
        if '.txt' in eachfile:         
            file = 'Temp/' + eachfile
            with open(file, 'r') as f:
                fp = f.read()

            # get AES key to encrypt text
            cipher = AES.new(aeskey, AES.MODE_EAX)
            iv = cipher.nonce
            ciphertext, tag = cipher.encrypt_and_digest(fp.encode('UTF-8'))

            print("iv : ", iv)
            print("ciphertext : ",ciphertext)

            # len iv = 16 | tag = 16
            ciphertext = iv + tag + ciphertext
            print("ciphertext_encrypt : ",ciphertext)

            # convert SHA512 to use public key
            digest = SHA512.new()
            digest.update(ciphertext)

            pub = RSA.import_key(open('File_Generate/Public_Key.pem').read())
            pubkey = PKCS1_v1_5.new(pub)
            enc = pubkey.encrypt(digest.digest())

            with open(file, 'wb') as f:
                f.write(enc)
                f.write(ciphertext) 

def sumbit():
    global id, start
    start = 0
    id = id_std.get()
    entry_id.delete(0,END)
    return frame_clock()

def frame_id():
    global id_std,frametest,entry_id

    frametest = Frame(Application, height=150, width=300)
    frametest.place(x=0, y=0)
    
    label_id = Label(frametest, text="ID : ")
    label_id.place(x=30, y=40)

    id_std = StringVar()

    entry_id = Entry(frametest, width=30, textvariable= id_std)
    entry_id.place(x=60, y=43)

    btn_submit = Button(frametest, text="Submit", command=sumbit)
    btn_submit.place(x=120, y=100)

def frame_clock():
    global frameclock

    if id:
        subprocess.run('mkdir Temp\\Capture', shell=True)
        txt = 'Create : ' + id
        messagebox.showinfo(title='Success!!', message=txt)
        frameclock = Frame(Application, height=150, width=300)
        frameclock.place(x=0, y=0)
        try :
            framename = Frame(frameclock,height=40,width=300,background="#a9c8dd")
            framename.place(x=0,y=0)

            std_label = Label(framename, text="Student ID: "+id , font=BOLD, background="#a9c8dd")
            std_label.place(x=10,y=10)

        except:
            pass

        def clock():
            global start
            test_start = "141500"
            test_stop = ""
            hour = str(datetime.datetime.now().strftime("%H"))
            minute = str(datetime.datetime.now().strftime("%M"))
            second = str(datetime.datetime.now().strftime("%S"))

            if (hour+minute+second >= test_start) and (start == 0):
                
                start = 1
                monitor()
                tasklist()
                Call_function()
            
            elif (hour+minute+second >= test_stop):
                messagebox.showinfo(message="Time Out")
                endApp()

            timer = hour + ":" + minute + ":" + second
            clock_label.config(text=timer)
            clock_label.after(1000, clock)

        clock_label = Label(frameclock, text="", font=("Raleway", 20))
        clock_label.place(x=90, y=50)

        clock()

        btn_back = Button(frameclock, text="Finish", command=endApp)
        btn_back.place(x=120, y=100)

    else:
        messagebox.showwarning(title="warning", message="error valid")


Application = tkinter.Tk()
Application.title("Anticheat")
Application.geometry('300x150')
Application.iconbitmap('material/icon2.ico')

frame_id()

Application.mainloop()