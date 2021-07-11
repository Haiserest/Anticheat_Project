from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as kf:
        kf.write(key)

def load_key():
    return open("key.key", "rb").read()

def encrypt(file,key):
    quit()


write_key()
key = load_key()
print(key)

