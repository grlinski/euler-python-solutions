


# Distinct primes factors
# https://projecteuler.net/problem=47



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
    q = [1]
    e = int(math.sqrt(x))+1

    for i in range(2,e):
        if x%i == 0:
            if (x//i == i):
                q.append(i)
            else:
                q.append(i)
                q.append(x//i)

    return q






def DPF(x,y):


    z = x
    div = list(y)*3
    timesdivided = 0
    setter = set()

    for i in range(1,len(div)+1):
        x = combinations(div,i)
        for j in x:
            x = z
            add = True
            for k in j:
                if k!=None and x%k == 0:
                    x = x//k
                elif k == None or x%k!=0:
                    add = False
                    break
            if x == 1 and add== True:
                setter.add(j)

    lastset = set()
    for i in setter:
        j = tuple(sorted(list(i)))
        lastset.add(j)


    #print(lastset)

    if len(lastset)!=0:

        return True
    else:
        return False












# 80000
lop = (prime_number_gen(1000))
lopset = set(lop)

prev = 0
total =0

h = []
for i in range(2,1000):
    divs = set(findDivs(i))
    sim = lopset&divs



    if len(sim) ==0:
        pass
    else:
        if DPF(i,sim):
            if i-prev == 1:
                h.append(i)
                total+=1

            else:

                total=0


    prev = i



print(total)
total =0
maxi = 0
for i in range(1,len(h)-1):
    a = h[i-1]
    b = h[i]

    if abs(b-a)==1:
        total+=1
        maxi = max(maxi,total)
    else:
        total = 0
    if total == 4:
        print(b,a)


print(maxi)
for i in h:
    print(i)






