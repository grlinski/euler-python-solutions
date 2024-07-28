

# Largest integer divisible by two primes

# https://projecteuler.net/problem=347

"""

Could split lists,
Meaning when generating primes, everything that is prime goes into one list,
Everything else goes into another list




"""



import math
import time

def prime_number_genSE(start,end):

    # For whatever reason this doesn't work unless start is 2 or greater
    # So may as well make start 2 as a minimum.
    if start < 2:
        start =2


    list_of_primes = []
    nonprime = []
    # 2 and 3 added since they are a pain in the ass


    prime = True
    # Main Loop for Prime Gen
    # Goes until our counter of primes hits items

    number = start

    # Manually Add Annoying Numbers
    if number < 3:
        list_of_primes.append(2)
    if number < 4:
        list_of_primes.append(3)
    if number < 6:
        list_of_primes.append(5)



    while number != end:

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
            for i in range(2, number):
                if i > upto:
                    break
                if number%i == 0:
                    prime = False
                    break



        if prime == True:
            if number < 5000000:
                list_of_primes.append(number)
        else:
            nonprime.append(number)

        number+=1

    nonprime = nonprime[4:]
    nonprime.insert(0,4)
    return list_of_primes,nonprime




t1 = time.time()
print(t1)
primes,nonprime = prime_number_genSE(2,10000001)
print(primes)
print(primes[0:10])
print(nonprime[0:10])


t2 = time.time()
# Prime Generation takes about 75 seconds
# New system up to 1000001 takes 201 seconds,
# I can skip any prime over 4999999
# Which is now done, so the list lengths won't add up properly

print(t2-t1)


print(len(nonprime)+len(primes)+1)
print('ender')


total = 0

used = []
checker = 10


tb = time.time()


numb = 0

for i in range(10000000,1,-1):
    numb+=1

    amt = 0
    q = []
    if numb == checker:
        tn = time.time()
        print(i, tn - tb)
        print(len(used))
        tb = tn
        checker = checker * 10


    for j in primes:
        if i%j == 0:
            amt+=1
            q.append(j)
        if amt >2:
            break
        if j >= i:
            break
    if amt == 2:
        set1 = set(q)
        if set1 not in used:
            #print(i)
            #print(q)
            total+=i
            used.append(set1)
t3 = time.time()

print(t3-t2)
print(total)
















