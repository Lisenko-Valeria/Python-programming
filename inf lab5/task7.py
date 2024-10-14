a = input("введите номер машины ")
if a[:3].isalpha() and a[:3].isupper() and a[3:6].isdigit():
    print("старый номер")
elif a[:4].isdigit() and a[4:7].isalpha() and a[4:7].isupper():
    print("новый номер")
else:
    print("не номер")

#old AAA111
#new 1111AAA