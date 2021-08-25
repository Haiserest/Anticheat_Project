import wmi
obj = wmi.WMI().Win32_PnPEntity(ConfigManagerErrorCode=0)

displays = [x for x in obj if 'DISPLAY' in str(x)]
i = 0
for item in displays:
   # print(i)
   # print (item)
   i +=1
i-=1

if i == 1:
   print("single Monitor")
elif i > 1:
   print("Multi Monitor : [" + str(i) + "]")