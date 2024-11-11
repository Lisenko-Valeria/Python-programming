'''n, nn = map(int, input().split())
m = []
for i in range(n):
    m.append(list(map(int, input().split())))
k = int(input())'''
n = 5
nn = 5
m = [[0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 0, 0, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 0]]
k = 3
v = []
for i in range(n):
    for j in range(nn-k+1):
        if not(any(m[i][j:(j+k)])):
            v.append(i+1)
            break
print(min(v))
