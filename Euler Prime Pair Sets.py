


# Prime Pair Sets
# https://projecteuler.net/problem=60



!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# I purposefully errored out this as it can and has crashed my computer


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

break


break


#from itertools import permutations,combinations
#import math


import time

# Note I removed 5 and 2

def prime_number_genSE(start,end):

    # For whatever reason this doesn't work unless start is 2 or greater
    # So may as well make start 2 as a minimum.
    if start < 2:
        start =2


    list_of_primes = []
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
            for i in range(2,len(list_of_primes)):
                if i > upto:
                    break
                if number%list_of_primes[i] == 0:
                    prime = False
                    break
        if prime == True:
            list_of_primes.append(number)

        number+=1


    return list_of_primes




def prime_number_gen(items):
    list_of_primes = [3]
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
            list_of_primes.append(number)
            counter += 1
            if len(list_of_primes)%10000 == 0:
                pass
                #print(counter)



        number+=1
    return list_of_primes




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





print(time.clock())


lop1 = (prime_number_genSE(1,10010))
print(time.clock())
lop2 = (prime_number_genSE(1,1000000))
print(time.clock())
print('end here')


print(len(lop1))
print(len(lop2))

lop3 = set(lop2)

print(time.clock())

print(time.clock())
print('end here')


y = list(x)
print(len(y))



dict = {}

limit = 1
counter = 1

list1 = []
set1 = set()

for i in x:
    break

    s1 = int(str(i[0])+str(i[1]))
    s2 = int(str(i[0])+str(i[2]))

    s3 = int(str(i[1]) + str(i[0]))
    s4 = int(str(i[1]) + str(i[2]))

    s5 = int(str(i[2]) + str(i[0]))
    s6 = int(str(i[2]) + str(i[1]))



    if is_prime(s1) and is_prime(s2) and is_prime(s3) and is_prime(s4) and is_prime(s5) and is_prime(s6):
        set1.add(i)
        list1.append(i)



print(time.clock())

fiver = set()

for i in set1:
    break
    for j in set1:
        a = set(i)
        b = set(j)
        newset = a.union(b)
        if len(newset) == 5:
            t = tuple(newset)
            fiver.add(t)

print(time.clock())

list1 = []
for i in fiver:
    break
    primer = True
    for j in i:
        list1.append(j)
    x = permutations(list1,2)
    for k in x:
        p = int(str(k[0])+str(k[0]))
        primer = is_prime(p)
        if primer == False:
            break
    if primer == True:
        print(i)






print(time.clock())