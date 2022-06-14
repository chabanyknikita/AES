import hashlib
from Crypto.Cipher import AES


def encrypting():
    pas = input('Write your password:').encode('utf-8')
    msg = input("Write your message:").encode('utf-8')

    def padding(msg):
        while len(msg) % 16 != 0:
            msg = msg + b' '
        return msg

    key = hashlib.sha3_256(pas).digest()
    cipher = AES.new(key, AES.MODE_CBC)
    msg_pad = padding(msg)

    encrypted_msg = cipher.encrypt(msg_pad)
    with open("encrypted.bin", "wb") as wen:
        wen.write(cipher.iv)
        wen.write(encrypted_msg)


def decryption():
    pas = input('Write your password for decrypt your data:').encode('utf-8')
    key = hashlib.sha3_256(pas).digest()

    with open("encrypted.bin", "rb") as read_en:
        cipher = AES.new(key, AES.MODE_CBC, read_en.read(16))
        decrypt_msg = cipher.decrypt(read_en.read())
        decrypt_msg = decrypt_msg.decode('utf-8')
        print("This is original message", decrypt_msg)
