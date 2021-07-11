import subprocess

subprocess.run("tasklist /fi \"STATUS eq RUNNING\" > Temp\\running.txt", shell=True)
subprocess.run("netstat -b > Temp\\scan.txt", shell=True)