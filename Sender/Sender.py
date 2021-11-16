import sys
sys.path.append("c:\\users\\jatin dhall\\anaconda3\\lib\\site-packages")
from Crypto.Cipher import AES
from base64 import b64encode
from Crypto import Random
from Crypto.Util.Padding import pad
from binascii import b2a_hex
import csv
#from Algorithms.AES import AES

#Assigning Algorithms Numbers :-
#0 -> RSA
#1 -> AES
#2 -> Twofish
#3 -> TDES
#4 -> BLOWFISH 

def AESEncrypt(key):
    plain_text = input("Enter the message : ")
    print("The key k is: ", key)
    key = key.encode()
    # Generate a non-repeatable key vector with a length
    # equal to the size of the AES block
    iv = Random.new().read(AES.block_size)
    # Use key and iv to initialize AES object, use MODE_CFB mode
    mycipher = AES.new(key, AES.MODE_CFB, iv)

    ciphertext = mycipher.encrypt(pad(plain_text.encode(),AES.block_size))
    #print("iv : ",ciphertext[:16])
    print("The encrypted data is:", b64encode(ciphertext).decode('utf-8'))
    print("The iv is:", b64encode(iv).decode('utf-8'))
    cipher = [b64encode(ciphertext).decode('utf-8'),b64encode(iv).decode('utf-8')]

    with open('ciphertext.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        # write the data(cipher,iv)
        writer.writerow(cipher)

        f.close()


def compute(a,m,n):
    y=1
    while(m>0):
        r=m%2
        if(r==1):
            y=(y*a)%n
        a = a*a % n
        m = m // 2
    return y

def RSAencryption(n,e):
    M=int(input("Enter Text to encrypt:"))
    d1=M
    if  M < n:
        C=compute(M,e,n)
        print("Encrypted text is:",C)
    else:
        f=0
        a=[]
        C=[]
        while d1>0:
            mod=d1%100
            a.insert(f,mod)
            f=f+1
            d1= d1//100
        a.reverse()
        for i in a:
            C.append(compute(i,e,n))
        print("Encrypted text is")
        cipher = []
        for i in C:
            print(i)
            cipher.append(i)
        with open('ciphertext.csv', 'w', encoding='UTF8') as f:
            writer = csv.writer(f)

            # write the data(cipher,iv)
            writer.writerow(cipher)

            f.close()


with open("C:\\Users\\Jatin Dhall\\Desktop\\Desktop File\\VIT\\VIT\\SEM 3\\Cyber Security\\PROJECT\\PROJECT\\Reciever\\key.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if(len(row) == 0):
            break
        keyrecieved = row[0]
    csv_file.close()

#keyrecieved = input("Enter the key recieved by the reciever side : ")
input("Please press enter once the key is generated from the receiver side : ")
print(keyrecieved)
print("Algo Number : ",keyrecieved[0])

algonumber = keyrecieved[0]
key = keyrecieved[1:]
print(algonumber)
print(key)

#Currently only for the 2 algorithms we have implemented
if(algonumber == '0'):
    nsize = int(key[0])
    n = key[1:nsize+1]
    esize = int(key[nsize+1])
    e = key[nsize+2:]
    print("n = " , n)
    print("e = ",e)
    RSAencryption(int(n),int(e))

elif(algonumber == '1'):
    # aes = AES()
    # aes.Encrypt(key)
    AESEncrypt(key)