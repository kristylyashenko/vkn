import math 

def fun(x):
    return math.exp(x) + math.sqrt(math.fabs(x))

a = int(input("Введіть нижню границю: "))
b = int(input("Введіть верхню границю: "))
h = int(input("Введіть крок: "))

for i in range(a, b, h):
    print(fun(i))