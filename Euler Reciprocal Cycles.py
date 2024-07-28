
from decimal import *
import math
getcontext().prec = 100


# Reciprocal Cycles
# https://projecteuler.net/problem=26


def findSub(string):
    q = []

    end = len(string)
    start = 0
    for k in range(start,end):
        for i in range(start,end):
            ns = ""
            for j in range(start,end):
                ns = ns+string[j]
            q.append(str(start)+'sv'+ns)
            end-=1
        end = len(string)
        start+=1
    return(q)







def isPrime(x):

    limit = int((math.sqrt(x))+1)
    prime = True

    for i in range(2,limit):
        if x%i == 0:
            prime = False
            break

    return prime




def matchingSubs(q,maxi):


    for i in range(0,len(q)-1):
        for j in range(i+1,len(q)):
            svindexa = q[i].index('sv')
            sva = q[i][:svindexa+2]
            a = q[i][svindexa+2:]

            svindexb = q[j].index('sv')
            svb = q[j][:svindexb + 2]
            b = q[j][svindexb + 2:]

            if a==b:
                if len(a) > maxi:
                    print(a)
                    maxi = max(len(a),maxi)
    return maxi


            #print(sva)
            #print(svb)





maxi = 0

for d in range(1,1000):

    x = (Decimal(1)/(Decimal(d)))
    if isPrime(d):
        print(d)
        y = str(x)
        z = (findSub(y))
        maxi = matchingSubs(z,maxi)


print()
print()

print('END')




















