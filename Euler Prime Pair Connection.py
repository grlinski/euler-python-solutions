
# Prime Pair Connection
# https://projecteuler.net/problem=134

import random



# p2 > p1
def endsWithP1DivP2(p1,p2):
    digits = set()
    for i in str(p1):
        digits.add(i)
    for i in str(p2):
        digits.add(i)

    numb = p2
    lengP1 = len(str(p1))
    total = p2
    while True:
        if p1 == 311:
            print(total)
        stotal = str(total)
        end = int(stotal[-lengP1:])
        #print(total)
        if end == p1:
            if total%p2 == 0:
                good = True
                for i in stotal:
                    if i in digits:
                        pass
                    else:
                        good = False
                if good == True:
                    return total
        total += p2







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
    trials = 3

    for i in range(trials):
        a = random.randint(2, n - 1)
        if trial_composite(a):
            return False

    return True

topmost = 10000
primes = []
for i in range(5,topmost+1):
    if millerRabin(i):
        primes.append(i)


total = 0
for i in range(0,len(primes)-1):
    p1 = primes[i]
    p2 = primes[i+1]

    s = (endsWithP1DivP2(p1,p2))
    total+=s
    print(p1, p2,s)
print(total)







