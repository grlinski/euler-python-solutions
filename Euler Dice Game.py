

import random
import time

peter = [1,2,3,4]
colin = [1,2,3,4,5,6]



d = 0
pw = 0
cw = 0


t =1


for j in range(0,100000000):
    p = 0
    c = 0
    for i in range(0, 9):
        x = random.randint(1, 4)
        p += x

    for i in range(0, 4):
        x = random.randint(1, 6)
        c += x

    if c > p:
        cw+=1
    elif p > c:
        pw+=1
    elif p==c:
        d+=1
    else:
        print(p,c)

    if t == j:
        print(t)
        print(1 - (cw / pw))
        print(time.clock())
        t = t*10

print(pw,cw,d)

print(cw/pw)
print(1-(cw/pw))






