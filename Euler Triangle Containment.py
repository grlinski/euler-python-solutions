

# Triangle Containment
# https://projecteuler.net/problem=102


"""
To check if a point is inside or outside a triangle
https://www.geeksforgeeks.org/how-to-check-if-a-given-point-lies-inside-a-polygon/

Basically move the point right.



"""





def between(a,b):

    if (0 >= a and 0 <= b) or (0 <= a and 0 >= b):
        return 1
    else:
        return 0


def contains(ax,ay,bx,by,cx,cy):
    total = 0
    total += between(ax,bx)
    total += between(bx, cx)
    total += between(cx, ax)


    total += between(ay, by)
    total += between(by, cy)
    total += between(cy, ay)

    return total





counter = 0

for i in range(0,1000):
    a,b,c,d,e,f = map(int, input().split(','))

    total = contains(a,b,c,d,e,f)
    print(a,b,c,d,e,f)
    print(total)
    if total==4:
        counter+=1


print(counter)






