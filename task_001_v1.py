# **task_001_v1.py** - програма для розв'язання завдання варіант №1

num_all = int(input("введіть число: "))

num_1 = num_all // 10000
num_2 = num_all // 1000 % 10
num_3 = num_all % 1000 // 100
num_4 = num_all % 100 // 10
num_5 = num_all % 10

print("Добуток першого та п'ятого числа: ", num_1 * num_5)
print("Сума другого та третього числа: ", num_2 + num_3)