### display filter program activate running 
tasklist /fi "STATUS eq RUNNING" >

### display tcp connection exec every 5 sec
netstat -b 5 > scan.txt

### kil task manage to stop Keylogger
taskkill /IM python.exe /F

### hide folder & file
attrib [+option] [file]
+ : enable
- : disable
[+option]
r : read mode
h : hide mode 
s : set 
                    ex: attib +r text.txt
                        attrib /s /d : all file & dir

python create 
>>pip install pyinstaller
    pyinstaller --onefile xxxxxx.py