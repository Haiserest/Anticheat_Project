import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

host = str(s.getsockname()[0])
port = 8080
rawdata = ''
folder = ''
CONNECT = True

s = socket.socket()
s.bind((host, port))
s.listen()

print(f"[{host}] Waiting Incoming ......")
conn, addr = s.accept()
print(addr, " Connected....")

while CONNECT:
    file_data = conn.recv(2048)
     
    if file_data:
        if file_data[:5] == '[seq]':
            rawdata = rawdata + file_data[5:]
        elif '[zip]' in str(file_data):
            folder = folder + file_data[5:].decode('utf-8')
            filename = f"copy_{folder}"
            print(f"filename : {filename}")
        else:
            # print(f"[{folder} Create....]")
            rawdata = rawdata = file_data
            # filename = f"{addr[0]}.zip"
            file = open(filename, 'ab')
            # print(rawdata)
            file.write(rawdata)
            file.close()
            rawdata = ''
        if 'DISCONNECT' in str(file_data) :
            conn.close()
            print("Success....")
            CONNECT = False  