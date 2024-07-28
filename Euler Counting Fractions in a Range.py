
# Counting Fractions in a Range
# https://projecteuler.net/problem=73

"""

Solved

Fairly Easy
Got the question correct the first time
7295372
Best advice is to keep range low, create cutoff points that stop the loop



"""

def GCD(a,b):
    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
    return a


counter = 0
total=0
for den in range(1,12001):
    start = int(den*(1/3))
    for num in range(start,den):
        counter += 1
        if num/den > 0.5:
            break
        if num/den > (1/3) and num/den < (1/2):
            if GCD(num,den) == 1:
                total+=1






print(counter)
#71994000
#36005997
#12025998
print(total)






