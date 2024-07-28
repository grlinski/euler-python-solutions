
# Prize Strings
# https://projecteuler.net/problem=191
from itertools import combinations_with_replacement
from itertools import permutations
"""
Turns out problem was with winners/win10 segments
Forgot to rid myself of bad strings
However I've moved to Mk2




"""


def copyList(list1):
    list2 = []
    for i in range(0,len(list1)):
        x = list1[i]
        list2.append(x)
    return list2

def tupleToList(tup):
    list1 = []
    for i in tup:
        list1.append(i)
    return list1

def listToString(list1):
    s = ''
    for i in list1:
        s+=i
    return s


"""
Three As in a row
Two Ls anywhere


"""

def removeNonWinners(string1):
    lcount = 0
    acount = 0
    for i in string1:
        if i=='L':
            lcount+=1

    for i in range(0,len(string1)-2):
        parts = string1[i:i+3]
        if parts == 'AAA':
            return False



    if lcount > 1:
        return False
    return True




def createNewWinners(winners,segment5):
    newWinners = []
    for i in winners:
        for j in segment5:
            s =i+j
            good = removeNonWinners(s)
            if good:
                newWinners.append(s)
    return newWinners






items = ['A','O','L']




x = combinations_with_replacement(items,5)
set5 = set()
for i in x:
    list1 = tupleToList(i)
    y = permutations(list1,5)
    for j in y:
        list1 = tupleToList(j)
        s = listToString(list1)
        set5.add(s)

# List 5 Contains all 5 Segment Winners.
list5 = list(set5)
segment5 = []
for i in list5:
    good = removeNonWinners(i)
    if good:
        segment5.append(i)
print(len(segment5))
winners = createNewWinners(segment5,segment5)
print(len(winners))

for i in range(0,1):
    newWinners = []
    for j in winners:
        good = removeNonWinners(j)
        if good:
            newWinners.append(j)
    winners15 = createNewWinners(newWinners,segment5)


"""
Alright now I have the half of everything.
Separate the items into different lists
For example if it has 0 lates, or 1 late.
If it ends with A or AA
If it begins with A or AA
And essentially clear ones.
Then I can just multiply them by eachother.

"""

# Lists
# No Lates,
noLatesOxO = []
noLatesAxO = []
noLatesAAxO = []
noLatesOxA = []
noLatesOxAA = []
noLatesAxA = []
noLatesAAxA = []
noLatesAAxAA = []
noLatesAxAA = []

# Lates, Doesn't End or Begin with As
latesOxO = []
latesAxO = []
latesAAxO = []
latesOxA = []
latesOxAA = []
latesAxA = []
latesAAxA = []
latesAAxAA = []
latesAxAA = []
problems = 0


for i in winners15:
    end1 = i[-1]
    end2 = i[-2]
    start1 = i[0]
    start2 = i[1]

    if 'L' in i:
        if end1 !='A'  and start1 != 'A':
            latesOxO.append(i)
        elif start1 == 'A' and start2 !='A' and end1!='A':
            latesAxO.append(i)
        elif start1 == 'A' and start2 =='A' and end1!='A':
            latesAAxO.append(i)
        elif start1 != 'A' and end2!='A' and end1=='A':
            latesOxA.append(i)
        elif start1 != 'A' and end2=='A' and end1=='A':
            latesOxAA.append(i)
        elif start1 == 'A' and start2 != 'A' and end2 != 'A' and end1 == 'A':
            latesAxA.append(i)
        elif start1 == 'A' and start2 == 'A' and end2 != 'A' and end1 == 'A':
            latesAAxA.append(i)
        elif start1 == 'A' and start2 == 'A' and end2 == 'A' and end1 == 'A':
            latesAAxAA.append(i)
        elif start1 == 'A' and end2 == 'A' and end1 == 'A':
            latesAxAA.append(i)
        else:
            print('Problem L',i)
            print(start1,start2,end2,end1)
            problems+=1
    elif 'L' not in i:
        if end1 !='A'  and start1 != 'A':
            noLatesOxO.append(i)
        elif start1 == 'A'  and start2!='A' and end1!='A':
            noLatesAxO.append(i)
        elif start1 == 'A' and start2 =='A'  and end1!='A':
            noLatesAAxO.append(i)
        elif start1 != 'A' and end2 !='A' and end1=='A':
            noLatesOxA.append(i)
        elif start1 != 'A' and end2=='A' and end1=='A':
            noLatesOxAA.append(i)
        elif start1 == 'A' and start2 != 'A' and end2 != 'A' and end1 == 'A':
            noLatesAxA.append(i)
        elif start1 == 'A' and start2 == 'A' and end2 != 'A' and end1 == 'A':
            noLatesAAxA.append(i)
        elif start1 == 'A' and start2 == 'A' and end2 == 'A' and end1 == 'A':
            noLatesAAxAA.append(i)
        elif start1 == 'A' and start2 != 'A' and end2 == 'A' and end1 == 'A':
            noLatesAxAA.append(i)
        else:
            print('Problem',i)
            problems+=1
    else:
        print('Problem X',i)
        problems+=1


print(len(noLatesOxO))
print(len(noLatesAxO))
print(len(noLatesOxA))

print(len(noLatesAAxO))
print(len(noLatesOxAA))

print(len(noLatesAxA))
print(len(noLatesAAxAA))
print(len(noLatesAAxA))

print(len(noLatesAxAA))


print('Lates')
print(len(latesOxO))
print(len(latesAxO))
print(len(latesOxA))

print(len(latesAAxO))
print(len(latesOxAA))

print(len(latesAxA))
print(len(latesAAxAA))
print(len(latesAAxA))

print(len(latesAxAA))



# Lates, Doesn't End or Begin with As
latesOxO = []
latesAxO = []
latesAAxO = []
latesOxA = []
latesOxAA = []
latesAxA = []
latesAAxA = []
latesAAxAA = []
latesAxAA = []



