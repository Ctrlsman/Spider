from Crypto.Cipher import AES
from binascii import b2a_hex

key123 = 'G*~^xV&+cHU@!*90'
IV456 = 'cc%-+]zD!$#qqffg'
aes = AES.new(key123, AES.MODE_CBC, IV456)
zhuge_userid_list = []
device_id = '1|1510418038|RYG9dbe5fc94c8f400facc14f18736f5ed3'
hash_data = b2a_hex(aes.encrypt(device_id))
# hash_data = ''.join("%02x" % ord(b) for b in aes.encrypt(device_id))
print(hash_data.decode('utf-8'))