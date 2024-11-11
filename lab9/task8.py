n, nn = map(int, input().split())
m = [[1]*nn for i in range(n)]
for i in range(1, n):
    for j in range(1, nn):
        m[i][j]=m[i][j-1]+m[i-1][j]
for i in range(n):
    print(*m[i])
#4 6
