import sys
sys.path.append("c:\\users\\jatin dhall\\anaconda3\\lib\\site-packages")
from Crypto.Cipher import AES
from Crypto import Random
from binascii import b2a_hex
import sys

class AES_ENCRYPTION:
    def __init__(self):
        # get the plaintext
        self.plain_text = input("Enter the message : ")
        self.Encrypt(b'this is a 16 key')

    def Encrypt(self,key):
        print("The key k is: ", key)
        # Generate a non-repeatable key vector with a length
        # equal to the size of the AES block
        self.iv = Random.new().read(AES.block_size)
        # Use key and iv to initialize AES object, use MODE_CFB mode
        self.mycipher = AES.new(key, AES.MODE_CFB, self.iv)

        # Add iv (key vector) to the beginning of the encrypted ciphertext
        # and transmit it together
        self.ciphertext = self.iv + self.mycipher.encrypt(self.plain_text.encode())
        print("The encrypted data is: ", b2a_hex(self.ciphertext)[16:])


# The key length must be 16 (AES-128), 24 (AES-192), or 32 (AES-256) Bytes.
# key = b'this is a 16 key'



# # To decrypt, use key and iv to generate a new AES object
# mydecrypt = AES.new(key, AES.MODE_CFB, ciphertext[:16])

# # Use the newly generated AES object to decrypt the encrypted ciphertext
# decrypttext = mydecrypt.decrypt(ciphertext[16:])

# # output
# file_out = open("encrypted.bin", "wb")
# file_out.write(ciphertext[16:])
# file_out.close()

# print("The key k is: ", key)
# print("iv is: ", b2a_hex(ciphertext)[:16])
# print("The decrypted data is: ", decrypttext.decode())

aes = AES_ENCRYPTION()