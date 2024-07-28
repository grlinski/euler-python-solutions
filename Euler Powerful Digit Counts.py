

# Powerful Digit Counts
# https://projecteuler.net/problem=63

total =0

for a in range(1,10000):
    for b in range(1,30):

        c = a**b
        if b == len(str(c)):
            print(a,b,c)
            total+=1




print(total)












