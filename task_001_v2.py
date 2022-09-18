# **task_001_v2.py** - програма для розв'язання завдання варіант №2
str_user = input("Введіть п'ятизначне число: ")

map_obj = map(int, str_user)

list_chisel = list(map_obj)

print("Добуток першого та п'ятого числа: ", list_chisel[0] * list_chisel[4])
print("Сума другого та третього числа: ", list_chisel[1] + list_chisel[2])