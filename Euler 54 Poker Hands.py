
#Cards go first then suit.
cards = {'A':1, '2':2, '3':3, '4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11, 'Q':12,'K':13}
suit = {'S':1,'D':2,'C':3,'H':4}


#Get All Hand Input
listofhands = []
string1=""
while True:
    string1 = input()
    if string1 == "":
        break
    listofhands.append(string1)


handx = listofhands[i]
hand1 = handx[:9]
hand2 = handx[9:]

straight1 = 0
straight2 = 0
flush1 = 0
flush2 = 0



