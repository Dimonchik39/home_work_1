# 2- Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Нужно написать таблицу истинности.

X = int(input("Введите значение X: "))
Y = int(input("Введите значение Y: "))
Z = int(input("Введите значение Z: "))
num = [X, Y, Z]

def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[2] and not x[2] and not x[2]
    result = left == right
    return result

if checkPredicate(num) == True:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")
