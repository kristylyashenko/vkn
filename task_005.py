import math

x = float(input("Введіть х: "))     

def f1(x1):
     rez = (2.25 + x) + x**2 + math.log1p(math.fabs(x))
     return(rez)
def f2(x2):
     rez = math.e**2 + (12 * x**2 - 1) / (x + 9)
     return(rez)
def f3(x3):
     rez = math.log1p(math.fabs(x)) - math.e**x
     return(rez) 

y = 0.0

if x >= 3.86:
     y = f1(x)
elif 1.54 < x < 3.86:
     y = f2(x)
elif x <= 1.54:
     y = f3(x)

print(y)