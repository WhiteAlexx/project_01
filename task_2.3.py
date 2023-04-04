# Задача 2.3.

def switch_it_up0(number):
    lst_nmb = [
        [0, "'Ноль'"],
        [1, "'Один'"],
        [2, "'Два'"],
        [3, "'Три'"],
        [4, "'Четыре'"],
        [5, "'Пять'"],
        [6, "'Шесть'"],
        [7, "'Семь'"],
        [8, "'Восемь'"],
        [9, "'Девять'"]
    ]

    while number >= 0 and number <= 9:
        nm_nmb = lst_nmb[number][1]
        return nm_nmb
    return None

print('''
    Вариант со списком
    ''')
numb = int(input("Введите число: "))

rtrn_nmb = switch_it_up0(numb)

print("switch_it_up(", numb, ") -> ", rtrn_nmb, sep="")




# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

def switch_it_up(number):
    match number:
        case 0:
            ret_num = "'Ноль'"
            return ret_num
        case 1:
            ret_num = "'Один'"
            return ret_num
        case 2:
            ret_num = "'Два'"
            return ret_num
        case 3:
            ret_num = "'Три'"
            return ret_num
        case 4:
            ret_num = "'Четыре'"
            return ret_num
        case 5:
            ret_num = "'Пять'"
            return ret_num
        case 6:
            ret_num = "'Шесть'"
            return ret_num
        case 7:
            ret_num = "'Семь'"
            return ret_num
        case 8:
            ret_num = "'Восемь'"
            return ret_num
        case 9:
            ret_num = "'Девять'"
            return ret_num
        case _:
            return None

print('''
    Вариант с кейсом
    ''')

numb = int(input("Введите число: "))

rtrn_nmb = switch_it_up(numb)

print("switch_it_up(", numb, ") -> ", rtrn_nmb, sep="")

#  Да) со switch-case вообще отлично))
# у меня как всегда словари)

def switch_it_up(number):
    return {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}.get(number)
