from Crypto.Cipher import Blowfish
from struct import pack
import binascii

key = b'ABCDE'

def criptografar(plaintext, cipher):
    bs = Blowfish.block_size
    plen = bs - len(plaintext) % bs
    padding = [plen]*plen
    padding = pack('b'*plen, *padding)
    msg = cipher.encrypt(plaintext + padding)
    return msg

def decriptografar(plaintext, cipher):
    bs = Blowfish.block_size
    plen = bs - len(plaintext) % bs
    padding = [plen] * plen
    padding = pack('b' * plen, *padding)
    msg = cipher.decrypt(plaintext)# encrypt(plaintext + padding)
    return msg


# --- Caso 1 ---
plaintext= b'FURB'
cipher = Blowfish.new(key, Blowfish.MODE_ECB)
print('1.1: ' + str(criptografar(plaintext, cipher).hex()))
print('1.2: ' + str(len(criptografar(plaintext, cipher))))
# Tem oito, sendo 4 de preenchemento do bloco
print()

# --- Caso 2 ---
plaintext= b'COMPUTADOR'
cipher = Blowfish.new(key, Blowfish.MODE_ECB)
print('2.1: ' + str(criptografar(plaintext, cipher).hex()))
print('2.2: ' + str(len(criptografar(plaintext, cipher))))
# 10 do texto simples + 6 de preenchemento, pois é formado dois blocos com 8 bytes cada
print()

# --- Caso  3---
plaintext= b'SABONETE'
cipher = Blowfish.new(key, Blowfish.MODE_ECB)
print('3.1: ' + str(criptografar(plaintext, cipher).hex()))
print('3.2: ' + str(len(criptografar(plaintext, cipher))))
# 8 DO TEXTO SIMPLES mais 8 de preenchimento, é necessário um bloco de preenchimento, pois o ultimo digito deve sempre guardar a quantidade de bytes completados
print()

# --- Caso  4---
plaintext= b'SABONETESABONETESABONETE'
cipher = Blowfish.new(key, Blowfish.MODE_ECB)
print('4.1: ' + str(criptografar(plaintext, cipher).hex()))
print('4.2: ' + str(len(criptografar(plaintext, cipher))))
# 24 do texto simples mais 8 de preenchimento, é necessário um bloco de preenchimento, pois o ultimo digito deve sempre guardar a quantidade de bytes completados
print()

# --- Caso  5---
# --- Caso 1 ---
plaintext= b'FURB'
cipher = Blowfish.new(key, Blowfish.MODE_CBC)
print('5.1: ' + str(criptografar(plaintext, cipher).hex()))
print('5.2: ' + str(len(criptografar(plaintext, cipher))))

text = criptografar(plaintext, cipher)
cipher = Blowfish.new(key, Blowfish.MODE_CBC)
print(binascii.crc32(cipher.decrypt(text)))
#print('5.2: ' + str((decriptografar(plaintext, cipher))))
# Tem oito, sendo 4 de preenchemento do bloco
print()