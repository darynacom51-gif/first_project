# ax^2 + bx + c = 0

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# d = b**2 - 4*a*c

# if d < 0:
#     print("Коренві немає")
# elif d == 0:
#     x = (-b) / (2*a)
#     print("Корінь один: х =", x)
# else:
#     x1 = (-b - d**0.5) / (2*a)
#     x2 = (-b + d**0.5) / (2*a)
#     print(f"x1 = {x1}, x2 = {x2}")


#2
# a = int(input("a: "))
# b = int(input("b: "))

# if a > b:
#     # a = b     # обмін значеннями змінних
#     # b = a
#     a, b = b, a

# for i in range(a, b+1):
#     print(i)


#3 таймер зворотного відліку

# n = int(input("Enter sec: "))

# for i in range(n, 0, -1):
#     print(i)
# print("Start")

#------через while

# n = int(input("Enter sec: "))

# while n > 0:
#     print(n)
#     n -= 1  # n = n-1

# print("Start")


#__________________________________________________________

# 8 Намалювати сходинки як у вихідних даних, використовуючи символи пропуску і решітки #, коли на вхід програми подається ціле число n - кількість сходинок.

# n = int(input("Couunt: "))

# for el in range(1, n+1):
#     print("#" * el)

# while n > 0:
#     print("#" * n)
#     n -= 1  # n = n-1

#__________________________________________________________

#9 За даним цілим додатнім числом n обчисліть n! - значення факторіалу цього числа.
#Факторіал: n! = 1 * 2 * 3 * ... * (n-1) * n

# n = int(input("Count: "))

# 5! = 1 * 2 * 3 * 4 * 5 -> range(1, n+1)
# 5! = 5 * 4 * 3 * 2 * 1  -> while n > 0: n -= 1

# f = 1
# for i in range(1, n+1):
#     print(i)
#     f *= i
# print(f)

# print("------------------------------")
# f = 1
# while n > 0:
#     print(n)
#     f *= n 
#     n -= 1
   
# print(f)






def averadge():
    n = int(input("Count: "))
    f = 1
    while n > 0:
        print(n)
        f *= n 
        n -= 1
    print(f)

averadge()