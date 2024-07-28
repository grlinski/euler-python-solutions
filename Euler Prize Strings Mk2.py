

# Prize Strings Mk2
# https://projecteuler.net/problem=191

"""
Original Got too Convoluted
Ended up with some problems that were easier to fix by redoing everything

"""


from itertools import combinations_with_replacement
from itertools import permutations


def tupleToList(tup):
    list1 = []
    for i in tup:
        list1.append(i)
    return list1

def countLinList(list1):
    counter=0
    for i in list1:
        if i =='L':
            counter+=1
    return counter

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

def listToString(list1):
    s = ''
    for i in list1:
        s+=i
    return s




segment5 = []
items = ['A','O','L']




x = combinations_with_replacement(items,5)
counter=0

for i in x:
    list1 = tupleToList(i)
    count = countLinList(list1)
    if count > 1:
        pass
    else:
        segment5.append(list1)

win5 = []
for i in segment5:
    y = permutations(i,5)
    for j in y:
        list1 = tupleToList(j)
        s = listToString(list1)
        good = removeNonWinners(s)
        if good:
            win5.append(s)

win5 = set(win5)
win5 = list(win5)

win10 = []
for i in win5:
    for j in win5:
        s= i+j
        good = removeNonWinners(s)
        if good:
            win10.append(s)
print(len(win10))
win15 = []
for i in win10:
    for j in win5:
        s1= i+j
        good = removeNonWinners(s1)
        if good:
            win15.append(s1)



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


for i in win15:
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

"""
Rules for answers
Also remember to combine each list with itself if possible.
Lates cannot be combined with lates.
AAxAA cannot be combined with any that begin or start with A
AxA can go with AxA

Combinations
Instead do what it either does combine with or what it doesn't.

n = No Late, l = Late
nOxO
nOxO + Everything

nAxO
nAxO + Everything

nAAxO
nAAxO + Everything

nOxA
nOxA, anything except those that start with Two As AA

nOxAA
nOxAA anything except those that start with one A

nAxA
nAxA anything except those that start with Two As AA

nAAxA
nAAxA anything except those that start with Two As AA, cannot combine with self

nAAxAA
nAAxAA nothing that starts with A, cannot combine with self

nAxAA
nAxAA nothing that starts with A, cannot combine with self.


Lates, cannot combine with eachother or self.
So only concern self with nolates.
lOxO + Everything

lAxO + Everything

lAAxO + Everything
lOxA + Cannot start with 2As
lOxAA + Cannot start with A
lAxA + Cannot start with 2As
lAAxA Cannot start with 2As
lAAxAA Cannot start with A
lAxAA Cannot start with A


nOxO
nAxO
nAAxO
nOxA
nOxAA
nAxA
nAAxA
nAAxAA
nAxAA

lOxO
lAxO
lAAxO
lOxA 
lOxAA
lAxA
lAAxA 
lAAxAA
lAxAA
problems = 0


"""



# Adding to the Answer


nOxO = len(noLatesOxO )
nAxO = len(noLatesAxO )
nAAxO = len(noLatesAAxO )
nOxA = len(noLatesOxA )
nOxAA = len(noLatesOxAA )
nAxA = len(noLatesAxA )
nAAxA = len(noLatesAAxA )
nAAxAA = len(noLatesAAxAA )
nAxAA = len(noLatesAxAA )

lOxO = len(latesOxO )
lAxO = len(latesAxO )
lAAxO = len(latesAAxO )
lOxA = len(latesOxA )
lOxAA = len(latesOxAA )
lAxA = len(latesAxA )
lAAxA  = len(latesAAxA )
lAAxAA = len(latesAAxAA )
lAxAA = len(latesAxAA )


total = 0
everything = [nOxO,nAxO,nAAxO,nOxA,nOxAA,nAxA,nAAxA,nAAxAA,nAxAA,lOxO,lAxO,lAAxO,lOxA,lOxAA,lAxA,lAAxA,lAAxAA,lAxAA]
startsOneAorLess = [nOxO,nAxO,nOxA,nOxAA,nAxA,nAxAA,lOxO,lAxO,lOxA,lOxAA,lAxA,lAxAA]
startsNoStartA = [nOxO,nOxA,nOxAA,lOxO,lOxA,lOxAA]

# No Lates
everythingN = [nOxO,nAxO,nAAxO,nOxA,nOxAA,nAxA,nAAxA,nAAxAA,nAxAA]
startsOneAorLessN = [nOxO,nAxO,nOxA,nOxAA,nAxA,nAxAA]
startsNoStartAN = [nOxO,nOxA,nOxAA]

# nOxO
for i in everything:
    total+=nOxO*i
# nAxO
for i in everything:
    total+=nAxO*i
# nAAxO
for i in everything:
    total+=nAAxO*i
# nOxA
for i in startsOneAorLess:
    total+=nOxA*i
# nOxAA
for i in startsNoStartA:
    total+=nOxAA*i
# nAxA
for i in startsOneAorLess:
    total+=nAxA*i
# nAAxA
for i in startsOneAorLess:
    total+=nAAxA*i
# nAAxAA
for i in startsNoStartA:
    total+=nAAxAA*i
# nAxAA
for i in startsNoStartA:
    total+=nAxAA*i

# Lates
# lOxO
for i in everythingN:
    total+=lOxO*i
# lAxO
for i in everythingN:
    total+=lAxO*i
# lAAxO
for i in everythingN:
    total+=lAAxO*i
# lOxA
for i in startsOneAorLessN:
    total+=lOxA*i
# lOxAA
for i in startsNoStartAN:
    total+=lOxAA*i
# lAxA
for i in startsOneAorLessN:
    total+=lAxA*i
# lAAxA
for i in startsOneAorLessN:
    total+=lAAxA*i
# lAAxAA
for i in startsNoStartAN:
    total+=lAAxAA*i
# lAxAA
for i in startsNoStartAN:
    total+=lAxAA*i


print(total)



