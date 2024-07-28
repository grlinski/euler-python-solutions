
# Poker Hands
# https://projecteuler.net/problem=54

# Works
# Note if I ever want to improve this, make sure it doesn't accept duplicate cards.
# Also I could always just return the hand ranking value and the list of cards in descending order.
# Rather than the weird return values I have now



totalwins = 0


for z in range(0,1000):
    x = input()

    p1 = []
    p2 = []

    hand1 = ''
    hand2 = ''


    swap = 14

    for i in range(0,len(x),3):
        c = x[i:i+2]
        if i < swap:
            p1.append(c)
        else:
            p2.append(c)





    def handDetermination(cards):

        numlist = []
        numset = set()

        suitlist = []
        suitset = set()

        count = {}

        hand = [0,0,0,0,0]


        for i in cards:
            v = i[0]
            s = i[1]



            suitlist.append(s)
            suitset.add(s)

            if v == 'A':
                numlist.append(14)
            elif v == 'K':
                numlist.append(13)
            elif v == 'Q':
                numlist.append(12)
            elif v == 'J':
                numlist.append(11)
            elif v == 'T':
                numlist.append(10)
            else:
                numlist.append(int(v))

        for i in numlist:
            if i in count:
                count[i]+=1
            else:
                count[i] = 1

        numset = set(numlist)
        numlist = sorted(numlist)

        print(numlist)
        print(numset)
        print(suitlist)
        print(suitset)


        # Hands, Return 2 numbers, Ranking of Actual Hand and then how good that hand is
        #Note for full houses, they both can't hand the same triple.

        # Royal Flush
        if len(suitset) == 1 and len(numset) == 5 and numlist[4] == 14 and numlist[0] == 10:
            print('Royal Flush')
            return 1,1,0,0,0,0
        # Straight Flush, Seems to Work, Get More Test Cases for this one, Redo
        elif len(suitset) == 1 and len(numset) == 5 and ((numlist[4] - numlist[0] == 4) or (numlist[3] - numlist[0] == 3 and numlist[4] == 14)):
            print('Straight Flush')
            if numlist[4] == 14:
                return 2,14-numlist[3],0,0,0,0
            else:
                return 2, 14-numlist[4],0,0,0,0
        # Four of a Kind
        elif 4 in count.values():
            print('Four of a Kind')
            for i in count:
                if count[i]==4:
                    return 3,14-i,0,0,0,0

        # Full House
        elif 3 in count.values() and 2 in count.values():
            print('Full House')
            for i in count:
                if count[i]==3:
                    return 4,14-i,0,0,0,0
        # Flush
        # Return cards
        elif len(suitset) == 1:
            print('Flush')
            q = []
            for i in numlist:
                q.append(i)
            return 5, 14-q[4],14-q[3],14-q[2],14-q[1],14-q[0]
        # Straight
        elif (len(numset) == 5) and ((numlist[4] - numlist[0] == 4) or (numlist[3] - numlist[0] == 3 and numlist[4] == 14)):
            print('Straight')
            if numlist[4] == 14:
                return 6,14-numlist[3],0,0,0,0
            else:
                return 6, 14-numlist[4],0,0,0,0
        # Three of a Kind
        elif 3 in count.values():
            print('Three of a Kind')
            for i in count:
                if count[i] == 3:
                    return 7, 14-i,0,0,0,0
        # Two of a Kind
        elif len(numset) == 3 and 2 in count.values():
            print('Two of a Kind')
            q=[]
            x = 0
            for i in count:
                if count[i] == 2:
                    q.append(i)
                if count[i] == 1:
                    x = i
            return 8,14-max(q),14-min(q),14-x,0,0
        # One Pair
        elif len(numset) == 4 and 2 in count.values():
            print('One Pair')
            q = []
            x = 0
            for i in numlist:
                if count[i] == 2:
                    x = i
            for i in numlist:
                if i!=x:
                    q.append(i)


            return 9, 14-x, 14-q[2],14-q[1],14-q[0]
        else:
            print('High Card')
            q = []
            for i in numlist:
                q.append(i)
            return 10, 14-q[4],14-q[3],14-q[2],14-q[1],14-q[0]






    h1 = (handDetermination(p1))
    h2 = (handDetermination(p2))


    for i in range(0,6):
        a = h1[i]
        b = h2[i]

        if a==b:
            pass
        elif a < b:
            print('Hand 1 Wins')
            totalwins+=1
            break
        elif b < a:
            print('Hand 2 Wins')
            break







print(totalwins)

"""
Royal Flush and Straight
KD QD TD AD JD KD QS JS TH AC

Straight Flush and Straight
9D QD TD AD JD KD QS JS TH AC

Four of a Kind and Straight
4D 4D 4D 4D KD KD QS JS TH AC

Four of a Kind and Straight
2D 4D 4D 4D 4D KD QS JS TH AC

Full House
3D 3D 4D 4D 4D KD QS JS TH AC

Flush
3D 3D 2D 4D 8D KD QS JS TH AC

Two of a Kind
2D 2C 5D 5C AD KD QS JS TH AC


Straight
2D 3C 4D 5C AD KD QS JS TH AC

One Pair
4D 5C 7C 8D 7S KD QS JS TH AC

High Card
4D 5C 7C 8D KS KD QS JS TH AC





8C TS KC 9H 4S 7D 2S 5D 3S AC
5C AD 5D AC 9C 7C 5H 8D TD KS
3H 7H 6S KC JS QH TD JC 2D 8S
TH 8H 5C QS TC 9H 4D JC KS JS


"""