# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

print('''
    Пункт A.''')
def remove_exclamation_marks(s):
    return s.replace('!', '')

stroka = "O!!h, no!!!"
print('foo(', stroka, ') -> ', remove_exclamation_marks(stroka), sep="")

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

print('''

    Пункт B.''')

def remove_last_em(s):
    if s[-1] == "!":
        s = s[: -1]
        return s
    else:
        return s

stroka = "O!!h, no!!!"
print('remove(', stroka, ') == ', remove_last_em(stroka), sep="")
    


# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"
# remove("Hi! !Hi! Hi! Hi!! Hi!") === "!Hi! Hi!!"

print('''

    Пункт C.''')

def remove_word_with_one_em(s):
    neo_s = s.split(" ")
    n_str = ""

    for elmnt in neo_s:
        for lttr in elmnt:
            if lttr == "!":
                cnt = elmnt.count(lttr)
        if cnt > 1:
            n_str += elmnt + " "

    return n_str

stroka = "Hi! !Hi! Hi! !Hi!! Hi! Hi!! H!i!"
print('remove(', stroka, ') === ', remove_word_with_one_em(stroka), sep="")

# Да, третий пункт, можно записать покороче

def remove_word_with_one_em(s):
    return ' '.join([w for w in s.split(' ') if w.count('!')!=1])

print(remove_word_with_one_em("Hi! Hi!! Hi!"))
