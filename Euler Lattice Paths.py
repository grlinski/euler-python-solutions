
# Lattice Paths
# https://projecteuler.net/problem=15


import itertools
import time
from itertools import permutations



#directions = ['r','r','l','l']

d = ['r','r','r','r','r','r','r','r','r','r','l','l','l','l','l','l','l','l','l','l']
e = ['l','l','l','l','l','l','l','l','l','l','r','r','r','r','r','r','r','r','r','r']

# Instead Going to do Pascals Triangle
# Only care for the middle value every second row
# https://en.wikipedia.org/wiki/Pascal's_triangle


q = [1]
s= []

midval = 1
for j in range(1,41):
    s = [0]*(len(q)+1)

    for i in range(0,len(s)):
        if i == 0:
            s[i]=q[0]
        elif i == len(s)-1:
            s[i]=q[-1]
        else:
            s[i] = q[i]+q[i-1]

    q = s
    if j%2==0:
        print(q[midval])
        midval+=1






















