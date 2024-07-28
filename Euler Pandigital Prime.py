

# Pandigital Prime
# https://projecteuler.net/problem=41

import math

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





def pandigital(x):

    d = str(x)
    limit = len(str(x))

    numbers = [1,2,3,4,5,6,7,8,9]
    setter = set(numbers[:limit])


    for i in d:
        try:
            setter.remove(int(i))
        except:
            return False
    if len(setter) > 0:
        return False
    return True

# Note while this works a smarter idea would have been to go top down.
# I know the largest value it can possibly be, and I only need the largest one
for i in range(1,987654322):

    s = str(i)
    if '0' in s:
        pass
    elif isPrime(i):
        if pandigital(i):
            print(i)














