# 2- Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Нужно написать таблицу истинности.

x = None
y = None
z = None
a_side = not (x or y or z)
b_side = not x and not y and not z
if a_side == b_side:
    print ('Истина')
else:
    print ('Ложь')

print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            result = a_side == b_side
            if result == True:
                print(x, y, z, result)