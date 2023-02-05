from basic_word import BasicWord
from player import Player
from utils import load_random_word


def main():

    print('Введите имя игрока')
    user_input = input()
    player = Player(user_input)
    print(f'Привет {player.get_name()}!')

    random_word = load_random_word()
    full_word = random_word.get('word')
    sub_words = random_word.get('subwords')
    basic_word = BasicWord(full_word, sub_words)
    subwords_max_count = basic_word.get_subwords_count()

    print(f'Исходное слово: {basic_word.get_word_capitalised()}\nМожно составить {subwords_max_count} слов')

    print(f'Слова должны быть не короче 3х букв')
    print(f'Чтобы закончить игру, угадайте все слова или напишите stop')
    print(f'Поехали, ваше первое слово')

    while True:

        user_input = input()

        used_count = player.get_used_words_count()

        if used_count == subwords_max_count:
            print(f'Слова закончились, игра завершена!')
            print(f'Вы угадали {used_count} слов')
            break

        if user_input == 'стоп':
            print(f'Вы остановили игру, игра завершена!')
            print(f'Вы угадали {used_count} слов')
            break

        is_subword = basic_word.has_subwords(user_input)
        was_used = player.is_word_used(user_input)

        if is_subword and not was_used:
            print('Верно!')
            player.add_word(user_input)
        else:
            print('Неверно!')


main()
