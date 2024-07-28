

# Truncatable Primes
# https://projecteuler.net/problem=37

import math



def trunk(x):
    s1 = str(x)
    s2 = s1[::-1]

    left = ''
    right = ''

    prime = True

    for i in range(1,len(s1)):
        left = s1[i:]

        if not isPrime(int(left)):
            return False




    for i in range(len(s1),0,-1):
        right = s1[:i]
        #print(right)
        if not isPrime(int(right)):
            return False

    return True







def isPrime(x):
    if x==0 or x==1 or x==-1:
        return False
    limit = int(math.sqrt(x))+1
    prime = True
    for i in range(2,limit):
        if x%i==0:
            prime = False
            break
    return prime





eleven = 11
total=0

for i in range(10,10000000):
    s = str(i)

    if eleven == 0:
        break

    if s[-1] == '2' or s[-1] == '5' or s[-1] == '1' or s[0] == '1':
        pass
    elif '4' in s or '6' in s or '8' in s:
        pass
    else:
        if isPrime(i):

            if trunk(i):
                print(i)
                total+=i
                eleven-=1



print(total)










