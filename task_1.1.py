# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.
spltd_sngs = my_favorite_songs.split(', ')
print(spltd_sngs[0], spltd_sngs[-1], spltd_sngs[1],spltd_sngs[-2])

# Ну этот вариант самый годный) да

print('''


#а это был первый вариант решения''')
nums = []
pos = 0

for smbl in my_favorite_songs:
  pos += 1
  if smbl == ',':
    nums.append(pos)

print(my_favorite_songs[:nums[0] - 1])
print(my_favorite_songs[nums[-1] + 1:-1])
print(my_favorite_songs[nums[0] + 1:nums[1] - 1])
print(my_favorite_songs[nums[1] + 1:nums[2] - 1])
