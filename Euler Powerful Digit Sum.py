


# Powerful Digit Sum
# https://projecteuler.net/problem=56


def digisum(x):
    y = str(x)
    total = 0
    for i in y:
        total+=int(i)
    return total


maxi = 0
for a in range(0,100):
    for b in range(0,a):

        m = digisum(a**b)
        if m > maxi:
            print(m,a,b)
            maxi = m

print(maxi)


















