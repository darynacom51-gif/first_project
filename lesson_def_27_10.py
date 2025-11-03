# Напишіть функцію, яка отримує ім’я і друкує вітальне повідомлення Hello, <name>.

# def name():
#     print("Hello, name!")

# name()

# name = "Daryna"

# def name_hello(name):     # вказали аргументи функції
#     print(f"Hello, {name}!")

# name_hello(name)      #викликає функцію



# def name_hello(name = "NON"):  # вказали аргументи функції за замовчуванням
#     print(f"Hello, {name}!")

# name_hello()




# name = "Daryna"

# def name_hello(name="NON"):
#     return f"Hello, {name}!"

# print(name_hello())
# print(name_hello(name))

#-------------------------------------------------------

# 2. Напишіть функцію, яка отримує рядок і ціле число n та повертає n копій заданого рядка.

# def copy_string(text, n):
#     return text * n

# text = input("Enter text: ")
# n = int(input("Enter n: "))

# print(copy_string(text, n))



# 3. Напишіть функцію для обчислення суми двох цілих чисел.

# def sum_a_b (a, b):
#     return a + b

# num_1 = int(input("Num 1 : "))
# num_2 = int(input("Num 2 : "))

# print(sum_a_b(num_1, num_2))



# 4. Напишіть функцію для отримання рядка з перших n символів іншого рядка. Якщо довжина рядка менше n, поверніть початковий рядок.

# def n_letter(word, n):
#     if len(word) < n:
#         return word
#     else:
#         return word[:n]
# print(n_letter("letter", 3))

# 5. Напишіть функцію для визначення найбільшого з трьох цілих чисел з використанянм вбудованої функції max().



# 6. Напишіть функцію для створення позначок тегів HTML навколо введених рядків. Функція отримує назву тега HTML і рядок, який необхідно помістити у відповідні теги.

# Вхідні дані: strong Python
# Вихідні дані: <strong>Python</strong>

# def teg_html(teg, text):
#     return f"<{teg}>{text}</{teg}>"

# text = input("Enter text: ")
# teg, string = text.split()

# print(teg_html(teg, string))

# 2 variant______________________________

# def teg_html(teg, text):
#     return f"<{teg}>{text}</{teg}>"

# text = input("Enter text: ")


# teg = text.split()[0]
# string = " ". join(text.split()[1:])

# print(teg_html(teg, string))


# 10. Напишіть функцію, яка отримує значення середньомісячної кількості опадів по місяцях (в мм) і повертає загальний обсяг опадів протягом року, середньорічну кількість опадів, назви місяців та значення з найвищим та найменшим числом опадів протягом року.

def rainfall_statatics(values):
    months = [
        "January", "February",
        "March", "April", "May",
        "June", "July", "August",
        "September", "October", "November",
        "December"
    ]

    rain = list(map(float, values.split()))

    total = sum(rain)

    average = total / 12 #len(rain) = 12
    max_rain = max(rain)
    min_rain = min(rain)

    max_month = months[rain.index(max_rain)]
    min_month = months[rain.index(min_rain)]

    return(total, average, (max_rain, max_month), (min_rain, min_month))

data = "22 22 24 49 72 98 101 82 51 40 36 24"

result = rainfall_statatics(data)
print(result)