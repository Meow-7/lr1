#Дана сторона квадрата a. Знайти його площу S=a^2
#Шимрило Олексій
a = int(input("Square side = "))


def find_area(a):
    s = a ** 2
    print("Square area =", s)
    return s


find_area(a)
