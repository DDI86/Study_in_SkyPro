import functions


# Получаем данные о студенте
print('Введите номер студента')
student_id = input()
for i in student_id:
        if i.isdigit() is not True:
            raise ValueError("Должны быть введены только цифры!")

student = functions.get_students_by_pk(student_id)

if not student:
    print('У нас нет такого студента')
    quit()

# Собираем информацию о студенте, его знаниях
student_name = student['full_name']
student_skills = ' '.join(student['skills'])
student_learns = ' '.join(student['learns'])

# Ввод информации о знаниях
print(f'Студент {student_name}')
print(f'Занает {student_skills}')

# Получаем данные о профессии
print(f'Выберите специальность для оценки студента {student_name}')
profession_title = input()
profession = functions.get_professions_by_title(profession_title)

if not profession:
    print('У нас нет такой профессии')
    quit()

# Сравнениваем данные
fitness = functions.check_fitness(student, profession)

# Извлекаем данные из полученного словаря
fit_percent = fitness['fit_percent']
has = fitness['has']
lacks = fitness['lacks']


# Вывод результатов
print(f'Пригодность {fit_percent}%')
print(f'Студент знает {" ".join(has)}')
print(f'Студент не знает {" ".join(lacks)}')

