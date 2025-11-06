# 1. Створіть словник зі списками добрих справ на сьогодні і на завтра. Надрукуйте із словника добрі справи, які плануєш зробити сьогодні і взавтра.

def task1():

    to_do =  { #словник
        "today": ["read", "clear", "dog"],# ключ today
        "tomorrow": ["read", "call my mom"]
    } 

    #print(to_do)
    print("To do for today")
    for item in to_do["today"]:
        print("-", item)

    print("To do for tomorrow")
    for item in to_do["tomorrow"]:
        print("--", item)

#task1()

# 2. Припустимо, що у нас є словник, в якому ключі є ідентифікаторами, а значення – іменами користувачів. Напишіть програму, яка виводить вітальне повідомлення користувачу на основі його ідентифікатора. Якщо ідентифікатор відсутній у словнику, виводиться вітання для усіх користувачів.

# users = {
#     0: "Alice",
#     1: "Bob",
#     2: "Jack"
# }

# user_id = int(input("Your id: "))
# if user_id in users:
#     print(f"Hello, {users[user_id]}")
# else:
#     print("Hello everybody!")

# 3. Напишіть програму для сортування за зростанням (за алфавітом) словника за ключами. Словник зберігає пари ключ-значення у вигляді «назва фільму: рік релізу». Інформація виводиться як у вихідних даних: сортування має бути проведено за назвами фільмів.

# Вихідні дані: ('Avengers: Endgame', 2019) ('Guardians of the Galaxy', 2014) ('Iron Man', 2008) ('Thor', 2011)

def task3():
    films = {
        'Thor': 2011,
        'Iron Man': 2008,
        'Guardians of the Galaxy': 2014,
        'Avengers: Endgame': 2019
    }
    sorted_films = dict(sorted(films.items()))

    for name, year in sorted_films.items():
        print(f" ('{name}': {year})")

#task3()

# 4. Надрукуйте елементи словника, де ключі - це числа від '1' до 'n' (обидва числа включно), а значення - квадрати ключів. 'n' – ціле число, яке вводить користувач.
def task4():
    n = int(input("n: "))

    squares = {}    #порожній словник

    for i in range(1, n+1):
        # dict[key] = value 
        squares[i] = i ** 2

    print(squares)

# 5. Створіть словник, в кому ключі – назви днів тижня, а значення - цілі числа, що позначають порядковий номер дня тижня від 0 до 6. Надрукуйте назву дня за введеним порядковим номером дня. Якщо введений номер виходить за межі, програма жодних повідомлень не друкує і не повідомляє про помилку.

# weeks = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# days = [i for i in range(7)]

# # week_dict = {}
# # for day in range(7):
# #     week_dict[weeks[day]] = days[day]

# week_dict


# 6 . Напишіть програму для створення словника із введеного рядка символів для підрахунку кількості символів.
def task_6():
    text = "Lorem ipsum dolor sit amet" # створюємо змінну text і присвоюємо їй рядок із текстом
    text = list(text) # перетворюємо рядок у список символів, щоб кожна літера і пробіл стали окремими елементами

    letters = {i: text.count(i)# створюємо словник: ключ — символ, значення — кількість його повторень у списку
            for i in text}# проходимо по кожному символу в списку text

    print(letters) # виводимо отриманий словник із підрахованими символами на екран

    # for key in [1, 2, 3]:
    #     d[key] = 0

# 7. Напишіть програму, яка приймає рядок символів, і обчислює кількість букв і цифр.
def task_7():
    text = "Project Gutenberg offers over 59,000 free eBooks"

    number_count = 0
    alpha_count = 0

    for ch in text:
        if ch.isdigit():
            number_count += 1
        elif ch.isalpha():
            alpha_count += 1

    result = {
        "LETTERS": alpha_count,
        "DIGITS" : number_count
    }

    # print(result)
    for key, value in result.items():
        print(key, value)


# 10. Дано два списки чисел. Порахуйте, скільки унікальних цифр міститься в обох з них.
def task_10():
    numbers_1 = [1, 5, 3, 8, 0, 1]
    numbers_2 = [23, 9, 0, 1, 5]

    result = len(set(numbers_1 + numbers_2))

# ------------------------------------
#об'єднання множин
# numbers_1 = {1, 5, 3, 8, 0, 1}
# numbers_2 = {23, 9, 0, 1, 5}

# print(numbers_1.union(numbers_2))   # a | b
# print(numbers_1 | numbers_2)

# # A - B = A (без B)
# print(numbers_1.difference(numbers_2))
# print(numbers_1 - numbers_2)


# print(numbers_1.symmetric_difference(numbers_2))
# print(numbers_1 ^ numbers_2)




#****************************************************


