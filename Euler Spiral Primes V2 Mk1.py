
# Spiral Primes V2 Mk1
# https://projecteuler.net/problem=58
"""
Complete Do Over

Take prime checker over here.
Maybe if truly needed the non-deterministic one.
"""

# Starting numbers and positions
import math


def is_prime(x):
    if x == 0 or x == 1 or x < 0:
        return False
    if x ==2:
        return True
    checker = 0
    for i in range(2,int(math.sqrt(x))+1):
        r = x%i
        if r == 0:
          checker +=1
    if checker > 0:
        return False
    else:
        return True


import random


# Where n is an odd integer to be tested for primality.
# Returns True or False for Primality.
# However this number is not guaranteed to be prime, just very high likelyhood
def millerRabin(n):
    # This is what I return if the number is probably prime
    # As in it passes the test k times.
    probablyPrime = True
    # I Skipped This Part
    # Just returned True or False

    # Fast Checks for Annoying Numbers
    passPrimes = [2, 3, 5, 7]
    autoFail = [0, 1, 4, 6, 8, 9]
    if n in passPrimes:
        return True
    if n in autoFail:
        return False

    d = n - 1
    s = 0
    # (2**s)*d == n-1
    # This needs to be true.

    while d % 2 == 0:
        # Bit Shift
        d >>= 1
        s += 1

    def trial_composite(a):
        x = pow(a, d, n)
        if x == 1:
            return False
        for i in range(s):
            if pow(a, (2 ** i) * d, n) == n - 1:
                return False
        return True

    # Trials is the parameter that determines accuracy of the test.
    # Basically how many random checks are done on the number.
    # There is always a chance of picking a number that gives false positive.
    # The more trials the more accurate but longer
    trials = 10

    for i in range(trials):
        a = random.randint(2, n - 1)
        if trial_composite(a):
            return False

    return True


counter = 0

cur = 1
prev = 0
prev2 = 0
step = 2
totalPrimes = 0
totalNumbers = 0

counterTen = 0
tenOfTen = 10

while True:

    if cur < 100000:
        if is_prime(cur):
            totalPrimes+=1
    else:
        if millerRabin(cur):
            totalPrimes+=1
    totalNumbers+=1
    if (totalPrimes/totalNumbers) < 0.1 and totalNumbers > 10:
        break

    if counterTen == tenOfTen:
        print(totalPrimes,totalNumbers)
        print(totalPrimes/totalNumbers)
        tenOfTen*=10
    prev2 = prev
    prev = cur
    cur = cur+step
    counterTen+=1
    counter+=1
    if counter==4:
        step+=2
        counter=0


print(cur,prev)
print(totalPrimes/totalNumbers)
print(cur-prev+1)
print(prev-prev2+1)












