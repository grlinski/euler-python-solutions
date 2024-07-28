

# Combinatoric selections
# https://projecteuler.net/problem=53




def combos(n,r,factorials):
    top = factorials[n]
    bottom = factorials[r]*factorials[n-r]


    return top//bottom




factorials = [1]

f = 1
for i in range(1,101):
    f=f*i
    factorials.append(f)


print(len(factorials))


total = 0




for n in range(1,101):
    for r in range(0,n+1):

        x = (combos(n, r, factorials))
        if x > 1000000:
            total+=1


print(total)


