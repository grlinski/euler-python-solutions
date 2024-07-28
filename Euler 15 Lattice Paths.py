
#20 x 20 Grid


# Visualize it like this, we need 40 moves to reach the end.
# 20 moves to the right, 20 down.
# We need to see how many permuations of right and down there are.

#2x2 Example
#RRDD, RDRD, RDDR, DRDR, DRRD, DDRR. So 6 different paths.
# Need to do the same for 20x20

# Do with 1s and 0s?
# A 40 character number, with only 1s and 0s. When added up ==20
#Possibly need to cap the start with a 2, so it 0011 isn't the same as

right = 1
down = 0

y = int(0b111000)

topmost = int(0b1111111111111111111100000000000000000000)
print(topmost)
#topmost = 1099510579200



def sum_digits3(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


twentyer = 0


counter = 0


i = 0

for i in range(0,topmost):
    x = int(i)
    y = bin(x)
    z = str(y)
    z = z[2:]
    x = int(z)
    twentyer = (sum_digits3(x))
    if twentyer == 20:
        counter = counter+1
        if counter % 10000 == 0:
            print(counter)




print(counter)
print(counter)
print(counter)







