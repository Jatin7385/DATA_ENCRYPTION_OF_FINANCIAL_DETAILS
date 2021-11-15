import random
class RSA:
    def __init__(self):
        pass
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
def compute(a,m,n):
    y=1
    while(m>0):
        r=m%2
        if(r==1):
            y=(y*a)%n
        a = a*a % n
        m = m // 2
    return y
def encryption(n,e):
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
def decryption(n,d):
    M=[]
    C=input("Enter the Text to Decrypt:")
    a=C.split()
    for i in a:
        M.append(compute(int(i),d,n))
    print("Decrypted text is")
    for i in M:
        print(i)
while(5):
    p=int(input("Enter p:"))
    if(check_prime(p)==1):
        print("Invalid input!Enter Again")
    else:
        break
while(5):
    q=int(input("Enter q:"))
    if(check_prime(q)==1):
        print("Invalid input!Enter Again")
    else:
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
print("n is",n)
print("e is",e)
print("d is",d)
encryption(n,e)
decryption(n,d)