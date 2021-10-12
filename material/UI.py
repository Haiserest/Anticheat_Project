import tkinter
from tkinter import *
from tkinter import filedialog,messagebox
from tkinter import ttk
from tkinter.font import BOLD
import datetime
import os
import subprocess
import zipfile
import random

global keywords
keywords = ['DISCORD','SKYPE','TEAMSPEAKER']

def listfilezip():
    file = os.listdir(id)
    file_list = []
    keep = ''
    count = 1
    for name in file:
        keep = keep + str(count) + ' : ' + name + '\n'
        file_list.append(id+'/'+name)
        count+=1
    count = count - 1
    keep = 'Found : ' + str(count) + '\n' + keep
    print(file_list)
    file_compress(file_list)
    

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

def findword(name):
    name = name_dirpath + '/' + name
    zip = zipfile.ZipFile(name)
    ziplist = zip.namelist()
    for files in ziplist:
        if 'Packet' in files:
            print("detect Packet : " + files)
            return 1
        elif 'Capture' in files:
            print("detect Capture : " + files)
            return 2
    # print(ziplist)
    return 0

def set_path(entry_field):
    path = filedialog.askdirectory(initialdir='C:')
    entry_field.delete(0, tkinter.END)
    entry_field.insert(0, path)

    global name_dirpath
    name_dirpath = path
    print("directory path : " + name_dirpath)


def dirsearch():

    file = os.listdir(name_dirpath)
    packet = ''
    scct = ''
    count = 1
    for name in file:
        status = findword(name)
        if status == 1 :
            packet = packet + 'Detect Packet : ' + name + '\n'
            count+=1
        elif status == 2 :
            scct = scct + 'Detect Capture : ' + name + '\n'
            count+=1
    count = count - 1
    keep = 'Suspect : ' + str(count) + '\n' + packet + scct

    if count == 0:
        messagebox.showinfo(message="All Done!!!")
    else:
        messagebox.showinfo(message=keep)

def kk():
    ck = check.get()
    key = keyword_entry.get()

    if ck:
        k = key.split(',')
        for count in range(len(k)):
            keywords.append(k[count].upper())
    else:
        pass
    print(keywords)

def pop_up():
    ans = messagebox.askyesno(title='Finish test', message='Are You Finish Test?')
    if ans:
        messagebox.showinfo(message='test compete!!')
        listfilezip()
        main_frame()
    else:
        pass

def tasklist():
    subprocess.run('tasklist /fi \"STATUS eq RUNNING\" > running.txt', shell=True)
    with open('running.txt', 'r') as r:
        x = r.read().upper()
    for name in keywords:
        if name in x:
            subprocess.run('taskkill /IM '+name+'.exe /F',shell=True)
        else:
            pass
    subprocess.run('del "running.txt"', shell=True)

def sumbit():
    global id

    id = id_std.get()
    entry_id.delete(0,END)
    tasklist()
    createfolder()
    return frame_clock()

def createfolder():
    subprocess.run('mkdir '+id, shell=True)
    file_random = ['log1.txt','log2.txt','Packet.txt','log3.txt']
    for i in range(1,2):
        name = id+'/file_'+ random.choice(file_random)
        with open(name, 'w') as f:
            f.write(name)

def main_frame():
    global page

    frame_main = Frame(Application, height=400, width=100, background='#65728d')
    frame_main.place(x=0,y=0)

    btn_home = Button(frame_main, text="Home",font=BOLD,bd=0,foreground='#ffffff', background='#65728d',command=frame_home)
    btn_home.place(x=10,y=30)

    btn_config = Button(frame_main, text="Config",font=BOLD,bd=0,foreground='#ffffff', background='#65728d',command=frame_config)
    btn_config.place(x=10, y=70)

    btn_decreypt = Button(frame_main, text="Decrypt",font=BOLD,bd=0,foreground='#ffffff', background='#65728d',command=frame_decrypt)
    btn_decreypt.place(x=10, y=110)

    btn_test = Button(frame_main, text="Test",font=BOLD,bd=0,foreground='#ffffff', background='#65728d',command=frame_id)
    btn_test.place(x=10, y=150)

    btn_clock = Button(frame_main, text="Clock",font=BOLD,bd=0,foreground='#ffffff', background='#65728d',command=frame_clock)
    btn_clock.place(x=10, y=190)

    frame_home()

def frame_home():
    global framehome

    framehome = Frame(Application, height=300, width=300)
    framehome.place(x=100, y=0)

    label_home = Label(framehome, text='Home Page', font=BOLD)
    label_home.place(x=100,y=100)
    

def frame_config():
    global framecon,keyword_entry,check

    framecon = Frame(Application, height=300, width=300)
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

    submit_btn = Button(framecon, text="Build", font=BOLD, command = kk)
    submit_btn.place(x=110, y=200)

def frame_decrypt():
    global framedecrypt

    framedecrypt = Frame(Application, height=300, width=300)
    framedecrypt.place(x=100, y=0)

    pathdir_label = Label(framedecrypt, text='dir path :',font=BOLD)
    pathdir_label.place(x=10, y=40)
    pathdir_entry = Entry(framedecrypt, width=30)
    pathdir_entry.place(x=85,y=42)
    pathdir_btn = Button(framedecrypt, text='...', font=BOLD, bd=1, command=lambda: set_path(pathdir_entry))
    pathdir_btn.place(x=275, y=35)

    search_btn = Button(framedecrypt, text='O-O', font=BOLD, bd=1, command=dirsearch)
    search_btn.place(x=20, y=70)

    label_findsol = Label(framedecrypt, text='==============================', font=BOLD)
    label_findsol.place(x=10,y=100)

    pathsc_label = Label(framedecrypt, text='file path :',font=BOLD)
    pathsc_label.place(x=10, y=140)
    pathsc_entry = Entry(framedecrypt, width=30)
    pathsc_entry.place(x=85,y=142)
    pathsc_btn = Button(framedecrypt, text='...', font=BOLD, bd=1)
    pathsc_btn.place(x=275, y=135)

    pathkey_label = Label(framedecrypt, text='key path :',font=BOLD)
    pathkey_label.place(x=10, y=180)
    pathkey_entry = Entry(framedecrypt, width=30)
    pathkey_entry.place(x=85,y=182)
    pathkey_btn = Button(framedecrypt, text='...', font=BOLD, bd=1)
    pathkey_btn.place(x=275, y=175)

    decrypt_btn = Button(framedecrypt, text='Decrypt', font=BOLD, bd=1)
    decrypt_btn.place(x=20, y=220)

def frame_id():
    global id_std,frametest,entry_id

    frametest = Frame(Application, height=300, width=300)
    frametest.place(x=100, y=0)
    
    label_id = Label(frametest, text="ID : ")
    label_id.place(x=30, y=40)

    id_std = StringVar()

    entry_id = Entry(frametest, width=30, textvariable= id_std)
    entry_id.place(x=60, y=43)

    btn_submit = Button(frametest, text="Submit", command=sumbit)
    btn_submit.place(x=120, y=100)

def frame_clock():
    global frameclock

    frameclock = Frame(Application, height=300, width=300)
    frameclock.place(x=100, y=0)
    try :
        framename = Frame(frameclock,height=40,width=300,background="#a9c8dd")
        framename.place(x=0,y=0)

        std_label = Label(framename, text='Student ID: '+id , font=BOLD, background="#a9c8dd")
        std_label.place(x=10,y=10)

    except:
        messagebox.showerror(title='error', message='Something Wrong!!')

    def clock():
        hour = str(datetime.datetime.now().strftime('%H'))
        minute = str(datetime.datetime.now().strftime('%M'))
        second = str(datetime.datetime.now().strftime('%S'))

        timer = hour + ':' + minute + ':' + second
        clock_label.config(text=timer)
        clock_label.after(1000, clock)

    clock_label = Label(frameclock, text="", font=("Raleway", 20))
    clock_label.place(x=90, y=50)

    clock()

    btn_back = Button(frameclock, text="Finish", command=pop_up)
    btn_back.place(x=120, y=100)


Application = tkinter.Tk()
Application.title("Anticheat")
Application.geometry("400x300")
Application.iconbitmap('material/icon2.ico')

main_frame()

Application.mainloop()

