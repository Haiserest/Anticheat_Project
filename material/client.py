import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

host = str(s.getsockname()[0])
port = 8080
quese = 0
DISCONNECT = "DISCONNECT"

s= socket.socket()
s.connect((host, port))

print("Connect....")

filename =''
# filename = input(str("Enter filename : "))
all_dir = os.listdir()
for n in all_dir:
    print(n)
    try : 
        sub = f"{n}/"
        subfile = os.listdir(sub)
        if "Capture" in subfile:
            # print(f"subfile : {n}")
            filename = n + ".zip"
    except:
        pass

namezip = '[zip]'
zipsend = namezip+filename
zipsend = bytes(zipsend, 'utf-8')
print(f"send : {type(zipsend)}")
s.send(zipsend)

def disconnect():
    print(DISCONNECT)
    s.send(DISCONNECT.encode('utf-8'))

with open(filename, 'rb') as f:
    file = f.read()
size_data = len(file)
round = (size_data//2000)+1
print(f"round : {round}")
print(size_data)
if size_data > 2048:
    i = 0
    while i < round:
        head = '[seq]'
        temp = file[:2000]
        # print(f"type : {type(temp)}")
        file_data =  bytes(head, 'utf-8') + temp
        file = file[2000:]
        i+=1
        file_data = temp
        # print(f"file_data : {type(file_data)}")
        s.send(file_data)
        
else:
    file_data = file
    # print(f"file_data : {type(file_data)}")
    print("Sending Done..")
    s.send(file_data)
    
# print("Data transfer success....")
disconnect()