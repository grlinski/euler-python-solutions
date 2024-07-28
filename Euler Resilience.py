
# Resilience
# https://projecteuler.net/problem=243
"""
Probably just some highly divisible number.

2x3x5x7x11x13

232792560
2520


Other problems similar
problem 47 distinct prime factors



Instead of Finding GCD, just find if any number divides both equally.
have a list of number, basically the list of primes and divide each number by those.



Instead create highly divisible numbers.
Check up to which prime numbers they aren't divisble by.
example
2x3x5 = 30
First prime it is not divisible by is 7
And as far as I can tell 30 should be divisible by everything less than itself except primes.


So list of primes, probably via miller rabin
Small list of candidate numbers created by prime numbers, maybe up to 100 primes.
Find the first prime the candidate is not divisible by.
Then count from there every prime that is less than the candidate.






"""

import random

import time



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
    trials = 5

    for i in range(trials):
        a = random.randint(2, n - 1)
        if trial_composite(a):
            return False

    return True



def GCD(a,b):

    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
    return a

start = time.time()
bound = 15499/94744
topmost = 10000000
tencent = 20


now = time.time()
print((now-start)/60)

primes = [2,3,5,7]
primeTop  = 1000

for i in range(9,primeTop,2):
    if millerRabin(i):
        primes.append(i)

now = time.time()
print((now-start)/60)
print('Primes Done',len(primes))
candidates = []
cand = 1
for i in range(0,100):
    cand = primes[i]*cand
    candidates.append(cand)


for i in candidates:
    print(i)





"""
highest number I've checked
200560490130
7420738134810
Which is 2x3...x31 = 200560490130
304250263527210
"""
