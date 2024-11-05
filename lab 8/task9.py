n = int(input())
cnt = 0
for i in range(n):
    a, b = map(int, input().split())
    if (b-a)>=2:
        cnt += 1
print(cnt)

'''
3
1 1
2 2
3 3
''''''
3
1 10
0 10
10 10
'''