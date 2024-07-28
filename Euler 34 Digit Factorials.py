
# Euler 34 Digit Factorials


"""

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.


"""

import datetime





# Store the factorials of all digits in a list
# These are the factorials of digits 0 to 9.
factorials = [1,1,2,6,24,120,720,5040,40320,362880]

#Construct a Function which takes a number, splits it's digits and adds the factorials together
def factorialadder (value1):
    stringvalue1 = str(value1)
    lengther = len(stringvalue1)
    sum = 0
    for i in range(0,lengther):
        a = stringvalue1[i]
        b = int(a)
        c = factorials[b]
        sum = sum+c
    return(sum)


#Now the Function Works Let's Try For Every Number Under 1 Million
# Topmost is the value the loop stops at.
topmost = 100000000
#Counter is the end value we desire
counter = 0
#Start of Calcs
start = datetime.datetime.now()

#Main Loop
for i in range(0,topmost):
    x = factorialadder(i)
    if(x == i):
        counter+=1
        print(i,x)

end = datetime.datetime.now()

print(counter)
print(end-start)

#Note this program only found 4 values under 100 million
# That took 7m40s
# 1,2,145,40585








