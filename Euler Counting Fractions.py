
# Counting Fractions
# https://projecteuler.net/problem=72

"""

How many reduced fractions with denominators up to d?

Check all numbers up to say 30



Some ideas
Let's say d=100
I'd know from the start there are 99 that have 1 as the numerator
Note we don't include 1/1
Half that amount for 2
Third that amount for 3
4 is where things are a bit different.
Any even denoms are reduced.
However odd ones are all original
1/5 for 5
Also note that as we go up in numerators, there will be less denominators possible
5/6 to 5/99 for example, I can't do 5/1 or 5/4

Now on to 6 which is highly divisible
6/7, 6/11
Only primes work as denoms.
7 can't be divided so as long as the denom isn't divisible by 7 its original

Note every fraction has a pair.
1/3 and 2/3
1/8, 7/8


https://en.wikipedia.org/wiki/Euler's_totient_function

totient


"""

import math



# Finds the greatest common divisor.
# Likely doesn't work if 1 is put in.
def findGCD(a,b):
    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
    return a




# Finds all Divisors of a Number, not including the number itself.
def findDivs(x):
    q = [1]
    e = int(math.sqrt(x))+1

    for i in range(2,e):
        if x%i == 0:
            if (x//i == i):
                q.append(i)
            else:
                q.append(i)
                q.append(x//i)

    return q

counter = 0

#for i in range(1,1000000):
#    (findDivs(i))


for denom in range(999990,1000001):
    counter=0
    for numer in range(1,denom):
        x = findGCD(numer,denom)
        if x == 1:
            counter+=1
    print(counter)












"""
1 = 0
2 = 1
3 = 3
4 = 5
5 = 9
6 = 11
7 = 17
8 = 21
9 = 27
10 = 31


3 3
4 5
5 9
6 11
7 17
8 21
9 27
10 31
11 41
12 45
13 57
14 63
15 71
16 79
17 95
18 101
19 119
20 127
21 139
22 149
23 171
24 179
25 199
26 211
27 229
28 241
29 269
30 277
31 307
32 323
33 343
34 359
35 383
36 395
37 431
38 449
39 473
40 489
41 529
42 541
43 583
44 603
45 627
46 649
47 695
48 711
49 753
50 773
51 805
52 829
53 881
54 899
55 939
56 963
57 999
58 1027
59 1085
60 1101
61 1161
62 1191
63 1227
64 1259
65 1307
66 1327
67 1393
68 1425
69 1469
70 1493
71 1563
72 1587
73 1659
74 1695
75 1735
76 1771
77 1831
78 1855
79 1933
80 1965
81 2019
82 2059
83 2141
84 2165
85 2229
86 2271
87 2327
88 2367
89 2455
90 2479
91 2551
92 2595
93 2655
94 2701
95 2773
96 2805
97 2901
98 2943
99 3003
100 3043

3, 5, 9, 11, 17, 21, 27, 31, 41, 45, 57, 63, 71, 79, 95, 101, 119, 127, 139, 149, 171, 179, 199, 211, 229, 241, 269, 277, 307, 323, 343, 359, 383, 395, 431, 449, 473, 489, 529, 541, 583, 603, 627, 649, 695, 711, 753, 773, 805, 829, 881, 899, 939, 963, 999, 1027, 1085, 1101, 1161, 1191, 1227, 1259, 1307, 1327, 1393, 1425, 1469, 1493, 1563, 1587, 1659, 1695, 1735, 1771, 1831, 1855, 1933, 1965, 2019, 2059, 2141, 2165, 2229, 2271, 2327, 2367, 2455, 2479, 2551, 2595, 2655, 2701, 2773, 2805, 2901, 2943, 3003, 3043, 3143, 3175, 3277, 3325, 3373, 3425
"""






