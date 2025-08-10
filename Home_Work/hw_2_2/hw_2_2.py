correct_answer_1 = "is"
correct_answer_2 = "am"
correct_answer_3 = "in"
count = 0
count_1 = 0
result_1 = ("Введите ваш ответ: \n")
result_2 = ("Неправильно.\nПравильный ответ:")

print("Привет! Предлагаю проверить свои знания английского!")
name = input("Напиши, как тебя зовут \n")
print("Привет,", name, "начинаем тренировку!")

print("__________\nВопрос 1: Mi name ___ Vova.")
answer_1 = input(result_1)
if answer_1 == correct_answer_1:
    count += 10
    count_1 += 1
    print("Ответ верный!\nВы получаете", count, "баллов!")
else:
    print(result_2, correct_answer_1)

print("__________\nВопрос 2: I ___ a coder.")
answer_2 = input(result_1)
if answer_2 == correct_answer_2:
    count += 10
    count_1 += 1
    print("Ответ верный!\nВы получаете", count, "баллов!")
else:
    print(result_2, correct_answer_2)

print("__________\nВопрос 3: I love ___ Moscow.")
answer_3 = input(result_1)
if answer_3 == correct_answer_3:
    count += 10
    count_1 += 1
    print("Ответ верный!\nВы получаете", count, "баллов!")
else:
    print(result_2, correct_answer_3)

print(f"__________\nВот и все, ", name, "!\nВы ответили на ", count_1, "вопросов из 3 верно.")
print(f"Вы заработали ", count, "баллов.\nЭто ", round(count_1/3 * 100, 2), "процентов.")