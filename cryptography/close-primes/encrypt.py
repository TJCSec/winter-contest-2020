import random, os, sys

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

def findPrime(maxN):
    while True:
        m = random.randint(1,maxN//2)
        n = 2*m+1
        if prime(n):
            return n



p = findPrime(10**200)
q = p+2
for i in range(10):
    while not prime(q): q+=2

n = p*q
phi = (p-1) * (q-1)
e = 65537
gcd, d, b = egcd(e, phi)

message = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flag.txt'), 'r').read()
m = int('0x' + ''.join([hex(i)[2:] for i in message.encode('ascii')]), 16)
c = m ** e % n

print('n = {}'.format(n))
print('e = {}'.format(e))
print('c = {}'.format(c))
