

# Pandigital Products
# https://projecteuler.net/problem=32


def pandigital(x,y,z):
    a = str(x)
    b = str(y)
    c = str(z)

    d =a+b+c
    limit = len(a+b+c)

    numbers = [1,2,3,4,5,6,7,8,9]
    setter = set(numbers[:limit])


    for i in d:
        try:
            setter.remove(int(i))
        except:
            return False
    if len(setter) > 0:
        return False
    return True






pan = '123456789'

total = 0
ans = []


h = 0
ptr = 10

# 987654322
for i in range(1,7859):

    s = str(i)

    if '0' not in s:
        for j in range(2,i//2):
            if i%j ==0:
                r = i//j



                if pandigital(i,j,r):
                    ans.append(i)
                    print(i)
                    break


    h+=1
    if h == ptr:
        print('Times',h)
        ptr = ptr*10



#7852

print(sum(ans))





