import math

x = int(input("Введіть значення x: "))

f = math.fabs(math.sin(2*x) + math.cos(3*x + 1) + math.tan(math.fabs(x) + 0.7)) + math.log10(math.fabs(x - 4))

print("Результат значення f: ", f)