

# Quadratic Primes
# https://projecteuler.net/problem=27

import math


n = 0
a = 999
b = 1000

def isPrime(x):
    if x==0 or x==1 or x==-1:
        return False
    limit = int(math.sqrt(x))+1
    prime = True
    for i in range(2,limit):
        if x%i==0:
            prime = False
            break
    return prime


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
            list_of_primes.append(number)
            counter += 1
            if len(list_of_primes)%10000 == 0:
                pass
                #print(counter)



        number+=1
    return list_of_primes

# List of Primes
lop = (prime_number_gen(20000))

h = 0

# This function will take in the values of a,b and a list of primes
# Staring at n=1, since I already I know 0 leads to a prime number I'll check if the subsequent numbers are prime.
# Are the primes in order?
def checkPrimes(a,b,lop):
    # Since n=0 is prime
    total = 1
    n=1
    while True:
        x = (n**2)+(n*a)+b
        if x in lop:
            total += 1
        else:
            break

        n+=1
    return total



maxi = 0
tprimes = 0
while True:

    if a == -1000:
        a = 999
        b-=1

    if b == 0:
        break

    num = n**2 + (a*n) + b
    if(isPrime(num)):
        tprimes = checkPrimes(a,b,lop)
        if tprimes > maxi:
            maxi = tprimes
            print('A B T', a,b,maxi)
    a-=1
    h+=1




print(h)



















