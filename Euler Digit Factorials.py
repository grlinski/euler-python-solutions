

# Digit Factorials
# https://projecteuler.net/problem=34



# UPLIMIT 9999999

factorials = [1,1,2,6,24,120,720,5040,40320,362880]


ans = 0
for i in range(3,9999999):

    s = str(i)
    total = 0
    for j in s:
        x = int(j)
        total +=factorials[x]

    if total==i:
        print(i)
        ans = ans+i



print(ans)










