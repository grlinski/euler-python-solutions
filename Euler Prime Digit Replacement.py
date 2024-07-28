
# Prime Digit Replacement
# https://projecteuler.net/problem=51


# Last Digit of the number must be 1,3,7 or 9


"""
Finishing Notes
Alright so I opted for an easier solution, which luckily enough worked.
Technically it gave me a list of possible solutions at the end and I just worked through them to get the right answer

And no the answer isn't 109, or 111109. Since apparantly replacing 000 doesn't count.

Unfortunately I never was able to create the consensus sequences as I wanted to.
Maybe next time.

Also maybe create a prime list generator that is able to start at a certain number.
I tried messing with the normal one and it became screwed up.


Note I think the answer is 171917
Prime family of *7*9*7 7 [171917, 272927, 373937, 575957, 676967, 777977, 878987]
There should be another prime in that family.

Actually it was probably 121313


"""







"""
Example of Prime Families
These Two Primes
7368659
7368689

Have the same digits and can be a prime family:
73686*9

Note the first 6 digit prime is 100003
It is the 9592nd prime


100003
9562
Useful for faster generation of primes.


"""




from itertools import count
import math
import random

def is_prime(x):
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




def prime_number_gen(items):
    list_of_primes = [2,3,5]
    # 2 and 3 added since they are a pain in the ass
    counter = 3
    number = 7
    prime = True
    # Main Loop for Prime Gen
    # Goes until our counter of primes hits items
    while counter != items:

        prime = True
        # Quick check if prime
        # The number has to be either 6n+1 or 6n-1,
        # Note I had a problem before with using or instead of and.
        # It only needs to be one or the other, not nessicarily both.
        if (number+1)%6 != 0 and (number-1)%6 != 0:
            prime = False

        elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
            prime = False
            # If all those fail check if it is divisible by any of the primes in the list
        else:
            # If the potential divisor is greater than the square root of the number it ends
            # This is one of the most important parts
            # Makes it much more efficient
            upto = int(math.sqrt(number))
            for i in range(2,len(list_of_primes)):
                if i > upto:
                    break
                if number%list_of_primes[i] == 0:
                    prime = False
                    break
        if prime == True:
            #print(number)
            list_of_primes.append(number)
            counter += 1
            if len(list_of_primes)%10000 == 0:
                pass
                #print(counter)



        number+=1
    return list_of_primes


lop = (prime_number_gen(100000))





def prime_family(x,d):

    # Preset Permuations
    # * = Skip/Turn into wildcard, k == keep. Only goes up to 4 of a given number.
    perm = ['*','**','k*','*k','***','**k','*k*','k**','k*k','*kk','kk*','kkk','****','***k','**k*','*k**','k***','**kk','*kk*','kk**','*k*k','k**k','k*k*','*kkk','kk*k','k*kk','kkk*','kkkk']
    ansset = set()

    s1 =str(x)
    endval = s1[-1]

    s1 = s1[:-1]
    l = []
    set1 = set()


    for i in s1:
        l.append(i)
        set1.add(i)

    freq = []
    for i in range(0,10):
        w = l.count(str(i))
        freq.append(int(w))

    ansset = set()
    for i in range(0,len(freq)):
        if freq[i] !=0:
            a = str(i)
            s2 = s1.replace(a, '*')
            ansset.add(s2)
    anslist = []

    trueanset = set()

    for i in ansset:
        q = i+endval
        trueanset.add(q)
        if q in d:
            d[q]+=1
        else:
            d[q]=1


    return d,trueanset





d = {}
g = set()

for x in lop:

    if len(str(x)) == 6:
        d,ns = prime_family(x,d)
        for i in ns:
            g.add(i)


g6 = []

for i in g:
    if d[i] > 5:
        print(d[i],i)
        g6.append(i)



for i in g6:
    count = 0
    pl = []
    for j in range(0,9):
        ns = i.replace('*',str(j))
        x = int(ns)
        if is_prime(x):
            pl.append(x)
            count+=1
    print(i,count,pl)


print(is_prime(111109))








































