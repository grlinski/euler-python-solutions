
# Spiral Primes
# https://projecteuler.net/problem=58

"""
Probably best to make a new file
Just so I don't destroy anything in this one.

So as far as I know it works so far.
One thing to do however is skip over d list
Everything in d list is not prime, I can just add it to the non prime total
Second is to keep track of how large the spiral gets.
Actually this may be where d comes in handy.
Whenever d is hit that is the creation of a new full square, with +2 sidelength

Also can get rid of any other lists where I store values,
These are just to make sure the program works,
I could even just store the primes there.

Gone up to:
100000000
Only hit about 17%

2nd
500000000
%

"""





import math


# Lists of Diagonals, Top Right going CCW to Bottom Right Diagonal, However I'm just going to start them with a-d then d for diagonal
adtr = [13,31,57]
bdtl = [5]
cdbl = [7]
ddbr = []


# a has the only unusual pattern, all other have a difference that increases by 8 each time




def isPrime(x):
    if x == 0 or x == 1 or x < 0:
        return False
    if x ==2:
        return True
    checker = 0
    for i in range(2,int(math.sqrt(x))):
        r = x%i
        if r == 0:
          checker +=1
    if checker > 0:
        return False
    else:
        return True

adif = 42
bdif = 20
cdif = 22
ddif = 16


a = 91
b = 17
c = 21
d = 9

# I already have a few in the lists.
# Later I can remove the lists
primes = 4

# Not prime numbers that should already be in there are
# 1?, 9,
notprime = 2

sidelength = 1


for i in range(2,500000000):

    if i == a:
        adtr.append(i)
        if isPrime(i):
            primes+=1
        else:
            notprime+=1

        a=a+ adif
        adif+=8
    elif i == b:
        if isPrime(i):
            primes+=1
        else:
            notprime+=1


        bdtl.append(i)

        b =b+ bdif
        bdif+=8

    elif i == c:
        if isPrime(i):
            primes+=1
        else:
            notprime+=1
        cdbl.append(i)

        c =c+ cdif
        cdif+=8

    elif i == d:
        if isPrime(i):
            primes+=1
        else:
            notprime+=1
        ddbr.append(i)

        d =d+ ddif
        ddif+=8
        sidelength+=2

    if (primes/(notprime+primes)*100) < 10:
        print(primes/(notprime+primes)*100)
        print(i)




#print(adtr)
#print(bdtl)
#print(cdbl)
#print(ddbr)

print(primes)
print(notprime)
print(primes/(notprime+primes)*100)
print(sidelength)



"""


TRD
Starts out weird, then just add 8, likely the same for other patterns
1
3 2
13 10 8
31 20 10
57 26 6
91 34 8
133 42 8
183 50 8
241 58 8
307 66 8
381 74 8


TLD
1
5 4
17 12 8
37 20 8
65 28 8
101 36 8

BLD
1
7 6
21 14 8
43 22 8
73
111
157



BRD, Note These are Squares
1
9 8 
25 16 8
49 24 8
81






"""








