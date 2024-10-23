grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]  # - Список оценок
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}                        # - Множество из списка учеников

students = list (students)                                                          # - Преобразуем множество в список

students.sort()                                                                     # - Сортируем по порядку

book = {students [0] : (sum (grades[0])) / (len (grades[0])) ,                      # - Находим средний бал и создаем словарь
        students [1] : (sum (grades[1])) / (len (grades[1])) ,                      # - обращаясь к данным по индексу
        students [2] : (sum (grades[2])) / (len (grades[2])) ,
        students [3] : (sum (grades[3])) / (len (grades[3])) ,
        students [4] : (sum (grades[4])) / (len (grades[4])) }

print(book)                                                                         # - Выводим на печать результат.