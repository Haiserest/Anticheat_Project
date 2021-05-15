### display filter program activate running 
tasklist /fi "STATUS eq RUNNING" >

### display tcp connection exec every 5 sec
netstat -b 5 > scan.txt




python create 
>>pip install pyinstaller
    pyinstaller --onefile xxxxxx.py