



# Goldbach's Other Conjecture
# https://projecteuler.net/problem=46

import math

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

# 80000
lop = (prime_number_gen(10000))



def checkCon(x,lop):



    for a in lop:
        if a > x:
            break
        for b in range(1,x):

            sq = int(2*(b**2))
            if sq+a == x:
                print(x,a,b)

                return False
            elif sq+a > x:
                break
    return True













for i in range(3,100000,2):

    if i in lop:
        pass
    else:
        if(checkCon(i,lop)):
            print(i)
            break












