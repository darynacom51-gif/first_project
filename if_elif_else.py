#Ви придбали товар на певну суму s. 
# Скільки купюр різного номіналу треба віддати продавцю, якщо починати платити з найбільших?
# У вас є 1, 2, 5, 10, 100, 500 гривень.

# sum = int(input("Enter sum:"))
# money_500 = sum // 500
# sum = sum % 500

# money_100 = sum // 100
# sum = sum % 100

# money_10 = sum // 10
# sum = sum % 10

# money_5 = sum // 5
# sum = sum % 5

# money_2 = sum // 2
# sum = sum % 2

# money_1 = sum // 1
# sum =  sum % 1

# print("count 500 ", money_500)
# print("count 100 ", money_100)
# print("count 10 ", money_10)
# print("count 2 ", money_2)
# print("count 1 ", money_1)
#-------------------------------------------------------------------------------

# Розгалудження

#1. Напишіть програму, в якій користувач вводить пароль і якщо він співпадає із наперед визначеним паролем для цього користувача, то виводиться повідомлення Password accepted.. У іншому випадку повідомлення буде Sorry, that is the wrong password..

# password = 1111
# password_ = int(input ("Enter password: "))
# if password_ == password:
#     print("Password accepted")
# else:
#     print("Sorry, that is the wrong password")

#-------------------------------------------------------------------------------


#2. Користувачем вводиться два імені. Використовуючи конструкцію розгалуження програма повинна вивести імена в алфавітному порядку.
# first_name = input("Enter first name: ")
# second_name = input("Enter second name: ")
# if first_name < second_name:
#     print(first_name, second_name)
# else:
#     print(second_name, first_name)
#-------------------------------------------------------------------------------


#3. Напишіть програму, яка виводить назви введених чисел. Користувач вводить ціле число. Якщо це число або 1 або 2 або 3, то виводиться повідомлення - назва числа, відповідно, One, Two, Three. В усіх інших випадках виводиться слово Unknown.

# num = int(input("Enter number: "))
# if num == 1:
#     print("One")
# elif num == 2:
#     print("Two")
# elif num == 3:
#     print("Three")
# else:
#     print("Unknown")


#4. Користувач вводить дві різних англійські літери в окремих рядках. Напишіть програму, яка виводить повідомлення про місце розташування однієї літери відносно іншої у алфавіті.
# first_letter = input("Enter first letter: ").lower() #метод для маленьких букв
# second_letter = input("Enter second letter: ").lower()
# if first_letter < second_letter:
#     print(first_letter, "comes before", second_letter)
# else:
#     print(second_letter, "comes after" ,first_letter)

#другий варіант з застосуванням методу lower.()
# first_letter = input("Enter first letter: ") 
# second_letter = input("Enter second letter: ")
# if first_letter.lower() == second_letter.lower():
#     if first_letter < second_letter:
#         print("first letter", first_letter, "Second letter", second_letter)
#     else:
#         print("first letter", second_letter, "Second letter", first_letter)
# elif first_letter.lower() < second_letter.lower():
#     print("first letter", first_letter, "Second letter", second_letter)
# else:
#     print("first letter", second_letter, "Second letter", first_letter)


#-------------------------------------------------------------------------------

# 5. Напишіть програму, в якій користувач вводить значення температури, і, якщо це значення менше або дорівнює 0 градусів Цельсія, необхідно вивести повідомлення A cold, isn’t it?. Якщо ж температура становить більше 0 і менше 10 градусів Цельсія повідомлення буде Cool., у інших випадках Nice weather we’re having..

# temperature = float(input("Enter temperature: "))
# if temperature <= 0:
#     print("Cold, isn’t it?")
# elif temperature < 10:
#     print("Cool")
# else:
#     print("Nice weather we’re having")
#-------------------------------------------------------------------------------






# Середній рівень

#1. Визначте назву геометричної фігури за введеною кількістю її сторін. Програма повинна підтримувати фігури від 3 до 6 сторін. Якщо введена кількість сторін поза межами цього діапазону, програма повинна відображати відповідне повідомлення.

# geometric_figure = int(input("Кількість сторін еометричної фігури (від 3 до 6): "))
# if geometric_figure == 3:
#     print("Трикутник")
# elif geometric_figure == 4:
#     print("Квадрат, прямокутник")
# elif geometric_figure == 5:
#     print("П'ятикутник")
# elif geometric_figure == 6:
#     print("Шестикутник")
# else:
#     print("Кількість сторін поза межами діапазону")



#-------------------------------------------------------------------------------

#2. Ігрове поле рулетки поділено на номери від 0 до 36, які мають чорний, червоний або зелений кольори. Номер 0 має зелений колір, для номерів від 1 до 10, непарні номери - червоні, а парні - чорні. Непарні номери від 11 до 18 - чорні, а парні номери - червоні. Непарні номери від 19 до 28 - червоні, а парні номери - чорні. Непарні номери від 29 до 36 - чорні, а парні номери - червоні. Напишіть програму, яка отримує номер (число від 0 до 36) та показує, чи є номер зеленим, червоним або чорним. Програма повинна враховувати варіант, якщо користувач вводить номер, який знаходиться за межами діапазону від 0 до 36.

num_ber = int(input("Введіть номер від 0 до 36: "))

if num_ber == 0:
    print("Зелений")
elif 1 <= num_ber <= 10:
    if num_ber % 2 == 0: # 1, 3, 5, 7, 9 - червоні (непарні)
        print("Чорний")  # 2, 4, 6, 8, 10 - чорні (парні)
    else:
        print("Червоний")

elif 11 <= num_ber <= 18:
    if num_ber % 2 == 0:
        print("Червоний")
    else:
        print("Чорний")


elif 19 <= num_ber <= 28:
    if num_ber % 2 == 0:
        print("Чорний")
    else:
        print("Червоний")

elif 28 <= num_ber <= 36:
    if num_ber % 2 == 0:
        print("Червоний")
    else:
        print("Чорний")




#-------------------------------------------------------------------------------


# Дано дві точки: A (x1, y1) і B (x2, y2). Напишіть програму, яка визначає, яка із точок знаходиться далі від початку координат.

#  Вхідні дані: 
#  1 
#  2 
#  3 
#  2 
#  4 
#  4 
#  4 
#  4 

#  Вихідні дані: 
#  B 
#  The distance is the same 

# a_x1 = float(input("Введіть x1: "))
# a_y1 = float(input("Введіть y1: "))
# b_x2 = float(input("Введіть x2: "))
# b_y2 = float(input("Введіть y2: "))

# a_distance = 