

# Pentagon Numbers
# https://projecteuler.net/problem=44

"""

Alright so from what I gather

The difference between any two numbers is
1+(3**?)





"""









pent = []
for i in range(1,10000):
    # Pn=n(3n−1)/2

    p = i*(3*i-1)//2
    pent.append(p)

mini = 1000000


for a in range(0,len(pent)-1):
    for b in range(a+1,len(pent)):

        x = pent[a]
        y = pent[b]

        s = abs(x-y)
        d = x+y


        if s in pent:

            print(x,y,s,d,(d in pent))







print('ending')
print(mini)

"""

                if mini < d:
                    mini = d
                    print(x,y,mini)


"""




