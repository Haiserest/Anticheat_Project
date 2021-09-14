from scapy.all import *
import datetime

# disable verbose mode
conf.verb = 0

def parse_packet(packet):
    """
        sniff callback function.
    """
    # print("============= [packet] =============")
    discord = "discord"
    ts3 = "teamspeak"
    sk = "skype"
    if packet and packet.haslayer('UDP'):
        # udp = packet.getlayer('UDP')
        # udp.show()
        udp = packet.firstlayer()
        # udp.show()
        file_packet = 'Temp/' + str(datetime.datetime.now().strftime("Packet_%H%M%S")) + ".txt"
        udp_packet = udp.show(dump = True)
        pac = str(udp_packet)
        if (discord in pac) or (ts3 in pac) or (sk in pac):

            with open (file_packet, 'a') as f:
                f.write(pac)
        
def udp_sniffer(adapter):
    """
        start a sniffer.
    """

    print('\n[*] start udp sniffer')
    sniff(
        filter="udp port 53",
        iface=adapter, prn=parse_packet
    )


if __name__ == '__main__':

    with open('Name_adapter.txt', 'r') as f:
        all_adapter = f.read()

    list_adapter = all_adapter.split('\n')
    # print(list_adapter)

    udp_sniffer(list_adapter[0])