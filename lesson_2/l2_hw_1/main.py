"""
    Полетели!!!!

    Основной модуль программмы в котором подключен модуль functions.
    По сути мы научились создавать свой модуль с фишечками и подгружать
    в main.

"""


import functions


def main():
    name = input('Введите ваше имя: ')

    words = functions.get_words('words.txt')
    point_counter = 0

    for word in words:
        shuffled_word = functions.shuffle_char_in_word(word)
        user_answer = input(f'Угадай слово: {shuffled_word}\nВаш ответ: ').lower()
        if user_answer == word:
            print('Верно! Вы получаете 10 очков!')
            point_counter += 10
        else:
            print(f'Неверно! Верный ответ - {word}')

    functions.save_user_result_in_history(name, point_counter)
    functions.print_statistics()


if __name__ == '__main__':
    main()
