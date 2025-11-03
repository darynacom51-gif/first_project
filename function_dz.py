# 5. Напишіть функцію для визначення найбільшого з трьох цілих чисел з використанянм вбудованої функції max().

# def max_3 (num_1, num_2, num_3):
#     return max(num_1, num_2, num_3)

# num_1 = int(input("Num 1 : "))
# num_2 = int(input("Num 2 : "))
# num_3 = int(input("Num 3 : "))

# print(max_3 (num_1, num_2, num_3))
#_______________________________________________________________________________

# 7. Напишіть функцію, яка повертає назву пори року для введеного значення номера місяця.


# def time_of_year(season):
#     match season:                   # використала конструкцію match-case
#         case 12 | 1 | 2 :           # порівню season з кожним блоком case
#             return print("Winter")
        
#         case 3 | 4 | 5 :
#             return print("Spring")
        
#         case 6 | 7 | 8 :
#             return print ("Summer")
        
#         case 9 | 10 | 11 :
#             return print("Autumn")
#         case _ :                        # case _ все інше
#             return print("Error...")


# season = int(input("Enter month: "))
# print(time_of_year(season))

#_______________________________________________________________________________


# 8. Напишіть функцію для створення гістограми (наприклад, у вигляді *) із заданого списку цілих чисел як у вихідних даних. Формат введення списку чисел як у вхідних даних.

# def function_(n):
#     print("\n".join("*" * i for i in n)) # генератор створення рядку з * / також об'єднання join через новий рядок "\n"

# n = list(map(int, input("Enter n: ").split(","))) #map перетворює у int / list перетворює у список

# function_(n)

#_______________________________________________________________________________


# 9. Напишіть функцію для визначення, чи рік високосний чи ні.


# def leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return print("Високосний")
#     else:
#         return print("Не високосний")

# year = int(input("Year: "))
# leap_year(year)

#_______________________________________________________________________________

# 11. На стадіоні є три категорії місць для сидіння: місця класу A коштують a грошових одиниць, місця класу B коштують b грошових одиниць, а місця класу C - c грошових одиниць. Напишіть першу функцію, яка запитує скільки продано квитків на кожний клас місць, і другу функцію, яка відображає суму отриманого доходу від продажу квитків на кожен клас окремо і загалом. Формати введення і виведення такі, як у вхідних і вихідних даних.
def task_11():
    def tickets_a_b_c():
        tickets = {         #словник з кортежем класів, цін і місць
            "A": (20.50, 45),
            "B": (15.75, 30),
            "C": (10.55, 15)
        }
        return tickets

    def sum_tickets(tickets):#сума з класів і загальний дохід
        money_from_class = {}    #словник доходу кожного з класів
        sum_money = 0              #змінна для загального доходу

        for class_ , (price_class, sold_tickets) in tickets.items():#дохід кожного з класів
            money_from_class[class_] = price_class * sold_tickets
            sum_money = sum_money + money_from_class[class_]

        return money_from_class, sum_money

    new_tickets = tickets_a_b_c()
    all_money = sum_tickets(new_tickets)
    print(all_money)




#_______________________________________________________________________________
# 12. Напишіть функцію, яка перевіряє, чи рядок є паліндром чи ні. Регістр літер, пропуски і знаки пунктуації не враховувати.
#Паліндром - це слово, фраза або послідовність, яка читається так само як зліва направо, так і справа наліво.


def task12():
    def palindrom(text):
        text = text.lower()
        text_with_out = ""

        for symbol in text:
            if symbol.isalnum(): # для перевірки чи літера чи цифра
                text_with_out = text_with_out + symbol
        return text_with_out == text_with_out [::-1]# читання зліва направо і справа на ліво

    text_input = input("Enter text: ")

    if palindrom(text_input):
        print("Palindrom")
    else:
        print("not Palindrom")

#_______________________________________________________________________________
# 13. Напишіть рекурсивну функцію, яка обчислює суму цілих чисел a і b. З арифметичних операцій використовується тільки додавання одиниці і віднімання одиниці.
def task_13():
    def sum_a_b(a, b):
        if a == 0:
            return b
        elif b == 0:
            return a
        elif a > 0:
            return sum_a_b(a - 1, b + 1)
        else:
            return sum_a_b(a + 1, b -1)
        
    a = int(input("a: "))
    b = int(input("b: "))
    print(sum_a_b(a,b))



#_______________________________________________________________________________
# 14. Дано послідовність цілих чисел, що закінчується числом 0. Напишіть рекурсивну функцію, яка друкує цю послідовність в зворотному порядку. При розв’язуванні цього завдання не можна користуватися списками.
def task_14():
    def sequence_in_reverse():
        reverse = int (input("Enter sequence integers : "))

        if reverse != 0:
            sequence_in_reverse()
            print(reverse)
    sequence_in_reverse()


#_______________________________________________________________________________
