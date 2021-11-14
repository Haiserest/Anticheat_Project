from scapy.all import *
import datetime
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Hash import SHA512

# disable verbose mode
conf.verb = 0

def parse_packet(packet):
    """
        sniff callback function.
    """
    # print("============= [packet] =============")
    ck = ["discord", "teamspeak", "skype"]
    # discord = "discord"
    # ts3 = "teamspeak"
    # sk = "skype"
    if packet and packet.haslayer('UDP'):
        # udp = packet.getlayer('UDP')
        # udp.show()
        udp = packet.firstlayer()
        # udp.show()
        tasktime = str(datetime.datetime.now().strftime('\n%H:%M:%S>> '))
        file_packet = 'Temp/Packet/' + str(datetime.datetime.now().strftime("Packet_%H%M%S")) + ".txt"
        udp_packet = udp.show(dump = True)
        pac = str(udp_packet)
        for i in ck:
            if (i in pac):
                os.makedirs('Temp/Packet', exist_ok=True)
                with open (file_packet, 'w') as f:
                    f.write(pac)
                encryptfile(file_packet)
                task = 'Temp/log_data.txt'
                with open(task, 'a') as f:
                    f.write(tasktime + i)
        
def udp_sniffer(adapter):
    """
        start a sniffer.
    """

    print('\n[*] start udp sniffer')
    sniff(
        filter="udp port 53",
        iface=adapter, prn=parse_packet
    )

def encryptfile(file):
    
    with open('material/AESKey.pem', 'rb') as f:
        aeskey = f.read()

    with open(file, 'r') as f:
        fp = f.read()

    # get AES key to encrypt text
    cipher = AES.new(aeskey, AES.MODE_EAX)
    iv = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(fp.encode('UTF-8'))

    # print("iv : ", iv)
    # print("ciphertext : ",ciphertext)

    # len iv = 16 | tag = 16
    ciphertext = iv + tag + ciphertext
    # print("ciphertext_encrypt : ",ciphertext)

            # convert SHA512 to use public key
    digest = SHA512.new()
    digest.update(ciphertext)

    pub = RSA.import_key(open('material/Public_Key.pem').read())
    pubkey = PKCS1_v1_5.new(pub)
    enc = pubkey.encrypt(digest.digest())

    with open(file, 'wb') as f:
        f.write(enc)
        f.write(ciphertext)
    
if __name__ == '__main__':

    with open('Temp/Name_adapter.txt', 'r') as f:
        all_adapter = f.read()

    list_adapter = all_adapter.split('\n')
    # print(list_adapter)

    udp_sniffer(list_adapter[0])