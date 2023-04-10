import random
import datetime

# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

print('''
task AC''')

rnd_sngs = random.sample(my_favorite_songs, k=3)
lst_sngs = rnd_sngs[0][0] + ', ' + rnd_sngs[1][0] + ', ' + rnd_sngs[2][0]
sum_sngs = round(rnd_sngs[0][-1] + rnd_sngs[1][-1] + rnd_sngs[2][-1])
print(lst_sngs, ' звучат ', sum_sngs, 'минут')

print('''
task AD''')

mnt_1sng = int(rnd_sngs[0][-1])
scn_1sng = int((rnd_sngs[0][-1] - mnt_1sng) * 100)
mnt_2sng = int(rnd_sngs[1][-1])
scn_2sng = int((rnd_sngs[1][-1] - mnt_2sng) * 100)
mnt_3sng = int(rnd_sngs[2][-1])
scn_3sng = int((rnd_sngs[2][-1] - mnt_3sng) * 100)

sum_scn = scn_1sng + scn_2sng + scn_3sng
sum_mnt = mnt_1sng + mnt_2sng + mnt_3sng + sum_scn // 60

print(lst_sngs, ' звучат ', datetime.time(0, sum_mnt, sum_scn % 60).strftime('%M:%S'), 'минут')


# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}


print('''
task BC''')

rnd_sngs = random.sample(sorted(my_favorite_songs_dict), k=3)
lst_sngs = rnd_sngs[0] + ', ' + rnd_sngs[1] + ', ' + rnd_sngs[2]
sum_sngs = round(my_favorite_songs_dict[rnd_sngs[0]] + my_favorite_songs_dict[rnd_sngs[1]] + my_favorite_songs_dict[rnd_sngs[2]])
print(lst_sngs, ' звучат ', sum_sngs, 'минут')

print('''
task BD''')

mnt_1sng = int(my_favorite_songs_dict[rnd_sngs[0]])
scn_1sng = int((my_favorite_songs_dict[rnd_sngs[0]] - mnt_1sng) * 100)
mnt_2sng = int(my_favorite_songs_dict[rnd_sngs[1]])
scn_2sng = int((my_favorite_songs_dict[rnd_sngs[1]] - mnt_2sng) * 100)
mnt_3sng = int(my_favorite_songs_dict[rnd_sngs[2]])
scn_3sng = int((my_favorite_songs_dict[rnd_sngs[2]] - mnt_3sng) * 100)

sum_scn = scn_1sng + scn_2sng + scn_3sng
sum_mnt = mnt_1sng + mnt_2sng + mnt_3sng + sum_scn // 60

print(lst_sngs, ' звучат ', datetime.time(0, sum_mnt, sum_scn % 60).strftime('%M:%S'), 'минут')

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime

# Ну так можно да)
# у меня было немного другое решение
from datetime import timedelta
from math import modf
from random import sample


total_time = timedelta()

for song in sample(my_favorite_songs, 3):
    s, m = modf(song[1])
    total_time += timedelta(minutes=int(m), seconds=int(s * 100))

print(f'Три песни звучат {total_time} минут')
