
# Permuted Multiples
#https://projecteuler.net/problem=52
#



def sameDigits(a,b,c,d,e,f):

    seta = set()
    setb = set()
    setc = set()
    setd = set()
    sete = set()
    setf = set()


    for i in range(0,len(str(a))):
        seta.add(a[i])
        setb.add(b[i])
        setc.add(c[i])
        setd.add(d[i])
        sete.add(e[i])
        setf.add(f[i])

    if seta == setb == setc == setd ==sete ==setf:
        return True

    return False


for i in range(1,1000000):


    #break
    x1 = i
    x2 = i * 2
    x3 = i * 3
    x4 = i * 4
    x5 = i * 5
    x6 = i * 6



    if len(str(x6)) == len(str(x1)) or len(str(x2)) == len(str(x1)):
        if sameDigits(str(x1),str(x2),str(x3),str(x4),str(x5),str(x6)):
            print(i)











#print(sameDigits('123','321','312','123','123','321'))




