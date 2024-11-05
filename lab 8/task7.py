a = list(map(int, list(input())))
s = 0
for i in range(0, len(a), 2):
    if a[i]*2>9:
        s += a[i]*2-9
    else:
        s += a[i]*2

for i in range(1, len(a), 2):
    s += a[i]
if s%10==0:
    print("Корректный номер")
else:
    print("Некорректный номер")

#4276440013361511 - yes
#4276440013361512 - no