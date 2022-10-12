import math 

def fun(i):
    return math.exp(i) + math.sqrt(math.fabs(i))

def frange(x, y, jump):
    while x < y:
        yield x
        x += jump

a = float(input("Введіть нижню границю: "))
b = float(input("Введіть верхню границю: "))
h = float(input("Введіть крок: "))

list_range = []

for i in frange(a, b, h):
    list_range.append(fun(i))

print(list_range)
print(list_range[0:4])