




# Cubic Permutations
# https://projecteuler.net/problem=62


def id_digits(x,d1,d2):

    list1 = []
    for i in str(x):
        list1.append(i)


    list1.sort()
    t = tuple(list1)

    if t in d1:
        d1[t]+=1
    else:
        d1[t] = 1


    if t in d2:
        d2[t] = d2[t]+', '+str(x)
    else:
        d2[t] = str(x)
    return d1,d2




dict1 = {}
dict2 = {}

for i in range(1,100000):
    i =i*i*i
    dict1,dict2 = (id_digits(i,dict1,dict2))

#print(dict2)

for i in dict1:
    if dict1[i] >4:
        print(i)
        print(dict2[i])








