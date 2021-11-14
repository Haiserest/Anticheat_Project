import subprocess

try:    
    subprocess.run('pip install pyinstaller')    
    subprocess.run('pip install pycryptodome==3.10.1')    
    subprocess.run('pip install WMI==1.5.1')    
    subprocess.run('pip install scapy==2.4.5')    
    subprocess.run('pip install winpcapy==1.0.2')
    subprocess.run('pip install pynput==1.6.8')    
    subprocess.run('pip install mss==6.1.0')    
    subprocess.run('pip install prettytable==2.1.0')
except:
    pass

subprocess.run('pyinstaller --onefile -i material/icon2.ico Main_App.py', shell=True)
subprocess.run('copy dist\Main_App.exe Application.exe', shell=True)