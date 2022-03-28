# За довжинами двох сторін деякого трикутника і кутом між ними знайти довжину третьої сторони і
# площу цього трикутника.
# Шимрило Олексій
from math import*
a = int(input("1 Triangle side = "))
b = int(input("2 Triangle side = "))
q = int(input("Angle between sides = "))


def find_side_area():                     # площа за формулой герона  i  3 сторона за теоремой косинусов
    c = sqrt(a ** 2 + b ** 2 - 2 * a * b * cos((q * 180) / pi))
    print("Third side = ", c)
    p = (a+b+c)/2
    s = sqrt(p*(p-a)*(p-b)*(p-c))
    print("Triangle area =", s)


find_side_area()
