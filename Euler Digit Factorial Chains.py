

# Digit Factorial Chains
# https://projecteuler.net/problem=74

def digitSum(x):
    s = str(x)
    factorials = [1,1,2,6,24,120,720,5040,40320,362880]
    total = 0
    for i in s:
        y = int(i)
        total+=factorials[y]
    return total

tens = 1000
chains = {}
for i in range(1,1000001):

    if i == tens:
        print(i)
        tens+=1000


    x = i
    temp = []
    onOff = True
    while onOff:

        x = digitSum(x)
        if x in temp:
            onOff = False
        else:
            temp.append(x)
    chains[i] = temp

ans = 0

for i in chains:
    if len(chains[i])==59:
        ans+=1
    if len(chains[i]) > 59:
        print(i,chains[i])


print(ans)

















