

# Integer Right Triangles
# https://projecteuler.net/problem=39


maxi = 0
ans = 0


for p in range(1,1001):
    total = 0
    tri = set()



    for a in range(1,p):
        for b in range(1,a):
            c = p - (a+b)
            if a+b+c == p:

                    if a**2 == (b**2 + c**2):
                        total+=1
                        h = (a,b,c,p)
                        tri.add(h)
    if total > maxi:
        maxi = total
        ans = p
        print(maxi,p)
        print(tri)

    print(p)

print('answer',ans)


















