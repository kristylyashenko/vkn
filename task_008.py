import math 

def fun(a):
    return math.exp(a) + math.sqrt(math.fabs(a))

a = float(input("Введіть нижню границю: "))
b = float(input("Введіть верхню границю: "))
h = float(input("Введіть крок: "))

while a < b:
    print(fun(a))
    a = a + h