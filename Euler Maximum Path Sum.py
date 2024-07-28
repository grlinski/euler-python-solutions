
q = []

for i in range(100):

    s = list(map(int, input().strip().split(' ')))
    q.append(s)

print(q[::-1])

for i in range(98,-1,-1):
    for j in range(len(q[i])):
        print(q[i][j])

        x = max(q[i+1][j],q[i+1][j+1])
        q[i][j]+=x


print(q[0])