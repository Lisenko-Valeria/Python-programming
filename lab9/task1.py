def func(x):
    return  x**2 / (10 + x**3)
a = -2
b = 5
def sq(N): #N-количество шагов
    h = (b - a)/N #длина шага по х
    f = [] # все y
    i = a # x, на данный момент слева направо
    while i < (b):
        f.append(func(i))
        i += h
    sum = 0
    for i in f:
        sum += h * i
    print(h/2*(func(0)+func(N-1))+sum)
sq(10)
sq(100)
sq(1000)

