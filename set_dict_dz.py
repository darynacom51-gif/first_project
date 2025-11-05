# 6. Напишіть програму для створення словника із введеного рядка символів для підрахунку кількості символів.

# Вхідні дані: Lorem ipsum dolor sit amet

# text = input("Enter text: ")
def task6():
    text = "Lorem ipsum dolor sit amet"
    symbols = []    # порожній список 

    for n in text:
        if n not in symbols:    
            symbols.append(n)#якщо символ ще не був доданий, додаємо без повторів

    symbol_count = {}

    for n in symbols:   #проходимо по кожному символу зі списку
        symbol_count[n] = text.count(n)#підрахунок кількості symbol в text

    print(symbol_count)
# task6()


# 7. Напишіть програму, яка приймає рядок символів, і обчислює кількість букв і цифр.

# Вхідні дані: Project Gutenberg offers over 59,000 free eBooks
# Вихідні дані: LETTERS 36 DIGITS 5

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



# 8. Напишіть програму для видалення дублікатів зі списку цілих чисел.

def task_8():

    num = [1, 1, 1, 2, 3, 4, 5, 6, 6 , 7, 7, 8]
    num_new = list(set(num))
    print(num_new)



# 9. Дано список словників. Кожен словники має 2 пари елементів: ключ 'name' і значення імені студента, ключ 'points' і значення - список балів з різних дисциплін (цілі двоцифрові числа). Надрукуйте найменші значення балів, отримані кожним студентом, в один рядок з пропуском.
def task_9():
    students =[
        {"name": "Daryna", "points": [55, 80, 90]},
        {"name": "Maryna", "points": [15, 70, 10]},
        {"name": "Karyna", "points": [25, 90, 99]},
    ]

    for person in students:
        points_min = min(person["points"])
        print(f"{person["name"]} : {points_min}", end = " ")





# 11. Дано три словники, в яких ключами є малі букви латинського алфавіту, а значеннями - цілі числа. Ключі у всіх словниках – різні, їх є по 3 в кожному словнику. Об’єднайте всі три словники в один і виведіть його вміст. Підказка. скористайтеся оператором **, що використовується для об’єднання довільної кількості словників.
def task_11():
    first = {"a": 5, "b": 10, "c": 15}
    second = {"q" : 1, "w" : 2, "e" : 3}
    third = {"r" : 7, "t": 8, "y" : 9}

    all_together = {**first, **second, **third}
    print(all_together)






# 12. Створіть словник, який відображає ідентифікатори акцій на біржі. Ключами словника є ідентифікатори акцій, а значеннями - дійсні числа - ціни акцій. Надрукуйте ціни акцій та ідентифікатори у порядку зростання ціни.
def task_12():
    actions = {
                "FB" : 10.75,
                "AAPL" : 612.78,
                "HPQ" : 37.2,
                "IBM" : 205.55,
                "ACME" : 45.23,
                "AAPL" : 612.78
    }

    for key, value in sorted(actions.items(), key = lambda item: item[1]):
        print(f"{key}:{value}")


# 13. В рядку записаний текст. Словом вважається послідовність непробільних символів, які йдуть підряд, слова розділені одним або більшим числом пропуском або символами кінця рядка. Для кожного слова з цього тексту підрахуйте, скільки разів воно зустрічалося в цьому тексті раніше.
def task_13():
    text = "var list set tuple list tuple tuple dict var"
    word = text.split()    #робимо список
    n = {}  #для підрахунку кожного слова

    for i in  word:
        print(n.get(i, 0), end =" ")
        n[i] = n.get(i, 0) +1 
 


# 14. Напишіть програму, яка зможе підрахувати слова у введеному рядку, розділені пропуском і вивести отриману статистику: для кожного унікального слова обчислити число його повторень (без урахування регістру), слова не повинні повторюватися, порядок слів довільний.
def task_14():

    text = "a bb acD bb abc ac BCD a"
    words = text.lower().split()
    n = {}  #словник для підрахунку

    for i in words: # кількість кожного слова
        n[i]=n.get(i,0)+1

    for word, count in n.items():
        print(word, count)




# 15. Дано два списки чисел. Знайдіть всі числа, що зустрічаються як в першому, так і другому списках, і надрукуйте їх у порядку зростання.

first = [2, 5, 8, 11, 10, 9]
second = [11, 3, 7, 6, 8, 5]

first_new = set(first)
second_new = set(second)

together = first_new & second_new
print(together)