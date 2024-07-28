
# Euler 15 Lattice Paths



import itertools
num = 5

down = ["d"]*num
right = ['r']*num
paths = down+right

x = (set(itertools.permutations(paths)))
print(len(x))
















