from random import*
a = ''
while ('PPP' not in a) and ('OOO' not in a):
    a += choice(["O", "P"])
print(a, "(попыток:", len(a), ")")