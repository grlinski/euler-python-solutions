

# Circular Primes
# https://projecteuler.net/problem=35

import sympy
from sympy.utilities.iterables import multiset_permutations

import math
from itertools import permutations



def isPrime(x):

    limit = int(math.sqrt(x))+1
    prime = True
    for i in range(2,limit):
        if x%i==0:
            prime = False
            break
    return prime



def isPrimeSet(setter):
    prime = True
    for x in setter:
        y = int(x)
        limit = int(math.sqrt(y))+1
        for i in range(2,limit):
            if y%i==0:
                prime = False
                break
    return prime



def permute(x):
    q = []
    s = str(x)
    for i in range(0,len(s)):
        y = s[i]
        q.append(y)

    setter = set()
    per = permutations(q,len(s))
    for i in per:
        j = ''.join(i)
        setter.add(j)
    print(setter)
    return isPrimeSet(setter)









# Skipping 2,3,5
total = 3



for i in range(6,1):

    s = str(i)
    if i%2 == 0:
        pass
    elif '5' in s or '0' in s or '2' in s or '4' in s or '6' in s or '8' in s:
        pass
    else:
        if isPrime(i):
            k = permute(x)

            if k:
                total+=1




print(permute(197))








