# [1, "a", 2.0]
# list()

#1
# value = "1 2 65 40 34 6 96 2 94 3"
# # value.split()
# value_list = list(map(int, value.split()))
# print(value_list[len(value_list)//2:])

#2
# value = "1 2 65 40 34 6 96 2 94 3"
# value_list = list(map(int, value.split()))
# v_12 = value_list[:-2]
# print(v_12)




# 3. Збережіть назви мов світу, які вводяться в одному рядку через пропуск, у списку. Простежте за тим, щоб елементи у списку не зберігались в алфавітному порядку. Відсортуйте список в алфавітному порядку і виведіть його елементи в рядку через пропуск.
def task_3():
    languages = input("Language: ").split()
    languages.sort()
    print(" ".join(languages))



# 4. Виведіть елементи списку в зворотному порядку, не змінюючи сам список.
def task_4():
    num = [1, 2, 3, 4, 5, 6, 7, 8 , 9]
    print(" ".join(map(str, num[::-1])))


# 5. Виведіть всі елементи списку з парними індексами. Вводиться список чисел. Всі числа списку знаходяться на одному рядку.

def task_5():
    num  = list(map(int, input("Enter: ").split()))
    print(" ".join(map(str, num[::2])))


# 6. Визначте, скільки різних слів у введеному рядку.
def task_6():
    text = "New Delhi New York Paris Prague Reykjavik"
    words = text.split()
    new_words = set(words)
    print(len(new_words))

# 7. Напишіть програму, яка приймає послідовність чисел, розділених комами, від користувача і створює список і кортеж з цими числами.
def task_7():
    num = input("Enter: ")
    num_list = [int(n.strip()) for n in num.split(" ")]

    num_tuple = tuple(num_list)
    print(num_list)
    print(num_tuple)

# 8. Напишіть програму для отримання частини рядка URL, що позначає назву ресурсу.
def task_8():
    url = input("Enter URL : ")
    http = url.split("/")[-1]
    print(http)


# 9. Для введеної послідовності унікальних цілих чисел, поміняйте місцями мінімальний та максимальний елементи цієї послідовності. Надрукуйте отриманий список.
def task_9():
    num = list(map(int, input("Enter : ").split()))

    num_max = num.index(max(num))
    num_min = num.index(min(num))

    num[num_max], num[num_min] = num[num_min],num[num_max]
    print(num)

# 10. Напишіть програму, яка приймає послідовність рядків (порожній рядок для завершення програми) як вхідний рядок і друкує рядки у верхньому регістрі.

def task_10():
    text = []
    while True:
        line = input("Enter : ")
        if line == "":
            break
        text.append(line.upper())
    for n in text:
        print(n)

# 11. У введеному списку цілих чисел, знайдіть і надрукуйте сусідні елементи, які мають однаковий знак. Якщо такої пари немає, не повинно нічого виводитися.
def task_11():
    num = list(map(int, input("Enter : ").split()))
    for i in range(len(num)-1):
        if num[i] * num[i+1]>0:
            print(num[i], num[i+1])




# 13. Напишіть програму для друку елементів певного цілочисельного списку після видалення з нього парних чисел. Значення списку вводяться через пропуск в одному рядку.
def task_13():
    num = list(map(int, input("Enter : ").split()))
    new_num = [n for n in num if n%2 != 0]
    print(new_num)


# 16 Напишіть програму для видалення кожного третього елемента із цілочисельного списку і друку результуючого списку, доки список не стане порожнім. Початковий список цілих чисел вводиться в одному рядку через пропуск.

# Вхідні дані:  2 5 8 9 4 78 7 1
def task_16():
    numbers = list(map(int, input("Enter list: ").split()))

    index = 2 
    while len(numbers) > index:
        # index = 
        numbers.pop(index)
        
        print(numbers)


# 17. Користувач вводить два цілих додатних числа n і m. Напишіть програму, яка створює двовимірний масив розміром n x m і заповнює його символами . і * у шаховому порядку (як у вихідних даних). Лівий верхній кут повинен мати символ ..
def task_17():
    n = int(input("n: "))
    m = int(input("m: "))

    for row in range(n):
        for col in range(m):
            if (row + col) % 2 == 0:
                print(".", end = " ")
            else:
                print("*", end = " ")

        print()
