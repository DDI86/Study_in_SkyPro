# Импорт модулей
import random


# Словарь, переменные
dictionary_morse = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}
words = ["code", "bit", "list", "soul", "next"]
answers = []
count_answers = 1


# функция свободного выбора слова из words
def get_word():
    random_word = random.choice(words)
    return random_word


# функция шифрования слова
def morse_encrypt(word_get):
    word_encrypted = " "
    for letter in word_get:
        word_encrypted += dictionary_morse[letter] + " "
    return word_encrypted


# Функция статистики
def print_statistics(answers_get):
    count_true = 0
    count_false = 0
    for meaning in answers_get:
        if meaning == "True":
            count_true += 1
        else:
            count_false += 1
    return f"Всего задачек: {len(answers)}\nОтвечено верно: {count_true}\nОтвечено не верно: {count_false}"


# Старт программы
input("Сегодня мы потренируемся расшифровать азбуку Морзе\nНажмите Enter и начнём\n")


for i in range(len(words)):
    word = get_word()
    print(f'Слово {count_answers} -  {morse_encrypt(word)}' '')
    answer = input().strip().lower()
    count_answers += 1
    if answer == word:
        answers += "True".split(' ')
        print(f'Верно, {word}!')
    else:
        answers += "False".split(' ')
        print(f'Неверно, {word}!')


# Вывод статистики
print(print_statistics(answers))
