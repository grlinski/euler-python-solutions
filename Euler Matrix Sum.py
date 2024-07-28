


# Matrix Sum
# https://projecteuler.net/problem=345


def printGrid(grid):
    for i in grid:
        print(i)


def separateNumbers(s):
    list1 = []
    num = ''
    for i in s:
        if i == ' ':
            if num == '':
                pass
            else:
                list1.append(int(num))
            num = ''
        else:
            num = num+i
    list1.append(int(num))
    return list1


def numb1000(grid):
    for i in range(0,len(grid)):
        for j in range(0,len(grid)):
            grid[i][j] = 1000-grid[i][j]
    return grid




def rowReduction(grid):
    counter = 0
    for i in range(0,len(grid)):
        maxi = max(grid[i])
        maxi = maxi//5
        for j in range(0,len(grid)):
            x = grid[i][j]
            if x < maxi:
                grid[i][j] = 0
                counter+=1

    printGrid(grid)
    print(counter)




def flowControl(grid):
    usedRows = []
    usedCols = []




grid = []
firstLine = input()
temp = separateNumbers(firstLine)
grid.append(temp)


for i in range(len(temp)-1):
    temp = input()
    temp = separateNumbers(temp)
    grid.append(temp)
size = len(grid)
printGrid(grid)
rowReduction(grid)













