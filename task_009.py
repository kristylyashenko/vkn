import math 

def fun(x):
    return math.exp(x) + math.sqrt(math.fabs(x))

a = int(input("Введіть нижню границю: "))
b = int(input("Введіть верхню границю: "))
h = int(input("Введіть крок: "))

list_range = []

for i in range(a, b, h):
    list_range.append(fun(i))

print(list_range)
print(list_range[0:4])