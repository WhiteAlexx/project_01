# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:


import sqlite3

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

#connection = sqlite3.connect('teatchers.db')
#cursor = connection.cursor()
#query = """CREATE TABLE Students (
#Student_Id INTEGER NOT NULL,
#Student_Name TEXT NOT NULL,
#School_Id INTEGER NOT NULL PRIMARY KEY
#);
#"""
#cursor.execute(query)
#connection.commit()
#connection.close()


# Наполните таблицу следующими данными:

#connection = sqlite3.connect('teatchers.db')
#cursor = connection.cursor()
#query = """INSERT INTO Students (Student_Id , Student_Name , School_Id)
#VALUES
#('201', 'Иван', '1'),
#('202', 'Петр', '2'),
#('203', 'Анастасия', '3'),
#('204', 'Игорь', '4');
#"""
#cursor.execute(query)
#connection.commit()
#connection.close()

def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()


def get_school_name(school_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """SELECT * FROM School WHERE School_Id = ?"""
    cursor.execute(select_query,(school_id,))
    record = cursor.fetchone()
    close_connection(connection)
    return record[1]
  except (Exception, sqlite3.Erorr) as erorr:
    print ("Ошибка в получении данных", erorr)


def get_student(Student_Id):
  try:
    
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """SELECT * FROM Students WHERE Student_Id = ?;"""
    cursor.execute(select_query,(Student_Id,))
    records = cursor.fetchall()
    school_id = records[0][2]
    school_name = get_school_name(school_id)
    print ("Данные по студентам", records)
    for row in records:
      print ("ID студента: ", row[0])
      print ("Имя студента: ", row[1])
      print ("ID школы: ", row[2])
      print ("Название школы: ", school_name)
  except (Exception, sqlite3.Erorr) as erorr:
    print ("Ошибка в получении данных", erorr)

print ("Задача 4.1. Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте")

get_student(202)