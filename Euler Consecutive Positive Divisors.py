
# Consecutive positive divisors
# https://projecteuler.net/problem=179
"""
Gives 1 more than the right answer
Luckily I guessed it would
986263
Right answer is:
986262



"""

import math



# Finds all Divisors of a Number, not including the number itself.
def findDivs(x):
    q = [1]
    e = int(math.sqrt(x))+1
    total = 1

    for i in range(2,e):
        if x%i == 0:
            if (x//i == i):
                total+=1
            else:
                total+=2
    return total

prev = -1
ans = 0
topmost = 10**7
cent = 0.01

percent = int(0.01*topmost)

for i in range(1,topmost):
    if i == percent:
        print(i,ans,cent*100)
        cent+=0.01
        percent = int(cent*topmost)

    cur = (findDivs(i))
    if cur==prev:
        ans+=1
    prev = cur

print(ans)









