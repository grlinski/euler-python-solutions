



# Sub-string divisibility
# https://projecteuler.net/problem=43



from itertools import permutations



nums = [0,1,2,3,4,5,6,7,8,9]

x = permutations(nums,10)





total = 0


for i in x:
    d=''
    s = list(i)
    for i in s:
        d+=str(i)

    a = int(d)
    if len(str(a)) < 10:
        pass
    else:
        v1 = int(d[1:4])
        v2 = int(d[2:5])
        v3 = int(d[3:6])
        v4 = int(d[4:7])
        v5 = int(d[5:8])
        v6 = int(d[6:9])
        v7 = int(d[7:10])

        if v1 %2 == 0 and v2 %3 == 0 and v3 %5 == 0 and v4 %7 == 0 and v5 %11 == 0 and v6 %13 == 0 and v7 %17 == 0:
            print(d)
            total += int(d)



print(total)









