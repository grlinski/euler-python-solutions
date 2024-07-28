
# Dice Game
# https://projecteuler.net/problem=205


"""
Peter 9 pyramidal dies
numbers 1,2,3,4

Collin 6 cube dies
number 1,2,3,4,5,6

What is the probability peter beats collin??
To 7 decimal points.




"""




peterD = {}
collinD = {}
collinN = [1,2,3,4,5,6]


peter = [1,1,1,1,1,1,1,1,1]
peterTotal = 0
collinTotal = 0

for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            for d in range(1,5):
                for e in range(1,5):
                    for f in range(1,5):
                        for g in range(1,5):
                            for h in range(1,5):
                                for i in range(1,5):
                                    p = [a,b,c,d,e,f,g,h,i]
                                    peterTotal+=1
                                    total = sum(p)
                                    if total in peterD:
                                        peterD[total]+=1
                                    else:
                                        peterD[total]=1


for a in range(1,7):
    for b in range(1,7):
        for c in range(1,7):
            for d in range(1,7):
                for e in range(1,7):
                    for f in range(1,7):
                        collinTotal+=1
                        p = [a,b,c,d,e,f]
                        total = sum(p)
                        if total in collinD:
                            collinD[total]+=1
                        else:
                            collinD[total]=1

totalGames = (peterTotal*collinTotal)
peterWin = 0
collinWin = 0
draws = 0


for i in peterD:
    peterNum = i
    peterTimes = peterD[i]
    for j in collinD:
        collinNum = j
        collinTimes = collinD[j]
        chance = (collinTimes * peterTimes)/totalGames

        if peterNum > collinNum:
            peterWin+=chance
        elif collinNum > peterNum:

            collinWin+=chance
        else:
            draws+=chance

# Peter Win, Collin, Draws

print(peterWin,collinWin,draws)
print(peterWin+collinWin+draws)


















