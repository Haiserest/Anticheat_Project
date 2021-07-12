import subprocess

hello = 'python material\\h.py'
time = 'python material\\time.py'
key = 'python material\\Keylogger.py'
p = subprocess.Popen(hello, shell=True)
k = subprocess.Popen(key, shell=True)
t = subprocess.Popen(time, shell=True)
