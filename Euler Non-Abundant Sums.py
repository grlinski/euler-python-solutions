

# Non-Abundant Sums
# https://projecteuler.net/problem=23


"""
Perfect Number
A number for which the sum of its divisors is exactly equal to the number
Ex 28
Has the divisors
1,2,4,7,14 added up = 28
Obviously ignore the number itself

Deficient Number
The sum a numbers divisors is less than the number itself.

Abundant Number
The sum of a numbers divisors is greater than the number itself
Ex 12
1,2,3,4,6 added = 16


All numbers over 28123 can be written as the sum of two abundant numbers
So that's my limit

Find the sum of all positive numbers which cannot be written as the sum of two abundant numbers.





"""



import math



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


def findAbundant(x):
    e = int(math.sqrt(x))+1
    total = 1

    for i in range(2,e):
        if x%i == 0:
            if (x//i == i):
                total+=i
            else:
                total += i
                total += (x//i)

    if total>x:
        return True
    else:
        return False





ab = []

total = 0
# Find Abundant Numbers
for i in range(2, 28123 ,1):
    break


    x = findAbundant(i)
    y = findDivs(i)

    print(i,x,sum(y))
    print(y)
    if x == True:
        ab.append(i)









# 28124


for i in range(1, 28124 ,1):


    x = findAbundant(i)
    if x == True:
        ab.append(i)


    top = len(ab)-1
    bot = 0
    adder = True

    while True:
        if bot > top:
            print('ans',i)
            break
        elif ab[top] + ab[bot] == i or ab[top]*2 == i or ab[bot]*2 ==i:
            adder = False
            print(i,ab[top],ab[bot])
            break
        elif ab[top] + ab[bot] > i:
            top-=1
        else:
            bot+=1
    if adder == True:
        total+=i




print(ab)
print(len(ab))
print(total)












