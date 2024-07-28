

# Pandigital Prime Sets
# https://projecteuler.net/problem=118

from itertools import permutations, combinations_with_replacement
import math
import time,random



def listToString(list1):

    (list1.sort())
    s = ''
    for i in list1:
        s+=str(i)
        s+=' '
    return s



def sumCombos(x):
    total = 0
    for i in x:
        y = int(i)
        total+=y
    return total


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


items = []

def createNumbers(perm,part):
    list1 = []
    s = ''
    counter = 0
    partPos = 0
    length = part[partPos]
    for i in perm:
        s+=str(i)
        counter+=1
        length = part[partPos]
        if counter == length:
            list1.append(int(s))
            s =''
            counter = 0
            partPos+=1


    for i in list1:
        if not millerRabin(i):
            return False,list1

    return True,list1




numb = [1,2,3,4,5,6,7,8,9]

parts = [[1,1]]
nineParts = [1,2,3,4,5,6,7,8,9]

#Cannot be Alone 1 4 6 8 9'
#Cannot be ends 2 4 5 6 8
counter = 0
partitions = []
for i in range(1,10):
    x = combinations_with_replacement(nineParts,i)
    for j in x:
        if(sumCombos(j) ==9):
            counter+=1
            partitions.append(j)

x = permutations(numb,9)

amount = 10886400


counter = 0
tenPercent = .1


set1 = set()
total = 0




for perm in x:
    for part in partitions:
        good, list1 = createNumbers(perm,part)

        if good and list1 !=None:
            string1 = listToString(list1)
            set1.add(string1)
            total+=1
        counter+=1
        if counter == int(amount*tenPercent):
            print(counter,total)
            tenPercent+=0.1



print(total)
print(len(set1))





