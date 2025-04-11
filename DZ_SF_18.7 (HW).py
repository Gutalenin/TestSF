import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Удалить оценку ученика по предмету
        3. Вывести средний балл по всем предметам по каждому ученику
        4. Вывести все оценки по всем ученикам
        5. Добавить предмет
        6. Удалить предмет
        7. Добавить ученика
        8. Удалить ученика
        9. Редактировать ученика
        10. Редактировать предмет
        11. Оценки ученика
        12. Средний балл ученика
        13. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')

    elif command == 2:
        print('1. Удалить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys() and mark in students_marks[student][class_]:
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].remove(mark)
            print(f'Для {student} по предмету {class_} оценка удалена {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика, название предмета или оценки нет в списке')
    elif command == 3:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 4:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 5:
        print('Добавить предмет')
        class_ = input('Введите название предмета: ')
        if class_ not in classes:
            classes.append(class_)
            print(f'Предмет {class_} добавлен')
        else:
            print(f'Ошибка: предмет {class_} уже есть в базе')

    elif command == 6:
        print('Удалить предмет из списка')
        class_ = input('Введите название предмета: ')
        if class_  in classes:
            classes.remove(class_)
            print(f'Предмет {class_} удалён')
        else:
            print(f'Предмета {class_} нет в базе')

    elif command == 7:
        print('Добавить ученика')
        student = input('Введите имя: ')
        if student not in students:
            students.append(student)
            print(f'Ученик {student} добавлен в список')
        else:
            print('Ученик {student} уже есть в списке')

    elif command == 8:
        print('Удалить ученика')
        student = input('Введите имя: ')
        if student in students:
            students.remove(student)
            print(f'Ученик {student} удалён из списка')
        else:
            print(f'Ученика {student} нет в списке')

    elif command == 9:
        print('Редактировать ученика')
        student = input('Введите имя ученика: ')
        rename = input('Введите изменения: ')
        if student in students_marks.keys():
            students_marks[student] = rename

            print(f'Данные ученика {student} изменены на {rename}')
        else:
            print(f'Ошибка: ученик {student} не найден')

    elif command == 10:
        print('Редактировать предмет')
        class_ = input('Введите предмет: ')
        reclass = input('Введите изменения: ')
        if class_ in classes:
            students_marks[class_] = reclass
            print(f'Предмет {class_} изменён на {reclass}')
        else:
            print(f'Ошибка: предмет {class_} не найден')

    elif command == 11:
        print('Оценки ученика')
        student = input('Введите имя ученика: ')
        if student  in students:

            print(student)

            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
                print()
        else:
            print(f'Ошибка: ученика {student} нет в базе')

    elif command == 12:
        print('Средний балл ученика')
        student = input('Введите имя: ')
        if student in students:
            print(student)

            for class_ in classes:

                marks_sum = sum(students_marks[student][class_])

                marks_count = len(students_marks[student][class_])

                print(f'{class_} - {marks_sum // marks_count}')
                print()

    elif command == 13:
        print('4. Выход из программы')
        break