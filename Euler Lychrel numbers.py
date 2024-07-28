


# Lychrel numbers
# https://projecteuler.net/problem=55
"""
Note I am looking for numbers that don't end up as palindromes

NOTE!
This is actually a bit easier than I had read.
I only need to reverse the numbers and add them, not every permuation
# I'm keeping this and trying again in a new file


Note one of the first, if not the first is 196



"""


import math
from itertools import permutations


# Creates all permuations of a number and returns them as a set
def permute(x):

    q = []
    for i in str(x):
        q.append(i)

    leng = len(str(x))
    y = permutations(q,leng)

    setter=set()

    for i in y:
        s = ''
        for j in i:
            s +=str(j)
        setter.add(str(s))

    return(setter)


def isPali(x):

    if len(x)%2==0:

        a = x[:len(x)//2]
        b = x[len(x) // 2:]
        r = b[::-1]
        if a==r:
            return True
        else:
            return False

    else:

        a = x[:len(x)//2]
        b = x[len(x) // 2+1:]
        r = b[::-1]

        if a==r:
            return True
        else:
            return False


# Takes in a set of number and creates all possible number combiinations from them.
# Also checks if any are palindromes
# Otherwise it sends it back to Permute to try again.
# May need another value to check how many times the numbers are being sent back
def combos(s):






for i in range(1,15):
    s = str(i)
    if isPali(s):
        print('pali',i)
    else:
        print(permute(i))















