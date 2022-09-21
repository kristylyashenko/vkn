import math

x = int(input("Введіть значення x: "))
y = int(input("Введіть значення y: "))

def func(x, y):
    return ((x ** 3 + y ** 3) ** 1/4) + math.sin(3*x + 1) + math.log1p(math.fabs(x)) - math.e ** y-x

print("Результат значення f: ", func(x, y))