




# Distinct primes factors Mk2
# Forgot to put in title Mk2
# https://projecteuler.net/problem=47
"""
Got it to work, luckily the first values it printed worked.
I could do a bit more but I'm lazy
For example I'm not sure but it is possible that in the data it outputs the first value could have non-distinct prime factors with the 3rd and 4th values
# And the same basic trend for non-adjacent values in the same sequence.
# This is because I'm only comparing the side by side values in a sequence, not every value by every value in the sequence.
# Not sure if it actually would make a difference, since I got the answer correct already I guess doesn't actually matter.
# Mostly just a note In case something like this comes up again I can avoid this problem





"""



from itertools import combinations


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


# Finds all Divisors of a Number, not including the number itself.
def findDivs(x):
    q = []
    e = int(math.sqrt(x))+1

    for i in range(2,e):
        if x%i == 0:
            if (x//i == i):
                q.append(i)
            else:
                q.append(i)
                q.append(x//i)

    return q






# 80000
lop = (prime_number_gen(10000))
lopset = set(lop)

prev = 0
total =0

prevdiv = set()

h = []

lodp = []

for i in range(2,1000000):
    divs = set(findDivs(i))
    sim = lopset&divs

    if len(prevdiv) ==0:
        pass
    else:
        hp =(sim - prevdiv)
        if len(hp) > 3:

            holder = [i,hp]
            lodp.append(holder)
            #print(i,hp)
    prev = i
    prevdiv = sim



seq = []
lodp.append([0,0])

store = False
con = False
holder = []
ans = []
for i in range(len(lodp)-1):
    a=lodp[i][0]
    b=lodp[i+1][0]
    if b-a == 1:
        holder.append(a)
        store=True
        con = True
    elif store == True:
        holder.append(a)
        #print(holder)
        if len(holder) > 3:
            ans.append(holder)
        store = False
        holder= []
    else:
        store = False
        holder = []



print(ans)


"""


    if len(sim) < 4:
        pass
    else:
        if i-prev == 1:
            print(prev,prevdiv)
            print(i,sim)

    prev = i
    prevdiv = sim


"""














