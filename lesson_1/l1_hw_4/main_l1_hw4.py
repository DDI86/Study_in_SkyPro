# уровень лёгкий
words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

# уровень средний
words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

# уровень сложный
words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

# уровень владения переводом
levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}

answers = {}

print("выберите уровень сложности:\nЛегкий, средний, сложный")

levels_dict = {
    "легкий": words_easy,
    "средний": words_medium,
    "сложный": words_hard,
}

while True:
    level = input().lower()
    if level in levels_dict.keys():
        break
    print('Неверный уровень сложности')

words = levels_dict[level]

for key, value in words.items():
    print(f'{key}, {len(value)}, начинается на {value[0]}')
    answer = input()
    if answer == value:
        print(f'Верно, {key} - это {value}.')
    else:
        print(f'Неверно. {key} - это {value}.')
    answers[key] = answer == value


print(f'Правильно отвеченные слова: ')
for word, result in answers.items():
    if result is True:
        print(word)


print(f'Неравильно отвеченные слова: ')
for word, result in answers.items():
    if result is False:
        print(word)


true_answers = []
for answer in answers.keys():
    if answers[answer]:
        true_answers.append((answer))

print(f'Ваш ранг: {levels[len(true_answers)]}')
