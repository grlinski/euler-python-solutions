
# XOR Decryption
# https://projecteuler.net/problem=59

"""

XOR Decryption

Convert to Letter
Convert to Byte
Find cipher.





XOR Cipher
https://www.youtube.com/watch?v=xK_SqWG9w-Y




Cipher is some binary number
00000000 to 11111111


Cipher is 3 characterslong
24 characters


Lowest
65
32 is space
Highest
122

[ 91
\ 92
] 93
^ 94
_ 95
` 96



a to z
97,122


"""

def aXORb(a,b):
    s = ''
    x = str(a)
    y = str(b)
    for i in range(0,len(x)):
        if x[i] == y[i]:
            s+='0'
        else:
            s+='1'
    return s



def convertToBin(x):
    b = bin(x)
    sb = str(b)
    sb = sb[2:]
    leng = 8-(len(sb))
    s = ''
    for i in range(0,leng):
        s+='0'
    ans = s+sb
    return ans

def binToInt(x):
    ans = int(str(x), 2)
    return ans
def intToChar(x):
    ans = char(x)
    return ans

#list1 = input().split(',')
#for i in list1:
#    convertToBin(int(i))


def flowControl(list1,a,b,c):





a = (convertToBin(65))
b = (convertToBin(42))
c = convertToBin(107)
k = aXORb(a,b)
print(a,b,c)

counter = 0
for i in range(97,123):
    for j in range(97,123):
        for k in range(97,123):
            print(i,j,k)
            counter+=1

print(counter)




