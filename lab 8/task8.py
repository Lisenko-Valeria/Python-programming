n = int(input())
itog = []
for i in range(n):
    a = input()
    if len(a)<=10:
        itog.append(a)
    else:
        a = a[0] + str(len(a[1:-1])) + a[-1]
        itog.append(a)
print(*itog, sep="\n")

'''3
word
localization
internationalization
'''
