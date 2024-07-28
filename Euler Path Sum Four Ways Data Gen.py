

# This is just a grid generator, I want to see how long certain sizes will take

import random

size = 6
n1 = 0
n2 = 10000


grid = []
for i in range(size):
    q = []
    for j in range(size):
        x = random.randint(n1, n2)
        q.append(x)
    grid.append(q)

print(grid)

















