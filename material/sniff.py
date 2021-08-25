from winpcapy import WinPcapDevices

with WinPcapDevices() as devices:
     for device in devices:
         print (device.name, device.description, device.flags ,device.addresses.contents.netmask.contents.sa_family)