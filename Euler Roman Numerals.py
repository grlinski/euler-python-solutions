

# Roman Numerals
# https://projecteuler.net/problem=89
"""
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000





"""

def romanNumeralToDecimal(rome):
    """
    MDCLXVI


    """
    romedict = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}


    numbers = []
    ordnum = []
    order = []
    prev = 'w'
    total = 0
    for i in rome:
        if i == prev:
            total+=1
        else:
            x = str(total)+prev
            ordnum.append(x)
            order.append(prev)
            total = 1
        prev = i
    x = str(total) + prev
    ordnum.append(x)
    order.append(prev)
    ordnum = ordnum[1:]
    order = order[1:]




    for i in ordnum:
        num = i[0]
        let = i[1]
        total = romedict[let]*int(num)
        numbers.append(total)
    total = 0
    for i in range(1,len(numbers)):
        prev = numbers[i-1]
        cur = numbers[i]
        if prev > cur:
            total+=prev
            if i == len(numbers)-1:
                total+=cur
        else:
            total+= cur-prev

    return total


def decimalToRome(deci):

    rome = ''
    sdeci = str(deci)

    while len(sdeci) < 4:
        sdeci ='0'+sdeci

    thou = deci//1000
    hund = int(sdeci[1])
    hundAbove5 = hund-5
    tens = int(sdeci[2])
    tensAbove5 = tens-5
    ones = deci%10
    onesAbove5 = ones-5


    if thou == 0:
        pass
    else:
        rome+='M'*thou


    if hund ==9:
        rome+='CM'
    elif hund >= 5:

        rome+='D'
        if hundAbove5 > 0:
            rome+='C'*hundAbove5
    elif hund == 4:
        rome += 'CD'
    else:
        rome+='C'*hund


    if tens ==9:
        rome+='XC'
    elif tens >= 5:

        rome+='L'
        if tensAbove5 > 0:
            rome+='X'*tensAbove5
    elif tens == 4:
        rome += 'XL'
    else:
        rome+='X'*tens



    if ones ==9:
        rome+='IX'
    elif ones >= 5:

        rome+='V'
        if onesAbove5 > 0:
            rome+='I'*onesAbove5
    elif ones == 4:
        rome += 'IV'
    else:
        rome+='I'*ones




    return rome


totalsaved = 0
for i in range(0,1000):
    rome = input()
    deci = romanNumeralToDecimal(rome)
    rome2 = decimalToRome(deci)
    diff = len(rome) - len(rome2)



    if diff < 0:
        print(rome,deci,rome2)
    totalsaved+=diff


print(totalsaved)













