#from Algorithms.AES import AES

#Assigning Algorithms Numbers :-
#0 -> RSA
#1 -> AES
#2 -> Twofish
#3 -> TDES
#4 -> BLOWFISH 

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
        for i in C:
            print(i)

keyrecieved = input("Enter the key recieved by the reciever side : ")
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

# elif(algonumber == 1):
#     aes = AES()
#     aes.Encrypt(key)