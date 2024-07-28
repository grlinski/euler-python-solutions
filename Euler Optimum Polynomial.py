
# Optimum Polynomial
# https://projecteuler.net/problem=101




def formula(x):
    ans = 1-x+(x**2)-(x**3)+(x**4)-(x**5)+(x**6)-(x**7)+(x**8)-(x**9)+(x**10)
    print(ans)


for i in range(1,10):
    formula(i)











