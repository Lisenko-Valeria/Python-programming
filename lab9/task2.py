from copy import*
from random import*

def pr(m):
    for i in range(3):
        print(*m[i])

def turn(m):
    mm = deepcopy(m)
    mm = mm[::-1]
    for i in range(3):
        for j in range(3):
            mmm = deepcopy(mm)
            m[i][j] = mmm[j][i]
    return m

def mat3(): #я не видела заготовку, так что квадрат формировался по алгоритму https://www.wikihow.com/Solve-a-Magic-Square
    m = [[0]*3 for i in range(3)]
    cnt = 1
    m[0][1] = cnt
    start_line = 0
    start_column = 1
    while cnt<9:
        cnt += 1
        start_line = start_line - 1 if (start_line != 0) else 2
        start_column = start_column + 1 if (start_column != 2) else 0
        if m[start_line][start_column]==0:
            m[start_line][start_column] = cnt
        else:
            start_line = start_line -1 if (start_line != 0) else 2
            start_column = start_column - 1 if (start_column != 0) else 2

            m[start_line][start_column] = cnt
    return m

x = randint(1,10)
n = randint(1,4)
y = choice(["+", "*"])
m = mat3()
for i in range(n):
    turn(m)
if y=="+":
    for i in range(3):
        for j in range(3):
            m[i][j] += x
else:
    for i in range(3):
        for j in range(3):
            m[i][j] *= x
pr(m)





