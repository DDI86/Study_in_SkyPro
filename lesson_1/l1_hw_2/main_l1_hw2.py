print("Привет! предлагаю проверить свои знания английского!\nРасскажи как тебя зовут!")

name = input(str())
line = "  "

print(f"Привет, {name}, начинаем тренировку!")

question = 0    # вопрос
answer = 0      # ответ
points = 0      # баллы

print("My name ___ Vova")
answer_1 = str(input())
if answer_1 == "is":
    question += 1
    answer += 1
    points += 10
    print("Ответ верный!\nВы получаете 10 баллов!")
else:
    question += 1
    print("Неправильно.\nПравильный ответ is")

print(line)

print("I ___ a coder")
answer_2 = str(input())
if answer_2 == "am":
    question += 1
    answer += 1
    points += 10
    print("Ответ верный!\nВы получаете 10 баллов!")
else:
    question += 1
    print("Неправильно.\nПравильный ответ am")

print(line)

print("I live ___ Moscow")
answer_3 = str(input())
if answer_3 == "in":
    question += 1
    answer += 1
    points += 10
    print("Ответ верный!\nВы получаете 10 баллов!")
else:
    question += 1
    print("Неправильно.\nПравильный ответ in")

print(line)

print(f"Вот и всё, {name}!\nВы ответили на {answer} вопросов из {question} верно.\nВы заработали {points} баллов.")
print("Это", round(answer/question*100, 2), "процентов")