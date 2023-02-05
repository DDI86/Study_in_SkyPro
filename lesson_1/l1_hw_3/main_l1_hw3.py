questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

count_right_answer = 0
percent_right_answer = 0
tottal_question = 0

if len(questions) < len(answers):
    tottal_question = len(questions)
else:
    tottal_question = len(answers)

ready_input = str.lower(input('Привет! Предлагаю проверить свои знания английского! Наберите "ready", чтобы начать!\n'))

if ready_input == "ready":
    for question_index in range(tottal_question):
        print(questions[question_index])
        user_answer = str.lower(input("Ваш ответ: "))
        if user_answer == answers[question_index]:
            print("Ответ верный!\n")
            count_right_answer += 1
        else:
            print(f"Неправильно. Правильный ответ: {answers[question_index]}\n")
    percent_right_answer = round((count_right_answer/tottal_question*100.2), 2)
    print(f"\nВот и все! Вы ответили на {count_right_answer} вопросов из {tottal_question} верно, это {percent_right_answer}.\n")
else:
    print("\nКажется, вы не хотите играть. Очень жаль.\n")

