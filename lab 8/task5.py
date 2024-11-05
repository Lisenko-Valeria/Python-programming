g = list(map(int, input().split()))
a = int(input())
for i in range(len(g)):
    if a>g[i]:
        print(i+1)
        exit()
print(len(g)+1)


#215 207 196 176 168 166
#215 210 207
#176