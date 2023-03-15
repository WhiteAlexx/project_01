# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

#| 1|  2|  3|  4|  5|  6|  7|  8|  9| 10| 11| 12
#|31| 28| 31| 30| 31| 30| 31| 31| 30| 31| 30| 31

# Например, 
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

num_mnth = int(input('Введите номер месяца: '))

if num_mnth < 1 or num_mnth > 12:
    print('Такого месяца нет!')

elif num_mnth == 2:
    print('В этом месяце 28 дней')

elif num_mnth <= 7 and num_mnth % 2 == 1 or num_mnth >= 8 and num_mnth % 2 == 0:
    print('В этом месяце 31 день')

#elif num_mnth >= 8 and num_mnth % 2 == 0:
#    print('В этом месяце 31 день')

else:
    print('В этом месяце 30 дней')


print('''
    
    Вариант с названием месяца
    ''')

def select_month(number):
    months = {
        1: "Январь",
        2: "Февраль",
        3: "Март",
        4: "Апрель",
        5: "Май",
        6: "Июнь",
        7: "Июль",
        8: "Август",
        9: "Сентябрь",
        10: "Октябрь",
        11: "Ноябрь",
        12: "Декабрь"
    }
    name_mnth = months[number]
    return name_mnth

num_mnth = int(input('Введите номер месяца: '))

if num_mnth < 1 or num_mnth > 12:
    print('Такого месяца нет!')

elif num_mnth == 2:
    name_mnth = select_month(num_mnth)
    print('Выбран ', name_mnth, '. В этом месяце 28 дней', sep="")

elif num_mnth <= 7 and num_mnth % 2 == 1 or num_mnth >= 8 and num_mnth % 2 == 0:
    name_mnth = select_month(num_mnth)
    print('Выбран ', name_mnth, '. В этом месяце 31 день', sep="")

else:
    name_mnth = select_month(num_mnth)
    print('Выбран ', name_mnth, '. В этом месяце 30 дней', sep="")