
# Bouncy Numbers
# https://projecteuler.net/problem=112
"""

1587000 1587000 1571130 0.99



"""

def checkBouncy(x):

    s = str(x)

    rev = s[::-1]
    upwards = True
    downwards = True

    prev = 0
    #Upwards

    for i in s:
        if int(i) >= prev:
            pass
        else:
            upwards = False
            break
        prev = int(i)

    #Downward
    prev = 10
    for i in s:
        if int(i) <= prev:
            pass
        else:
            downwards = False
            break
        prev = int(i)
    if downwards==True and upwards==True:
        return True
    ans = downwards != upwards
    #print(upwards,downwards)
    return ans


# False == Bouncy, True == Upwards or Downwards or All Digits Same
bouncy = 0
notBouncy = 0
ratio = 0
count = 1
numb = 1
while True:
    if checkBouncy(numb) == True:
        notBouncy+=1
    else:
        bouncy+=1
    #print(i,checkBouncy(i))


    ratio = bouncy/count
    if ratio >= 0.99:
        print(count,numb,bouncy,ratio)
        break



    count += 1
    numb+=1






print(count,numb,bouncy,ratio)












