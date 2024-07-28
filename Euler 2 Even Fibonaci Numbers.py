
total = 0
counter = 1
stepwise = 0
tweener = 0
j = 0

while counter < 4000000:
    holder = counter
    counter = counter+j
    j = holder

    if counter%2 ==0:
        total = total+counter
    print (counter)


print (total)



