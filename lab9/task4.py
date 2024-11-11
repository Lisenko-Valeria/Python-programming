menu = [
["Пицца Маргарита", ["мука", "томаты", "сыр", "базилик"], 10],
["Салат Цезарь", ["салат", "курица", "сыр", "сухарики"], 8],
['Суп Томатный', ["томаты", "лук", "морковь", "картофель"], 6]
]
def pr(m):
    print("МЕНЮ:")
    for i in range(len(m)):
        print(m[i][0], ", (ингридиенты:", *m[i][1], ")", "цена:", m[i][2])
    print("\n")
def find(m):
    name = input("Введите название блюда для поиска: ")
    k = [i for i in range(3) if m[i][0]==name][0]
    print("ингридиенты:", *m[k][1], "цена:", m[k][2], "\n")
def new(m):
    m.append([])
    print("ВЫ ДОБАВЛЯЕТЕ НОВОЕ БЛЮДО!")
    m[3].append(input("Введите название блюда: "))
    m[3].append(input("Введите состав блюда: ").split())
    m[3].append(input("Введите стоимость блюда: "))
def change(m):
    print("ВЫ МЕНЯЕТЕ ЦЕНУ!")
    name = input("Введите название блюда: ")
    k = [i for i in range(3) if m[i][0] == name][0]
    m[k][2] = int(input("Введите новую цену: "))
    print("\n")

pr(menu)
find(menu)
new(menu)
pr(menu)
change(menu)
pr(menu)

