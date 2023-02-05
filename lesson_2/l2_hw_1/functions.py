"""
    ФУНКЦИИ, КОТОРЫЕ ВЫ МОЖЕТЕ ПОДСМОТРЕТЬ В ЭТОМ ФАЙЛЕ:

1.  Импорт модуля (random).
2.  Читаем некий файл построчно в кодировке  UTF-8 и возвращаем из него слово.
3.  Волшебным образом перемешиваем буквы и возвращем набор символов.
4.  Сохраняем статистику игр в вайл history.txt в кодировке UTF-8 в корневой каталог программы.
5.  Выводим статистику путём чтения файла history.txt в кодировке UTF-8

"""


# 1. Импорт модуля (random).
import random


# 2. Читаем некий файл построчно в кодировке  UTF-8 и возвращаем из него слово.
def get_words(filenames):
    with open(filenames, 'r', encoding='utf-8') as f:
        words = f.read().splitlines()
    return words


# 3. Волшебным образом перемешиваем буквы и возвращем набор символов.
def shuffle_char_in_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)


# 4. Сохраняем статистику игр в вайл history.txt в кодировке UTF-8 в корневой каталог программы.
def save_user_result_in_history(user_name, points):
    with open('history.txt', 'a', encoding='utf-8') as f:
        f.write(f'{user_name} {points}\n')


# 5. Выводим статистику путём чтения файла history.txt в кодировке UTF-8
def print_statistics():
    with open('history.txt', 'r', encoding='utf-8') as f:
        data = f.read().splitlines()
        total_count_games = len(data)
        points_list = list()

        for note in data:
            user_name, points = note.split(' ')
            points_list.append(points)

        max_record = max(points_list)
        print(f'Всего игр сыграно: {total_count_games}\nМаксимальный рекорд: {max_record}')
