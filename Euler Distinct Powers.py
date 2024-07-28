

# Distinct Powers
# https://projecteuler.net/problem=29


set1=set()


for a in range(2,101):

    for b in range(2,101):

        x = a**b
        set1.add(x)

print(len(set1))





