#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Diapason:

    def __init__(self, first=0.0, second=0.0):
        if not isinstance(first, (int, float)) or \
           not isinstance(second, (int, float)):
            raise ValueError

        if first > second:
            raise ValueError

        self.__first = float(first)
        self.__second = float(second)

    @property
    def first(self):
        return self.__first

    @property
    def second(self):
        return self.__second

    # Чтение границ с клавиатуры
    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = line.split()

        if len(parts) != 2:
            raise ValueError

        try:
            first = float(parts[0])
            second = float(parts[1])
        except ValueError:
            raise ValueError

        if first > second:
            raise ValueError

        self.__first = first
        self.__second = second

    # Вывод диапазона
    def display(self):
        print(f"[{self.__first}, {self.__second}]")

    # Принадлженость диапазону
    def rangecheck(self, x):
        if not isinstance(x, (int, float)):
            raise ValueError

        return self.__first <= x <= self.__second


# Внешняя функция
def make_diapason(first, second):
    if not isinstance(first, (int, float)) or \
       not isinstance(second, (int, float)):
        raise ValueError

    if first > second:
        raise ValueError

    return Diapason(first, second)


if __name__ == '__main__':
    d1 = Diapason(1.5, 3.7)
    d1.display()

    d2 = Diapason()
    d2.read("Введите границы через пробел: ")
    d2.display()

    d3 = make_diapason(0.0, 10.0)
    d3.display()

    print("2.0 в диапазоне [1.5, 3.7]:", d1.rangecheck(2.0))
    print("1.5 в диапазоне [1.5, 3.7]:", d1.rangecheck(1.5))
    print("3.7 в диапазоне [1.5, 3.7]:", d1.rangecheck(3.7))
