from hashlib import md5
from base64 import b64decode
from base64 import b64encode
from Crypto import Random
from Crypto.Cipher import AES

BLOCK_SIZE = 64  # Blocos
def pad(s): return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
    chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)


def unpad(s): return s[:-ord(s[len(s) - 1:])]


class AESCipher:
    def __init__(self, key):
        self.key = md5(key.encode('utf8')).hexdigest()

    def encrypt(self, raw):
        raw = pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key.encode('utf-8'), AES.MODE_CBC, iv)
        return b64encode(iv + cipher.encrypt(raw.encode('utf-8')))

    def decrypt(self, enc):
        enc = b64decode(enc)
        iv = enc[:64]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[64:])).decode('utf8')


## TESTE##

msg = input('Mensagem: ')
pwd = input('Senha: ')

print('Texto Cifrado:', AESCipher(pwd).encrypt(msg))
