
# https://projecteuler.net/problem=94
# Almost Equilateral Triangles
"""
Smaller
Larger
Smaller

Alternates between big sides
https://mathschallenge.net/full/almost_equilateral_triangles#:~:text=We%20shall%20define%20an%20almost,is%205%2D5%2D6.


Formula
hyp**2 = height**2 + (b/2)**2




"""



import math



def isIntegral(x):
    y = int(x)
    if y==x:
        return True
    else:
        return False


def triangleArea(equalSides,oneSide):
    base = oneSide/2
    height = math.sqrt(equalSides**2-base**2)

    area = (base*height)/2
    if isIntegral(area):
        perimeter = equalSides*2+oneSide
        #if equalSides < oneSide:
            #print('2 Smaller than 1')

        #else:
            #print('2 Larger than 1')
        #print(int(area),equalSides,equalSides,oneSide)
        #print('Peri',perimeter)
        return True,int(area)
    return False,0



topmost = 1000000

a = 1
b = 2
smaller2 = []
larger2 = []
allArea = []

for i in range(0,topmost):
    ab = triangleArea(a,b)
    ba = triangleArea(b,a)

    if ab[0] == True:
        ans = [ab[1],a,a,b]
        smaller2.append(ans)
        allArea.append(ans)
        #print(ans)
    if ba[0] == True:
        ans = [ba[1],b,b,a ]
        larger2.append(ans)
        allArea.append(ans)
        #print(ans)



    a+=1
    b+=1
print('XXXXXXXXXXXXXXXXXX')
print('Smaller Equal Sides')
for i in smaller2:
    print(i)


print('XXXXXXXXXXXXXXXXXX')
print('Larger Equal Sides')
prev = 1
prev2 = 1
for i in larger2:
    area = i[0]
    print(area,end=',')
    prev = area

print()
print('XXXXXXXXXXXXXX')
print()
for i in allArea:
    area = i[0]
    print(area,end=',')





























