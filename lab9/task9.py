from random import*
def pr(m):
    for i in range(4):
        print(*m[i])

def check(i, j): # проверка для того, чтобы потом единичные корабли не ставились около других (вроде такое есть в правилах игры)
    ch = []
    if i<3:
        ch.append([i+1, j])
    if i>0:
        ch.append([i-1,j])
    if j>0:
        ch.append([i, j-1])
    if j<3:
        ch.append([i, j+1])
    if i<3 and j<3:
        ch.append([i+1, j+1])
    if i>0 and j>0:
        ch.append([i-1, j-1])
    if i<3 and j>0:
        ch.append([i+1, j-1])
    if i>0 and j<3:
        ch.append([i-1, j+1])
    return ch

def ships(m):
    ships = []
    while len(ships)!=4:
        tmp = [randint(0,3), randint(0,3)]
        ch = check(tmp[0], tmp[1])
        if (tmp not in ships) and (all(i not in ships for i in ch)):
            ships.append(tmp)
    return ships

def bomb():
    bomb = ships[0]
    while bomb in ships:
        bomb = [randint(0, 3), randint(0, 3)]
    return bomb

m = [["."]*4 for i in range(4)]
cnt = 0
tries = 0
ships = ships(m)
bomb = bomb()
pr(m)
#print("|", ships, bomb)
while cnt!=4:
    tries += 1
    k = list(map(int, input("Введите координаты: ").split()))
    if k in ships:
        print("вы попали")
        m[k[0]][k[1]]="x"
        cnt += 1
        pr(m)
    elif k==bomb:
        print("бомба, вы проиграли")
        break
    else:
        print("вы не попали")
        pr(m)
if cnt==4:
    print("победа, вам понадобилось ", tries, "попыток")