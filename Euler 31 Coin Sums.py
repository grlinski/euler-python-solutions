
#How many ways to make 2$?
#This is in pounds but for simplicity I'm going to use cents and dollars

#Note this program works but is insanely inefficient.

a = 1
b = 2
c = 5
d = 10
e = 20
f = 50
g = 100
h = 200

#Since each value can only hit a certain amount, ie) There can't be 201 a values or 5 f values.
# As exceeding those limits puts us over 200. So cap those values, l = limit
al = 201
bl = 101
cl = 41
dl = 21
el = 11
fl = 5
gl = 2
hl = 2


#Amount of Each value
ax = 0
bx = 0
cx = 0
dx = 0
ex = 0
fx = 0
gx = 0
hx = 0

#Also I can probably leave out h, just automatically count it. This will cut computations by half

breaker = 0
#Counts Amount of Ways to Make 200
counter = 1


while breaker != 1:
    sum = 0
    if ax == al:
        ax = 0
        bx = bx+1

    if bx == bl:
        bx = 0
        cx = cx+1

    if cx == cl:
        cx = 0
        dx = dx+1

    if dx == dl:
        dx = 0
        ex = ex+1

    if ex == el:
        ex = 0
        fx = fx+1

    if fx == fl:
        fx = 0
        gx = gx + 1

    if gx > gl:
        breaker = 1

    sum = (a*ax) +(b*bx)+(c*cx)+(d*dx)+(e*ex)+(f*fx)+(g*gx)

    if sum == 200:
        counter = counter+1
        if counter%10000 ==0:
            print(counter)
       # print(counter)

    ax = ax+1

print(counter)
print(counter)
print(counter)














