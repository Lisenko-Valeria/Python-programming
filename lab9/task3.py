n = int(input("Количество сокровищ: "))
tr = [] #treasure
d = [] #distances
print("Координаты сокровищ: ")
for i in range(n):
    tr.append(list(map(int, input().split())))
k = list(map(int, input("Координаты андрея: ").split()))
for i in range(n):
    d.append(((k[0]-tr[i][0])**2+(k[1]-tr[i][1])**2)**0.5)
print(*tr[d.index(min(d))])
'''4
1 2
3 5
5 6
7 8

2 3
'''