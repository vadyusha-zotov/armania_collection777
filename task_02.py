# Задача 2
# Создайте список "города" с именами любых городов
# Количество элементов в списке "города" не меньше 3!

# Создайте список списков населения перечисленных городов

# Выведите на консоль население второго города в списке в формате
# Население Москвы - ХХ человек

# Выведите на консоль общий размер населения перечисленных городов как сумму населения всех городов
# Итого размер населения - ХХ человек

city = [['Москва', 14], ['Питер', 8], ['Ереван', 1]]

print(f'Население города {city[1][0]} - {city[1][1]} Миллионов человек')
S = 0 
for i in city:
    S = S + int(i[1])
print(f'Итого размер населения - {S} миллионов человек')
