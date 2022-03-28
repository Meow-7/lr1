# Дано два ненульових числа. Знайти суму, різницю, добуток і частку їх квадратів.
v1 = int(input("1 number = "))
v2 = int(input("2 number = "))


def summ():
    print(v1+v2)


def difference():
    print(abs(v1-v2))


def product():
    print(v1 * v2)


def fraction():
    print(v1/v2)


summ()
product()
difference()
fraction()
