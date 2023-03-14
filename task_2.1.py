# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции max и min использовать нельзя!

def minimum(arr):
    n_lst = sorted(arr)
    return n_lst[0]

def maximum(arr):
    n_lst = sorted(arr)
    return n_lst[-1]

list = [4,6,2,1,9,63,-134,566]

mini = minimum(list)
maxi = maximum(list)

print(list, " -> max =", maxi, "min =", mini)

list = [-52, 56, 30, 29, -54, 0, -110]

mini = minimum(list)
maxi = maximum(list)

print(list, " -> max =", maxi, "min =", mini)

list = [42, 54, 65, 87, 0]

mini = minimum(list)
maxi = maximum(list)

print(list, " -> max =", maxi, "min =", mini)

list = [5]

mini = minimum(list)
maxi = maximum(list)

print(list, " -> max =", maxi, "min =", mini)

list = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]

mini = minimum(list)
maxi = maximum(list)

print(list, " -> max =", maxi, "min =", mini)

list = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]

mini = minimum(list)
maxi = maximum(list)

print(list, " -> max =", maxi, "min =", mini)
