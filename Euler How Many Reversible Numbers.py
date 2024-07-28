

# How Many Reversible Numbers
# https://projecteuler.net/problem=145


def isRev(x):
    s = str(x)
    if s[-1] == '0':
        return False
    evens = '24680'
    revX = s[::-1]
    y = x + int(revX)
    s = str(y)
    for i in s:
        if i in evens:
            return False
    return True


total = 0
tenOfTens = 10
for i in range(1,1000000001):
    if (isRev(i)):
        total+=1
    if i == tenOfTens:
        print(i)
        tenOfTens*=10
print(total)
















