import math 

def fun(i):
    return math.exp(i) + math.sqrt(math.fabs(i))

def frange(x, y, jump):
    while x < y:
        yield x
        x += jump

a = float(input("Введіть нижню гр1аницю: "))
b = float(input("Введіть верхню границю: "))
h = float(input("Введіть крок: "))

for i in frange(a, b, h):
    print(fun(i))