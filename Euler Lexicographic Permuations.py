
# Lexicographic permutations
# https://projecteuler.net/problem=24


import itertools

from itertools import permutations

a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0


num = ['0','1','2','3','4','5','6','7','8','9']


#for i in range(0,1000000):

x = (permutations(num,10))
total = 1
for i in x:

    if total == 1000000:
        print(i)
    total += 1












