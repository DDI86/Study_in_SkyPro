import json

from cfg import STUDENTS_PATH, PROFESSIONS_PATH


# Загрузка данных о студентах из файла
def load_students():
    with open(STUDENTS_PATH, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


# Загрузка данных о профессиях из файла
def load_professions():
    with open(PROFESSIONS_PATH, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


# Получение данных о студенте по его номеру
def get_students_by_pk(pk):
    students = load_students()
    for student in students:
        if student.get('pk') == pk:
            return student


# Получение данных о профессии по её названию
def get_professions_by_title(title):
    professions = load_professions()
    for profession in professions:
        if profession.get('title') == title.title():
            return profession


# Поиск соответсвий между студнтами и профессиями
def check_fitness(student, profession):
    student_skills = set(student['skills'])
    profession_skills = set(profession['skills'])

    has_skills = student_skills.intersection(profession_skills)
    lacks_skills = profession_skills.difference(has_skills)

    has_percent = round(len(has_skills) / len(profession_skills) * 100)

    return {
        'has': list(has_skills),
        'lacks': list(lacks_skills),
        'fit_percent': has_percent,
    }
