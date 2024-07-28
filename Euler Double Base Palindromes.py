


# Double Base Palindromes
# https://projecteuler.net/problem=36


total = 0

def isPali(x):


    if len(x)%2==0:

        a = x[:len(x)//2]
        b = x[len(x) // 2:]
        r = b[::-1]
        if a==r:
            return True
        else:
            return False

    else:

        a = x[:len(x)//2]
        b = x[len(x) // 2+1:]
        r = b[::-1]

        if a==r:
            return True
        else:
            return False





summer =0
for i in range(1,1000000):
    bx = str(bin(i))
    b = bx[2:]

    s = str(i)

    if isPali(s):
        if isPali(b):
            print(i,b)
            summer+=i
            total+=1



print(total)
print(summer)

















