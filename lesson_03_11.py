# 16 Напишіть програму для видалення кожного третього елемента із цілочисельного списку і друку результуючого списку, доки список не стане порожнім. Початковий список цілих чисел вводиться в одному рядку через пропуск.

# Вхідні дані:  2 5 8 9 4 78 7 1

# numbers = list(map(int, input("Enter list: ").split()))

# index = 2 
# while len(numbers) > index:
#     # index = 
#     numbers.pop(index)
    
#     print(numbers)


numbers = list(map(int, input("Enter list: ").split()))

index = 2 
while numbers:
    index = 4
    index %= len(numbers)
    numbers.pop(index)
    print(numbers)
    