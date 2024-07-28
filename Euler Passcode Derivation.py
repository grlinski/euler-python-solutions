

# Passcode Derivation
# https://projecteuler.net/problem=79


codes = ['680', '180', '690', '129', '620', '762', '689', '762', '318', '368', '710', '720', '710', '629', '168', '160', '689', '716', '731', '736', '729', '316', '729', '729', '710', '769', '290', '719', '680', '318', '389', '162', '289', '162', '718', '729', '319', '790', '680', '890', '362', '319', '760', '316', '729', '380', '319', '728', '716']




# Pairs, Create Pairs of Numbers and Create Consensus, after finding the first number.
# Pairs

pairs = []
before = []
for i in codes:
    p1 = i[0:2]
    p2 = i[1:]
    pairs.append(p1)
    pairs.append(p2)
    a = i[0]
    b = i[1]
    c = i[2]
    if a in before:
        pass
    else:
        before.append(a)
    if b in before:
        pass
    else:
        before.append(b)
    if c in before:
        pass
    else:
        before.append(c)




# Swap Values
for i in pairs:
    a = i[0]
    b = i[1]

    x = before.index(a)
    y = before.index(b)
    print(a,x,b,y)
    if x > y:
        before[x] = b
        before[y] = a
        print(before)

print(before)
s= ''.join(before)
print(s)








