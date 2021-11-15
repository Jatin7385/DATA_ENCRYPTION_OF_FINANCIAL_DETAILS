import random
import sys
sys.path.append("c:\\users\\jatin dhall\\anaconda3\\lib\\site-packages")
from Crypto.Cipher import AES
from Crypto import Random
from binascii import b2a_hex

#Assigning Algorithms Numbers :-
#0 -> RSA
#1 -> AES
#2 -> Twofish
#3 -> TDES
#4 -> BLOWFISH 

def RSAdecryption(n,d):
    M=[]
    C=input("Enter the Text to Decrypt:")
    a=C.split()
    for i in a:
        M.append(compute(int(i),d,n))
    print("Decrypted text is :-")
    plaintext = ""
    for i in M:
        plaintext += str(i)
    print(plaintext)

def compute(a,m,n):
    y=1
    while(m>0):
        r=m%2
        if(r==1):
            y=(y*a)%n
        a = a*a % n
        m = m // 2
    return y

def AESdecryption(key):
    key = key.encode()
    ciphertext = input("Enter the ciphertext generated : ")
    # iv = input("Enter the iv generated : ")
    ciphertext = ciphertext.encode()
    # iv = iv.encode()
    print(ciphertext)
    # To decrypt, use key and iv to generate a new AES object
    mydecrypt = AES.new(key, AES.MODE_CFB, ciphertext[:16])

    # Use the newly generated AES object to decrypt the encrypted ciphertext
    decrypttext = mydecrypt.decrypt(ciphertext[16:])

    print("iv is: ", b2a_hex(ciphertext)[:16])
    print("The decrypted data is: ", decrypttext.decode())

def assymetricfinalkey(res):
    n = str(res[0])
    e = str(res[1])
    nsize = len(n)
    esize = len(e)
    print("ASSYMETRIC : ",n,e,nsize,esize)
    key = str(nsize) + n + str(esize) + e
    print("n = ",n)
    print("e = ",e)
    return key


def  randomize():
    rand=random.randint(40,4000)
    return (rand%2) #Should be %5 but for now we have implemented only 2 algorithms so %2

def symmetrickeygen():
    c=""
    for i in range(0,16):
        a=(random.randint(0,9))
        b=str(a)
        c=c+b
    return c

def check_prime(n):
	for i in range(2,n):
		if(n%i==0):
			return 1
	return 0
def gcd(a,b):
    while(1):
        temp=a%b
        if temp==0:
            return b
        a=b
        b=temp
def asymmetric():
    while(5):
        p=random.randint(1,1000)
        while(check_prime(p)==1):
            p=p+1
        break
    while(5):
        q=random.randint(1,1000)
        while(check_prime(q)==1):
            q=q+1
        break
    n=p*q
    phi_n=(p-1)*(q-1)
    while(5): 
        e=random.randint(2,n-1)
        if(gcd(e,phi_n)==1):
            break
    k=0
    while((1+(k*phi_n))%e!=0):
        	k+=1
    d=(1+(k*phi_n))//e

    res = [n,e,d]
    print("p = ",p)
    print("q = ",q)
    return res
    # print("n is",n)
    # print("e is",e)
    # print("d is",d)
    

algonumber = randomize()
if algonumber == 0: #Meaning the algorithm is RSA(Assymetric)
    key = str(algonumber)
    res = asymmetric()
    key += assymetricfinalkey(res)
    d = res[2]
    n = res[0]
    print("Assymetric Key : ",key)
    print("Algo Number : ",algonumber)

    print("DECRYPTION OF RSA")
    RSAdecryption(int(n),int(d))

    
else:
    key = str(algonumber)
    key += str(symmetrickeygen())
    print("Symmetric Key : ",key)
    print("AlgoNumber : ",algonumber)

    if algonumber == 1:
        AESdecryption(key[1:])


# for i in range(0,64):
#     print(symmetrickeygen())
# print("random",randomize())
# asymmetric()