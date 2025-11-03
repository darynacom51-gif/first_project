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


n = int(input("n: "))
m = int(input("m: "))

for row in range(n):
    for col in range(m):
        if (row + col) % 2 == 0:
            print(".", end = " ")
        else:
            print("*", end = " ")

    print()