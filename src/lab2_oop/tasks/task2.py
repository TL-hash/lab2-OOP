#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Задание 2 (Вариант 7).

Составить программу с использованием классов и объектов для решения задачи.
Во всех заданиях, помимо указанных в задании операций, обязательно должны быть
реализованы следующие методы:
1. метод инициализации __init__;
2. ввод с клавиатуры read;
3. вывод на экран display.

В раздел программы, начинающийся после инструкции if __name__ == '__main__': добавить
код, демонстрирующий возможности разработанного класса.

Создать класс Date для работы с датами в формате «год.месяц.день». Дата представляется
структурой с тремя полями типа unsigned int: для года, месяца и дня. Класс должен
включать не менее трех функций инициализации: числами, строкой вида «год.месяц.день»
(например, «2004.08.31») и датой. Обязательными операциями являются: вычисление
даты через заданное количество дней, вычитание заданного количества дней из даты,
определение високосности года, присвоение и получение отдельных частей (год, месяц, день),
сравнение дат (равно, до, после), вычисление количества дней между датами.
"""


class Date:

    def __init__(self, year=None, month=None, day=None,
                 date_str=None, date=None):
        #если передали строку — разбираем её
        if date_str is not None:
            if not isinstance(date_str, str):
                raise TypeError
            parts = date_str.split('.')
            if len(parts) != 3:
                raise ValueError
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])

        #если передали другую дату — копируем
        elif date is not None:
            if not isinstance(date, Date):
                raise TypeError
            year = date.year
            month = date.month
            day = date.day

        #если ничего не передали — дата по умолчанию
        elif year is None and month is None and day is None:
            year = 2000
            month = 1
            day = 1

        #если числа переданы не полностью — ошибка
        elif year is None or month is None or day is None:
            raise ValueError

        if not isinstance(year, int) or not isinstance(month, int) \
                or not isinstance(day, int):
            raise TypeError

        if year < 0 or month < 1 or month > 12 or day < 1:
            raise ValueError

        if day > self.__days_in_month(year, month):
            raise ValueError

        self.__year = year
        self.__month = month
        self.__day = day

    @property
    def year(self):
        return self.__year

    @property
    def month(self):
        return self.__month

    @property
    def day(self):
        return self.__day

    def __is_leap(self, year):
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        return False

    def __days_in_month(self, year, month):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and self.__is_leap(year):
            return 29
        return days[month - 1]

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = line.split('.')

        if len(parts) != 3:
            raise ValueError

        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])

        if year < 0 or month < 1 or month > 12 or day < 1:
            raise ValueError

        if day > self.__days_in_month(year, month):
            raise ValueError

        self.__year = year
        self.__month = month
        self.__day = day

    def display(self):
        print(f"{self.__year:04d}.{self.__month:02d}.{self.__day:02d}")


    def is_leap(self):
        return self.__is_leap(self.__year)

    def add_days(self, n):
        if not isinstance(n, int) or n < 0:
            raise TypeError

        year = self.__year
        month = self.__month
        day = self.__day

        for _ in range(n):
            day += 1
            if day > self.__days_in_month(year, month):
                day = 1
                month += 1
                if month > 12:
                    month = 1
                    year += 1

        return Date(year, month, day)

    def sub_days(self, n):
        if not isinstance(n, int) or n < 0:
            raise TypeError

        year = self.__year
        month = self.__month
        day = self.__day

        for _ in range(n):
            day -= 1
            if day < 1:
                month -= 1
                if month < 1:
                    month = 12
                    year -= 1
                day = self.__days_in_month(year, month)

        return Date(year, month, day)

    def days_between(self, other):
        if not isinstance(other, Date):
            raise TypeError

        if self.before(other):
            small = self
            big = other
        else:
            small = other
            big = self

        #от меньшей даты шагаем вперёд, пока не дойдём до большей
        count = 0
        current = Date(small.year, small.month, small.day)

        while not current.equals(big):
            current = current.add_days(1)
            count += 1

        return count

    def equals(self, other):
        if not isinstance(other, Date):
            raise TypeError
        return (self.__year == other.year) and \
               (self.__month == other.month) and \
               (self.__day == other.day)

    def before(self, other):
        if not isinstance(other, Date):
            raise TypeError
        if self.__year != other.year:
            return self.__year < other.year
        if self.__month != other.month:
            return self.__month < other.month
        return self.__day < other.day

    def after(self, other):
        if not isinstance(other, Date):
            raise TypeError
        return not self.before(other) and not self.equals(other)

    def set_year(self, year):
        if not isinstance(year, int) or year < 0:
            raise TypeError
        self.__year = year

    def set_month(self, month):
        if not isinstance(month, int) or month < 1 or month > 12:
            raise TypeError
        self.__month = month

    def set_day(self, day):
        if not isinstance(day, int) or day < 1:
            raise TypeError
        if day > self.__days_in_month(self.__year, self.__month):
            raise ValueError
        self.__day = day


def make_date(year=2000, month=1, day=1):
    return Date(year, month, day)


if __name__ == '__main__':
    #создание числами
    d1 = Date(2004, 8, 31)
    d1.display()

    #создание строкой
    d2 = Date(date_str="2004.02.29")
    d2.display()

    #создание копией
    d3 = Date(date=d2)
    d3.display()

    #ввод с клавиатуры
    d4 = Date()
    d4.read("Введите дату в формате год.месяц.день: ")
    d4.display()

    #високосность
    print(d1.is_leap())
    print(d2.is_leap())

    #прибавление / вычитание дней
    d5 = d1.add_days(10)
    d5.display()

    d6 = d1.sub_days(10)
    d6.display()

    #разница между датами
    print(d1.days_between(d2))

    #сравнения
    print(d1.equals(d2))
    print(d1.before(d2))
    print(d1.after(d2))

    #получение и установка частей
    print(d1.year, d1.month, d1.day)
    d1.set_year(2020)
    d1.set_month(2)
    d1.set_day(29)
    d1.display()

    d7 = make_date(1999, 12, 31)
    d7.display()
