import math

Ax = float(input("Введіть координати точки Ax: "))
Ay = float(input("Введіть координати точки Ay: "))

Bx = float(input("Введіть координати точки Bx: "))
By = float(input("Введіть координати точки By: "))

Cx = float(input("Введіть координати точки Cx: "))
Cy = float(input("Введіть координати точки Cy: "))

def distance(x, y):
    return math.sqrt(x**2 + y**2)

A = distance(Ax, Ay)
B = distance(Bx, By)
C = distance(Cx, Cy)

if A < B and A < C:
    print("A minimum: ", A)
elif B < A and B < C:
    print("B minimum: ", B)
elif C < A and C < B:
    print("C minimum: ", C)