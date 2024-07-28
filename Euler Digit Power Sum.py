
# Digit Power Sum
# https://projecteuler.net/problem=119
"""
Right Track, likely need more powers.
248155780267521
Turns out I was accidently counting a few non valid entries.
Namely those which were single digits.




"""

def digitSum(x):
    s = str(x)
    total = 0
    for i in s:
        total+=int(i)
    return total



def checkPower(b,e):

    while True:
        b=b/e

        if int(b)!=b:
            return False
        elif b==1:
            return True


powers = []

for b in range(1,1000):
    print(b)
    for e in range(2,100):
        p = b**e
        powers.append(p)

ans = []
powers = set(powers)
powers = list(powers)
powers.sort()
count = 1
for i in powers:
    ds = digitSum(i)
    if i%ds == 0 and ds!=1:
        if checkPower(i,ds):
            if len(str(i)) == 1:
                pass
            else:
                print(i,ds,count)
                count+=1
                ans.append(i)


ans = set(ans)
ans = list(ans)
ans.sort()

counter = 0
# Ignore 4
for i in ans:
    print(i,counter)
    counter+=1


"""
Base Digit Sum
81 9
512 8
2401 7
4913 17
5832 18
17576 26
19683 27
234256 22
390625 25
614656 28





"""








