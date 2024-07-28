


# Square Digit Chains
# https://projecteuler.net/problem=92



square = [0,1,4,9,16,25,36,49,64,81]



def digiSquare(x):

    q = [x]
    n = 0
    for t in range(0,1000):
        n = 0
        for i in str(x):
            n=n+square[int(i)]
        q.append(n)
        x = n

        #print(n)
        #print(n,end=' ')
        if n == 89:
            return True
        if n == 1:
            return False
    return False








total = 0
for i in range(1,10000000):

    x = (digiSquare(i))
    if x == True:
        #print(i)
        total+=1

print(total)








