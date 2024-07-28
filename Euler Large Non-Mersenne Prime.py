

# Large non-Mersenne prime
# https://projecteuler.net/problem=97


# The largest Non-Mersenne Prime
# 28433×2**7830457+1
# Find the last ten digits of this number.
"""
I'm going to attempt brute force computing
However I only need to technically worry about storing the last ten digits

So I can just multiply 2 by itself 7830457 times, storing only the last ten digits
Then multiply it again by 28433 and add one.


"""

# 27830457
# Should





num = 1
# Note since I already have set num to 2, that's one less times I need to multiply by 2
for i in range(0,27830457):
    num = num *2
    s = str(num)
    if len(s) >20:
        over = len(s)-20
        rd  = s[over:]
        num = int(rd)

print(num)
ans =((num*28433)+1)
print(ans)









"""
Past Answers that were wrong.
939992577
Obviously this was wrong since I input 9 digits

7939992577
This one is very close to the real answer
5879985153



So I looked up the answer which is 8739992577
7939992577
Why is my answer 8 off?




"""







