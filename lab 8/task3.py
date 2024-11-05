a = input().split()
for i in range(1, len(a)):
    if int(a[i]) > int(a[i-1]):
        print(a[i], end=" ")

#1 5 2 4 3