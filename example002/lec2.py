#Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. Примечание:
#Используйте знания об Алгебра Логике, вы должны перебрать все возможные комбинации значений X, Y, Z (принимают значения 0 или 1)
result = True
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            print(f"{x = } {y = } {z = }  {not(x or y or z) == (not x and not y and not z)}")