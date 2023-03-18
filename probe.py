letter = str
word = input("введите текст: ")

while letter != "стоп":
  letter = input("введите искомый символ (или стоп для выхода): ")
  count = 0
  nums = []
  pos = 0

  for L in word:
    pos += 1
    if L == letter:
      count = word.count(L)
      nums.append(pos)

  if letter == "стоп":
    print("поиск остановлен!")
    break
  elif count == 0:
    print("символа", letter, "нет в тексте")
  elif count != 0:
    nums = ', '.join(map(str, nums))
    print(nums)
    print("символ '", letter, "' встречается ", count, " раз(а) на ", nums, " позиции", sep="")
