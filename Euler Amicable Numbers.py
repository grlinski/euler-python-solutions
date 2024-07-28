

# Amicable Numbers
# https://projecteuler.net/problem=21



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



total = 0

for i in range(1,10000):
    sum1 = sum(findDivs(i))
    sum2 = sum(findDivs(sum1))
    if i == sum2 and i!= sum1:
        print(i,sum1,sum2)
        total+=i


print(total)







