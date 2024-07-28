
# Prime Summations
# https://projecteuler.net/problem=77


import random


def millerRabin(n):

    probablyPrime = True
    passPrimes = [2, 3, 5, 7]
    autoFail = [0, 1, 4, 6, 8, 9]
    if n in passPrimes:
        return True
    if n in autoFail:
        return False

    d = n - 1
    s = 0
    while d % 2 == 0:
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

    trials = 10

    for i in range(trials):
        a = random.randint(2, n - 1)
        if trial_composite(a):
            return False
    return True









