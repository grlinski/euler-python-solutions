



# Path Sum Three Ways
# https://projecteuler.net/problem=82
# Rework on the Five list

five =[[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]


# Easy path top left to bottom right
five =[[1,673,234,103,18],[1,1,342,965,150],[630,1,1,422,111],[537,699,1,1,956],[805,732,524,1,1]]


# Easy Path Bottom Left to Top Right
five =[[131,673,234,1,1],[201,96,1,1,150],[630,1,1,422,111],[1,1,497,121,956],[1,732,524,37,331]]


ojfive =[[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]

#
five =[[131,673,1,1,1],[201,96,1,965,150],[630,803,1,422,111],[537,699,1,121,956],[1,1,1,37,331]]



five =[[1,1,1,103,18],[201,96,1,965,150],[630,803,1,422,111],[537,699,1,121,956],[805,732,1,1,1]]



# NTS
"""
So for this minimize each number in each column, with the minimum path to get there.


"""



def minimizeCol(x,y,eighty,ueighty):

    mini = 1000000

    cur = eighty[x][y]
    #print(cur)

    # Side Value
    if eighty[x][y-1] < mini:
        mini = eighty[x][y-1]

    # Below ##################
    end = x+1

    sidex = 1

    # Later change end to 80?


    limit =len(eighty[x])

    while end < limit:
        sideval = eighty[x+sidex][y-1]

        tbelow =0
        for i in range(x+1,end+1):
            tbelow+=(eighty[i][y])

        total = tbelow+sideval
        if total < mini:
            mini = total

        end+=1
        sidex+=1

    # Above ##################
    start = y
    end = x - 1

    sidex = -1

    while end > -1:
        sideval = eighty[x + sidex][y - 1]

        #print(sideval)

        tabove = 0
        for i in range(x -1, end-1,-1):
            tabove += (eighty[i][y])






        total = tabove + sideval

        if x == 1 and y == 2:
            print(total)
        if total < mini:
            mini = total

        #print(tabove)

        end -= 1
        sidex -= 1

    ans = ueighty[x][y] + mini
    return ans




ufive = five[::]




for y in range(1,len(five)):
    newfive = ufive[::]
    app = []
    for x in range(0,len(five[y])):
        #print(neweighty[x][1])
        #print(five[y][x])
        #newfive[x][y] = minimizeCol(x, y, five, ufive)
        ans = minimizeCol(x, y, five, ufive)
        app.append(ans)

        #print(neweighty[x][1])
    for k in range(0,len(five)):
        ufive[k][y] = app[k]



mini = 100000000000
print()
print()
for i in range(0,5):
    print(i)
    mini = min(mini,ufive[i][4])
    print(mini)

for i in ufive:
    print(i)


print()
print(mini)






















