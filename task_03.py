# Задача 4
# Вывести по номеру месяца кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

month = [31,28,31,30,31,30,31,31,30,31,30,31]
num = int (input('Введите номер месяца'))
AC = int(input('Сколько дней в этом месяце'))
if month [num-1] == AC:
    print('Верно')
else:
    print('Не верно')
