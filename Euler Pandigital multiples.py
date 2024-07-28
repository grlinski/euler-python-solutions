

# Pandigital multiples
# https://projecteuler.net/problem=38


def panDig(x1):


    x2 = x1*2
    x3 = x1*3



    s1 = str(x1)
    s2 = str(x2)
    s3 = str(x3)

    d = s1+s2+s3

    numbers = [1,2,3,4,5,6,7,8,9]
    setter = set(numbers)

    for i in d:
        try:
            setter.remove(int(i))
        except:
            return False
    if len(setter) > 0:
        return False
    return True


def panDig2(x1):


    x2 = x1*2




    s1 = str(x1)
    s2 = str(x2)


    d = s1+s2

    numbers = [1,2,3,4,5,6,7,8,9]
    setter = set(numbers)

    for i in d:
        try:
            setter.remove(int(i))
        except:
            return False
    if len(setter) > 0:
        return False
    return True




for i in range(1,1000000):

    #break

    s = str(i)
    set1 = set()
    for j in s:
        set1.add(j)

    # Quick Check for Duplicate numbers
    if len(set1) != len(s):
        pass
    else:
        if(panDig(i)):
            print(i,i*2,i*3)
        if (panDig2(i)):
            print(print(i,i*2))


































