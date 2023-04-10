# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - проявите фантазию :)


import random

class MatrixForGame:
    '''Игровая матрица'''

    def __init__(self) -> None:

        clmns = 5
        rws = 5

        slct = random.randint(0, 1)
        if slct == 0:
            nmbr, chng = 96, 69
        else:
            nmbr, chng = 69, 96
        
        square = clmns * rws
        pos_chng = random.randint(1, square)

        cl_chng = pos_chng % clmns
        if cl_chng == 0:
            cl_chng = clmns - 1
            rw_chng = pos_chng // clmns - 1
        else:
            cl_chng -= 1
            rw_chng = pos_chng // clmns

        matrix = []
        while rws != 0:
            matrix.append(list(range(0, clmns)))
            rws -= 1
            
        indx_r = 0
        for r in matrix:
            indx_c = 0
            if indx_r == rw_chng:
                for c in matrix[indx_r]:
                    if indx_c == cl_chng:
                        matrix[indx_r][indx_c] = chng
                    else:
                        matrix[indx_r][indx_c] = nmbr
                    indx_c += 1
            else:
                for c in matrix[indx_r]:
                    matrix[indx_r][indx_c] = nmbr
                    indx_c += 1
            indx_r += 1
        self.cntnt = matrix

    def get_content_for_matrix(self, ch_clmns, ch_rws):
        slct = random.randint(0, 1)
        if slct == 0:
            nmbr, chng = 96, 69
        else:
            nmbr, chng = 69, 96

        mtrx.get_count_rows_columns(mtrx.cntnt)
        
        clmns = mtrx.size[1] + ch_clmns
        rws = mtrx.size[0] + ch_rws
        square = clmns * rws
        pos_chng = random.randint(1, square)

        cl_chng = pos_chng % clmns
        if cl_chng == 0:
            cl_chng = clmns - 1
            rw_chng = pos_chng // clmns - 1
        else:
            cl_chng -= 1
            rw_chng = pos_chng // clmns

        matrix = []
        while rws != 0:
            matrix.append(list(range(0, clmns)))
            rws -= 1

        indx_r = 0
        for r in matrix:
            indx_c = 0
            if indx_r == rw_chng:
                for c in matrix[indx_r]:
                    if indx_c == cl_chng:
                        matrix[indx_r][indx_c] = chng
                    else:
                        matrix[indx_r][indx_c] = nmbr
                    indx_c += 1
            else:
                for c in matrix[indx_r]:
                    matrix[indx_r][indx_c] = nmbr
                    indx_c += 1
            indx_r += 1
        self.cntnt = matrix

    def get_count_rows_columns(self, cntnt):
        rows = len(cntnt)
        columns = len(cntnt[0])
        self.size = [rows, columns]


print("""
    ИГРА "ПЕРЕВЕРТЫШ"
    Найди перевернутое число
    """)

mtrx = MatrixForGame()
mtrx.get_count_rows_columns(mtrx.cntnt)
print("Наша матрица из", mtrx.size[0], "строк и", mtrx.size[1], "колонок:")
indx_r = 0
for r in mtrx.cntnt:
  print(' '.join(map(str, mtrx.cntnt[indx_r])))
  indx_r += 1

neo_game = "y"

while neo_game == "y":
    
    print("""
        Сыграем еще раз!
        Теперь введите числа, на которые
        изменится наша игровая матрица.
        Перевернутое число будет в случайной ячейке.
        """)

    ch_clmns = int(input("Насколько изменится количество колонок матрицы: "))
    while 1 == 1:
        try:
            if mtrx.size[1] + ch_clmns< 2:
                print("Нельзя сделать матрицу из 1 колонки или меньше!")
                ch_clmns = int(input("Насколько изменится количество колонок матрицы: "))
            else:
                break
        except ValueError:  #почему-то не работает перехват ошибки ValueError
            print("Нужно вводить число!")
            ch_clmns = int(input("Насколько изменится количество колонок матрицы: "))       

    ch_rws = int(input("Насколько изменится количество строк матрицы: "))
    while 1 == 1:
        try:
            if mtrx.size[0] + ch_rws < 2:
                print("Нельзя сделать матрицу из 1 строки или меньше!")
                ch_rws = int(input("Насколько изменится количество строк матрицы: "))
            else:
                break
        except ValueError:  #почему-то не работает перехват ошибки ValueError
            print("Нужно вводить число!")
            ch_rws = int(input("Насколько изменится количество строк матрицы: "))      

    mtrx.get_content_for_matrix(ch_clmns, ch_rws)
    mtrx.get_count_rows_columns(mtrx.cntnt)
    print("""
        Наша матрица из""", mtrx.size[0], "строк и", mtrx.size[1], "колонок:")
    indx_r = 0
    for r in mtrx.cntnt:
        print(' '.join(map(str, mtrx.cntnt[indx_r])))
        indx_r += 1

    neo_game = input("""
    Сыграем еще раз? (y/n): """)

    while neo_game != "y" or neo_game != "n":
        if neo_game == "y" or neo_game == "n":
            break
        else:
            print("Введите корректный ответ")
            neo_game = input("""
                Сыграем еще раз? (y/n): """)
            
