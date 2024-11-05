a = input().split()
l = []
d = []
for i in a:
    if i.isalpha():
        l.append(i)
    else:
        d.append(i)
print(*d)
print(*l)
#1 a 3 4 b 6