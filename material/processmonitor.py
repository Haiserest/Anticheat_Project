import subprocess
import datetime

global keyword_app
keyword_app = ['DISCORD', 'SKYPE', 'TEAMSPEAKER']

def tasklist():
    subprocess.run('tasklist /fi \"STATUS eq RUNNING\" > Temp\\running.txt', shell=True)
    with open('Temp/running.txt', 'r') as r:
        x = r.read().upper()
    for name in keyword_app:
        if name in x:
            print(name)
            subprocess.run('taskkill /IM '+name+'.exe /F',shell=True)
        else:
            pass

    subprocess.run('tasklist /fi \"STATUS eq RUNNING\" > Temp\\running.txt', shell=True)

    with open('Temp/running.txt', 'r') as r:
        x = r.read().upper()
        detect = ''
                                                                    # filter keyword application voice chat
    for name in keyword_app:
        if x.find(name) >= 0:
            detect += name + '\n'
                                                                    # get process detected to exe.txt            
            task = 'Temp/exe.txt'
            with open(task, 'a') as f:
                tasktime = str(datetime.datetime.now().strftime('Time >> %H : %M : %S\n'))
                f.write(tasktime)
                f.write(detect)
                f.close()
        else:
            print("pass")

tasklist()