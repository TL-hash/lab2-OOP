#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 Задание 1 (Вариант 7).

Парой называется класс с двумя полями, которые обычно имеют имена first и second.
Требуется реализовать тип данных с помощью такого класса. Во всех заданиях обязательно
должны присутствовать:
1. метод инициализации __init__; метод должен контролировать значения аргументов на корректность;
2. ввод с клавиатуры read;
3. вывод на экран display.

Реализовать внешнюю функцию с именем make_тип(), где тип – тип реализуемой структуры.
Функция должна получать в качестве аргументов значения для полей структуры и возвращать
структуру требуемого типа. При передаче ошибочных параметров следует выводить сообщение
и заканчивать работу.

В раздел программы, начинающийся после инструкции if __name__ == '__main__': добавить
код, демонстрирующий возможности разработанного класса.

Поле first – дробное число, левая граница диапазона; поле second – дробное число,
правая граница диапазона. Реализовать метод rangecheck() – проверку заданного числа
на принадлежность диапазону.
"""


class Diapason:

    def __init__(self, first=0.0, second=0.0):
        if not isinstance(first, (int, float)) or \
           not isinstance(second, (int, float)):
            raise TypeError

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

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = line.split()

        if len(parts) != 2:
            raise ValueError

        first = float(parts[0])
        second = float(parts[1])

        if first > second:
            raise ValueError

        self.__first = first
        self.__second = second

    def display(self):
        print(f"[{self.__first}, {self.__second}]")

    def rangecheck(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError

        return self.__first <= x <= self.__second


def make_diapason(first, second):
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
