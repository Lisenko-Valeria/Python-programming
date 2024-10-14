a, b, c = int(input("введите 3 числа ")), int(input()), int(input())
if a==b and a==c:
    print("равносторонние")
elif (a==b or b==c or a==c) and not( a==c and a==b):
    print("равнобедренный")
else:
    print("разносторонние")