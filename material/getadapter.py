import subprocess
from prettytable import PrettyTable

subprocess.run("wmic nic get Name > Name_adapter.txt",shell=True)
subprocess.run("wmic nic get Netconnectionstatus > status_adapter.txt",shell=True)

with open('Name_adapter.txt', 'rb') as f:
    alladapter = f.read().decode("utf-16")

with open('status_adapter.txt', 'rb') as f:
    status = f.read().decode("utf-16")

subprocess.run('del "Name_adapter.txt"', shell=True)
subprocess.run('del "status_adapter.txt"', shell=True)

listadapter = alladapter.split("\r\n")
status = status.replace(" ","")
liststatus = status.split("\r\n")
count = len(listadapter)

table = PrettyTable([listadapter[0],liststatus[0]])

for i in range(1,count-1):
    table.add_row([
        str(listadapter[i]),
        str(liststatus[i])
    ])

adapter = []
wireless_adapter = []
found = 0

for i in range(1,count-1):

    # print(listadapter[i])
    if ( "Wireless" in listadapter[i] ) or ( "LAN" in listadapter[i] ) or ( "USB" in listadapter[i] ) :
        # print("\n\n >>> "+ listadapter[i] +"\n\n")
        
        try :      
            # print("\n****************\nName : " + listadapter[i] + " \nStatus : " + liststatus[i] +"\n*****************\n")

            # NetConnectionStatus
            #     Disconnected (0)
            #     Connecting (1)
            #     Connected (2)
            #     Disconnecting (3)
            #     Hardware Not Present (4)
            #     Hardware Disabled (5)
            #     Hardware Malfunction (6)
            #     Media Disconnected (7)
            #     Authenticating (8)
            #     Authentication Succeeded (9)
            #     Authentication Failed (10)
            #     Invalid Address (11)
            #     Credentials Required (12)

            if (liststatus[i] == '2') :
                # print("\n=====================\nactive " + listadapter[i] +"\n=====================\n")
                wireless_adapter.append(str(listadapter[i].strip()))
                
                with open('Temp/Name_adapter.txt', 'a') as f:
                    if (found > 0):
                        f.write('\n')
                    f.write(str(listadapter[i].strip()))
                    found+=1
        except:
            pass 

# print("Wireless Adapter :\n" + str(wireless_adapter))
