
# Non-Bouncy Numbers
# https://projecteuler.net/problem=113

"""

Especially at larger values only certain numbers are not bouncy.

These will have tons of the same values.



Ranges and How Many Bouncy Numbers
100-1000
525

1000-10000
7800

10000-100000
86721

892002

8982135



ALternates between odd and even amounts
Odd amount of digits = odd amounts of bouncy



"""

def checkBouncy(x):
    s = str(x)
    rev = s[::-1]
    upwards = True
    downwards = True
    prev = 0
    #Upwards
    for i in s:
        if int(i) >= prev:
            pass
        else:
            upwards = False
            break
        prev = int(i)
    #Downward
    prev = 10
    for i in s:
        if int(i) <= prev:
            pass
        else:
            downwards = False
            break
        prev = int(i)
    if downwards==True and upwards==True:
        return True
    ans = downwards != upwards
    #print(upwards,downwards)
    return ans

counter = 0
for i in range(10000000,100000000):
    if not checkBouncy(i):
        counter+=1
print(counter)



















