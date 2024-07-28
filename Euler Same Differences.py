

# Same Differences
# https://projecteuler.net/problem=135

squares = []

for i in range(1,1000000):
    sq = i**2
    squares.append(sq)

squareminus1 = []
for i in range(len(squares)-1,1,-1):
    for j in range(i,0,-1):
        x =i*j















