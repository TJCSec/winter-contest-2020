import random, math, gmpy2
from decimal import *

n = 595457894020630546875752966791042785294725759042100377835539686845934265329035124242207166150486143663858009765557142196309108219155835319774546238061639016124051685244334875530033869306105865675900166357091457569800409262510480946801318198579363576701896089680724855283100857901208860448303897452700474794861208073442299444227611506419869370362698060212058025019912935641109050965839298104856938979
e = 65537
c = 547975586649230680653956847616851301933989280525964620554420514800277102968478232787132938908346021393244440230544500639793280079552627384437255678899229180193846450997161893236221599877515583688415541909372710178559107513358754629894862537023962108857718493703756799890356444664054579748962051276457518620553609395367047655580109531678198908754687618991056640498450402757084829011330963831153435036

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

def findSD(n):
    s = 0
    d = n-1
    while d % 2 == 0:
        s = s + 1
        d = d//2
    return s,d

def checkBase(a,n):
    s,d = findSD(n)
    x = pow(a,d,n)
    if x == 1 or x == n-1:
        return "probable prime"
    else:
        for i in range(s-1):
            x = pow(x,2,n)
            if x == 1:
                return "composite"
            elif x == n-1:
                return "probable prime"
        return "composite"

def MSR(n,k):
    #Implements the Miller-Selfridge-Rabin test for primality
    for i in range(k):
        a = random.randint(2,n-2)
        if checkBase(a,n) == "composite":
            return "composite"
    return "probable prime"

def prime(n):
    smallPrimes = [2,3,5,7,11,13,17,19]

    for p in smallPrimes:
        if n == p:
            return True
        elif n % p == 0:
            return False

    if MSR(n,20) == "composite":
        return False
    else:
        return True

getcontext().prec = 1500
close_p = gmpy2.mpz(n)
gmpy2.get_context().precision=1500
close_p = int(gmpy2.sqrt(close_p))

while not prime(close_p) and not (Decimal(n)/Decimal(close_p)) % 1 == 0:
    close_p+=2

p = close_p
q = n//p
phi = (p-1) * (q-1)
gcd, d, b = egcd(e, phi)

m = pow(c,d,n)
flag = bytearray.fromhex(hex(m)[2:]).decode()
print(flag)



