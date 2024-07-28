

# Triangular, pentagonal, and hexagonal
# https://projecteuler.net/problem=45



seta = set()
setb = set()
setc = set()


for i in range(1,1000000):


    tri = (i * (i + 1)) // 2
    pen = (i * (3*i - 1)) // 2
    hex = (i * (2*i - 1))

    seta.add(tri)
    setb.add(pen)
    setc.add(hex)


setans = (seta & setb & setc)

print(setans)






