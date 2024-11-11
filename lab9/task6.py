#n = int(input())
#m = []
n = 3
#for i in range(n):
#    m.append(list(map(int, input().split())))
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(n):
    tmp = m[i][i]
    m[i][i] = m[-1-i][i]
    m[-1-i][i] = tmp

for i in range(n):
    print(*m[i])