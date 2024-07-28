





# Large non-Mersenne prime Mk2
# https://projecteuler.net/problem=97

# Trying the mod % way this time
# I copied the 2**7830457 incorrectly in the original
# It has been changed and now works.



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



# My Work
############################################
num = 1
# Note since I already have set num to 2, that's one less times I need to multiply by 2
for i in range(0,7830457):
    num = num *2
    num = num%10000000000



ans =((num*28433)+1)
print(ans)




























