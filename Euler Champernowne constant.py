



# Champernowne's constant
# https://projecteuler.net/problem=40

s = '0'
for i in range(1,1000000):
    x = str(i)
    s = s+x


ans = int(s[1])*int(s[10])*int(s[100])*int(s[1000])*int(s[10000])*int(s[100000])*int(s[1000000])

print(ans)






