
# Prime Cube Partnership
# https://projecteuler.net/problem=131
"""
Most important part is putting bounds on n?
But how?
So n only increased by 1 to maybe 10 at most between answers
So bounding it was fairly easy
173






"""



import random


def checkIfCube(x):
    return round(x ** (1 / 3)) ** 3 == x


def digitalSum(x):
    pass

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

def formula(p,n):
    x = (n**3) + (n**2)*p
    return x


topmost = 1000000
#topmost = 10000



primes = [2,3,5,7]
cubes = []
for i in range(8,topmost):
    if millerRabin(i) == True:
        primes.append(i)



allowance = 20
previous = 1
total = 0
for p in primes:
    for j in range(previous,previous+allowance):
        n = j*j*j
        form = formula(p,n)
        if checkIfCube(form):
            print(p,n,j,form)
            allowance+=1
            previous = j
            total+=1
print(total)




"""
78498 primes under 1 million.

Prime CubeofInteger Integer and Cube
Note that each n is a cube.
7 1 1 8
19 8 2 1728
37 27 3 46656
61 64 4 512000
127 216 6 16003008
271 729 9 531441000
331 1000 10 1331000000
397 1331 11 3061257408
547 2197 13 13244763896
631 2744 14 25412184000
919 4913 17 140770302408
1657 12167 23 2046448129536
1801 13824 24 2985984000000
1951 15625 25 4291015625000




"""







