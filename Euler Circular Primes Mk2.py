

# Circular Primes
# https://projecteuler.net/problem=35

# I thought I needed all permuations, I just need rotations
# Look up the difference if need be.


import math

def isPrime(x):

    limit = int(math.sqrt(x))+1
    prime = True
    for i in range(2,limit):
        if x%i==0:
            prime = False
            break
    return prime


def rotations(x):
    y = str(x)

    q = []

    ender = len(y)

    s1 = y[0]
    s2 = y[1:]
    s3 = s2 + s1


    while ender!=0:
        q.append(int(s3))
        s1 = s3[0]
        s2 = s3[1:]
        s3 = s2+s1
        ender-=1

    return (isPrimeList(q))

# Same Idea as isPrime, but checks an entire list. Stops if it hits a non-prime value
def isPrimeList(x):



    for j in x:
        limit = int(math.sqrt(j))+1


        prime = True
        for i in range(2,limit):


            if j%i==0:
                prime = False
                return False
    return prime






# Skipping 2,3,5
total = 3



for i in range(6,1000000):

    s = str(i)
    if i%2 == 0:
        pass
    elif '5' in s or '0' in s or '2' in s or '4' in s or '6' in s or '8' in s:
        pass
    else:
        if isPrime(i):
            if(rotations(i)):
                print(i)
                total+=1

print(total)







