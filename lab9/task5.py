from copy import*
#n, nn = map(int, input("Введите размер матрицы ").split())
#m = []
m = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]
n = 3
nn = 4
#for i in range(n):
#    m.append(list(map(int, input().split())))

def t(n,nn, m):
    if nn>n:
        for i in range(nn-n):
            m.append([0]*nn)
    elif n>nn:
        for i in range(n):
            for j in range(n-nn):
                m[i].append(0)

    mm = deepcopy(m)
    for i in range(nn):
        for j in range(n):
            mmm = deepcopy(mm)
            m[i][j] = mmm[j][i]

    if nn > n:
        for i in range(nn):
            for j in range(nn - n):
                del m[i][-1]
    elif n > nn:
        for j in range(n - nn):
            del m[-1]
    return m
m = t(n, nn, m)
for i in range(nn):
    print(*m[i])
