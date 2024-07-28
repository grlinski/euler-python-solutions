
# Palidromic Sums
# https://projecteuler.net/problem=125
"""
Answer
2906969179


Fairly easy
Just need to narrow confines and ranges of numbers.





"""

import math, time


def checkPalindrome(x):
    s = str(x)
    rev = s[::-1]
    if s == rev:
        return True
    else:
        return False



def createAllCombos(list1,topmost):
    set1 = set()

    for i in range(0,len(list1)):
        x = list1[i]
        total = x
        for j in range(i+1,len(list1)):
            y = list1[j]
            total+=y
            if total >= topmost:
                break
            set1.add(total)
    return set1








squares = []
topmost = 10**8
count = 1
while True:

    x = count**2
    if x >= topmost:
        break
    squares.append(x)
    count+=1

if 0 in squares:
    squares.remove(0)

palidromes = []


print('Create All Combos Start')


canBeMade = createAllCombos(squares,topmost)
total = 0
palidromes = []
for i in canBeMade:
    if checkPalindrome(i):
        palidromes.append(i)


for i in palidromes:
    print(i)
    total+=i
print(total)




"""
19999
10000
"""

