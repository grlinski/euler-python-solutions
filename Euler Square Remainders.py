

# Square Remainders
# https://projecteuler.net/problem=120


def formula(a,n):
    part1 = (a-1)**n
    part2 = (a+1)**n
    part3 = part1+part2
    part4 = a**2
    r = part3%part4
    return r

maxi = 0
for a in range(1,1001):

    for n in range(1,100):
        r = formula(a,n)
        maxi = max(maxi,r)

print(maxi)








